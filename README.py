import subprocess
import os
import argparse


def get_pods(namespace):
    """Получаем список подов в указанном namespace."""
    try:
        # Выполняем команду kubectl для получения списка подов.
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
        # Преобразуем результат в список.
        return pods.decode("utf-8").split()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды kubectl: {e}")
        return []


def save_logs(pod_name, namespace, logs_dir):
    """Сохраняем логи пода в файл."""
    try:
        # Убедимся, что директория для логов существует.
        os.makedirs(logs_dir, exist_ok=True)
        # Определяем имя файла для логов.
        log_file = os.path.join(logs_dir, f"{pod_name}.log")
        # Выполняем команду kubectl logs и записываем результат в файл.
        with open(log_file, "w") as f:
            subprocess.run(["kubectl", "logs", pod_name, "-n", namespace], stdout=f)
        print(f"Логи пода {pod_name} сохранены в {log_file}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при получении логов пода {pod_name}: {e}")


def main(namespace, logs_dir="logs"):
    # Получаем список всех подов в указанном namespace.
    pods = get_pods(namespace)
    if not pods:
        print("Подов не найдено.")
        return

    # Для каждого пода сохраняем логи.
    for pod_name in pods:
        save_logs(pod_name, namespace, logs_dir)


if __name__ == "__main__":
    # Настраиваем парсер аргументов командной строки.
    parser = argparse.ArgumentParser(description="Сбор логов подов Kubernetes.")
    parser.add_argument(
        "--namespace", required=True, help="Имя неймспейса в Kubernetes."
    )
    parser.add_argument(
        "--logs-dir", default="logs", help="Директория для сохранения логов."
    )

    args = parser.parse_args()

    # Запускаем основную функцию с переданными аргументами.
    main(namespace=args.namespace, logs_dir=args.logs_dir)


error: a container name must be specified for pod gorm-pom-config-nft01-a-1-66f4d67b6f-szrql, choose one of: [gorm-pom-config-nft01-service gorm-pom-config-nft01]
Логи пода gorm-pom-config-nft01-a-1-66f4d67b6f-szrql сохранены в ./log/gorm-pom-config-nft01-a-1-66f4d67b6f-szrql.log
error: a container name must be specified for pod gorm-pom-ui-nft01-a-1-99bb78f77-584bk, choose one of: [gorm-pom-ui-nft01-service gorm-pom-ui-nft01]
Логи пода gorm-pom-ui-nft01-a-1-99bb78f77-584bk сохранены в ./log/gorm-pom-ui-nft01-a-1-99bb78f77-584bk.log
error: a container name must be specified for pod gorm-pom-ui-nft01-b-1-796c9d887b-p4b62, choose one of: [gorm-pom-ui-nft01-service gorm-pom-ui-nft01]
Логи пода gorm-pom-ui-nft01-b-1-796c9d887b-p4b62 сохранены в ./log/gorm-pom-ui-nft01-b-1-796c9d887b-p4b62.log



