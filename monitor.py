import requests
from datetime import datetime


def check_service(service_name, url):

    try:

        start = datetime.now()

        response = requests.get(url, timeout=5)

        end = datetime.now()

        response_time = (end - start).total_seconds()

        return {
            "service_name": service_name,
            "url": url,
            "status_code": response.status_code,
            "response_time": response_time,
            "check_time": datetime.now(),
            "error_message": None
        }

    except Exception as e:

        return {
            "service_name": service_name,
            "url": url,
            "status_code": None,
            "response_time": None,
            "check_time": datetime.now(),
            "error_message": str(e)
        }