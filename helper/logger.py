import logging
import requests


logger = logging.getLogger()
logger.setLevel(logging.INFO)

response1 = requests.get(url="https://petstore.swagger.io/v2/pet/222")


def log(response, request_body=None):
    logger.info("Start Log **************************************************************")
    logger.info(f"REQUEST METHOD: {response.request.method}")
    logger.info(f"STATUS CODE: {response.status_code}")
    logger.info(f"REQUEST URL: {response.url}")
    logger.info(f"REQUEST HEADERS: {response.request.headers}")
    logger.info(f"REQUEST BODY: {request_body}\n")
    logger.info(f"STATUS CODE: {response.status_code}")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n")
    logger.info(f"RESPONSE HEADERS: {response.headers}")
    logger.info(f"RESPONSE BODY: {response.text}")
    logger.info("End Log **************************************************************\n.\n.")


log(response1)
