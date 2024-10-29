# main.py
import requests
import asyncio
from data_collector import collect_pod_logs


async def collect_and_send_logs(namespace, api_url):
    logs = collect_pod_logs(namespace)

    for pod_name, log in logs.items():
        log_entry = {"pod_name": pod_name, "log": log}
        response = requests.post(f"{api_url}/logs/", json=log_entry)
        print(f"Sent log for {pod_name}: {response.status_code}")


async def main(api_url):
    while True:
        namespace = input("Enter namespace to collect logs: ")  # Ввод неймспейса
        await collect_and_send_logs(namespace, api_url)
        await asyncio.sleep(300)  # Пауза 5 минут


if __name__ == "__main__":
    api_url = "http://localhost:5000"  # URL вашего Flask приложения
    asyncio.run(main(api_url))
