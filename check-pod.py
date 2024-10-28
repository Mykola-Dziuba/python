import subprocess
import os
import time
from plyer import notification


def run_env_script(env_script_path):
    """Run the env.sh script to set up environment variables for the Kubernetes cluster."""
    command = f'eval "$(cat {env_script_path})"'
    try:
        # Execute the command using the shell.
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed {env_script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {env_script_path}: {e}")


def get_pod_status(namespace="default"):
    """Get the status of all pods in the specified namespace."""
    try:
        result = subprocess.check_output(
            [
                "kubectl",
                "get",
                "pods",
                "-n",
                namespace,
                "-o",
                "jsonpath={.items[*].status.phase}",
            ]
        )
        statuses = result.decode("utf-8").split()
        return statuses
    except subprocess.CalledProcessError as e:
        print(f"Error getting pod statuses: {e}")
        return []


def check_pods_status(namespace="default"):
    """Check for any pods in non-running states and return True if any issues are found."""
    statuses = get_pod_status(namespace)
    problem_states = {"Error", "CrashLoopBackOff", "Pending", "Failed"}
    if any(status in problem_states for status in statuses):
        return True
    return False


def send_notification(title, message):
    """Send a Windows notification."""
    notification.notify(
        title=title,
        message=message,
        app_name="K8s Monitor",
        timeout=10,  # Duration in seconds
    )


def collect_logs(namespace):
    """Run the script to collect logs from all pods in the given namespace."""
    try:
        subprocess.run(["python", "get_pod_logs.py", "--namespace", namespace])
        print(f"Logs collected for namespace {namespace}")
    except subprocess.CalledProcessError as e:
        print(f"Error collecting logs: {e}")


def monitor_clusters(base_path, interval=600):
    """Monitor multiple Kubernetes clusters by iterating over folders with credentials."""
    while True:
        for folder_name in os.listdir(base_path):
            env_script_path = os.path.join(base_path, folder_name, "env.sh")

            if not os.path.isfile(env_script_path):
                print(f"No env.sh found in {folder_name}, skipping.")
                continue

            # Run the env.sh script to set up environment.
            run_env_script(env_script_path)

            # Define the namespace to check (you can change this or make it dynamic).
            namespace = "default"

            # Check the pod statuses.
            if check_pods_status(namespace):
                print(f"Issues found in cluster {folder_name}, namespace {namespace}")
                send_notification(
                    title="Kubernetes Cluster Alert",
                    message=f"Issues found in cluster {folder_name} in namespace {namespace}. Collecting logs.",
                )
                # Run the log collection script.
                collect_logs(namespace)
            else:
                print(
                    f"No issues found in cluster {folder_name}, namespace {namespace}"
                )

        print(f"Waiting for {interval} seconds before the next check...")
        time.sleep(interval)


if __name__ == "__main__":
    # Path where folders with env.sh files are located.
    base_path = "/path/to/your/credentials/folders"
    # Interval in seconds (e.g., 600 seconds = 10 minutes).
    interval = 600
    monitor_clusters(base_path, interval)
