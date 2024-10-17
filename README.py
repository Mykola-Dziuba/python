import subprocess
import os
import argparse


def get_pods(namespace):
    """Получаем список подов в указанном namespace."""
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
        print(f"Ошибка при выполнении команды kubectl: {e}")
        return []


def get_containers(pod_name, namespace):
    """Получаем список контейнеров в поде."""
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
        print(f"Ошибка при получении контейнеров пода {pod_name}: {e}")
        return []


def save_logs(pod_name, container_name, namespace, logs_dir):
    """Сохраняем логи контейнера в файл."""
    try:
        os.makedirs(logs_dir, exist_ok=True)
        log_file = os.path.join(logs_dir, f"{pod_name}_{container_name}.log")
        with open(log_file, "w") as f:
            subprocess.run(
                ["kubectl", "logs", pod_name, "-c", container_name, "-n", namespace],
                stdout=f,
            )
        print(
            f"Логи контейнера {container_name} пода {pod_name} сохранены в {log_file}"
        )
    except subprocess.CalledProcessError as e:
        print(
            f"Ошибка при получении логов контейнера {container_name} пода {pod_name}: {e}"
        )


def main(namespace, logs_dir="logs"):
    pods = get_pods(namespace)
    if not pods:
        print("Подов не найдено.")
        return

    for pod_name in pods:
        containers = get_containers(pod_name, namespace)
        if not containers:
            print(f"Контейнеров не найдено в поде {pod_name}.")
            continue
        for container_name in containers:
            save_logs(pod_name, container_name, namespace, logs_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Сбор логов подов Kubernetes.")
    parser.add_argument(
        "--namespace", required=True, help="Имя неймспейса в Kubernetes."
    )
    parser.add_argument(
        "--logs-dir", default="logs", help="Директория для сохранения логов."
    )

    args = parser.parse_args()
    main(namespace=args.namespace, logs_dir=args.logs_dir)
