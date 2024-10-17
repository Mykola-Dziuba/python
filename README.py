import subprocess
import os
import argparse


def get_pods(namespace):
    """Get the list of pods in the specified namespace."""
    try:
        pods = subprocess.check_output(
            [
                "kubectl",
                "get",
                "pods",
                "-n",
                namespace,
                "-o",
                "jsonpath={.items[*].metadata.name}",
            ]
        )
        return pods.decode("utf-8").split()
    except subprocess.CalledProcessError as e:
        print(f"Error executing kubectl command: {e}")
        return []


def get_containers(pod_name, namespace):
    """Get the list of containers in the pod."""
    try:
        containers = subprocess.check_output(
            [
                "kubectl",
                "get",
                "pod",
                pod_name,
                "-n",
                namespace,
                "-o",
                "jsonpath={.spec.containers[*].name}",
            ]
        )
        return containers.decode("utf-8").split()
    except subprocess.CalledProcessError as e:
        print(f"Error getting containers for pod {pod_name}: {e}")
        return []


def save_logs(pod_name, container_name, namespace, logs_dir):
    """Save the logs of the container to a file."""
    try:
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, f"{pod_name}_{container_name}.log")
        with open(log_file, "w") as f:
            subprocess.run(
                ["kubectl", "logs", pod_name, "-c", container_name, "-n", namespace],
                stdout=f,
            )
        print(
            f"Logs for container {container_name} in pod {pod_name} saved to {log_file}"
        )
    except subprocess.CalledProcessError as e:
        print(
            f"Error getting logs for container {container_name} in pod {pod_name}: {e}"
        )


def main(namespace, logs_dir="logs"):
    pods = get_pods(namespace)
    if not pods:
        print("No pods found.")
        return

    for pod_name in pods:
        containers = get_containers(pod_name, namespace)
        if not containers:
            print(f"No containers found in pod {pod_name}.")
            continue
        for container_name in containers:
            save_logs(pod_name, container_name, namespace, logs_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect logs from Kubernetes pods.")
    parser.add_argument(
        "--namespace", required=True, help="Name of the Kubernetes namespace."
    )
    parser.add_argument("--logs-dir", default="logs", help="Directory to save logs.")

    args = parser.parse_args()
    main(namespace=args.namespace, logs_dir=args.logs_dir)
