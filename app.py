import json
import schedule
import time

from database import create_database, save_log
from monitor import check_service
from reports import show_statistics, export_report


def run_monitoring():

    with open("config.json", "r") as file:
        config = json.load(file)

    services = config["services"]

    print("\n===== NEW CHECK =====")

    for service in services:

        result = check_service(
            service["name"],
            service["url"]
        )

        save_log(result)

        print(result)

    show_statistics()
    export_report()


create_database()

run_monitoring()

schedule.every(1).minutes.do(run_monitoring)

while True:
    schedule.run_pending()
    time.sleep(1)