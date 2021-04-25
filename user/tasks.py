import json
import requests
from datetime import date
from celery.decorators import task
from celery.utils.log import get_task_logger

from .models import Holiday
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings

ipgeolocation_api_key = settings.IP_GEOLOCATION_API_KEY
holiday_api_key = settings.HOLIDAY_API_KEY

logger = get_task_logger(__name__)


"""
Save holiday information on basis of user system IP address from which they sign up
"""


@task(name="save_holiday_info_task")
def save_holiday_info_task(user_id):

    logger.info("Saving Holiday Info...")
    user = get_object_or_404(User, pk=user_id)

    # Get country using IP address of user trying to sign up
    payload = {"api_key": ipgeolocation_api_key}
    ipgeolocation_response = requests.get(
        "https://ipgeolocation.abstractapi.com/v1/", params=payload
    )
    data = ipgeolocation_response.content
    ipgeolocation_response_dict = json.loads(data.decode("UTF-8"))
    country_code = ipgeolocation_response_dict.get("country_code")

    if country_code:
        current_date = date.today()

        # Get holiday for country of user trying to sign up from
        holiday_api_payload = {
            "api_key": holiday_api_key,
            "country": country_code,
            "year": current_date.year,
            "month": current_date.month,
            "day": current_date.day,
        }
        holiday_api_response = requests.get(
            "https://holidays.abstractapi.com/v1/", params=holiday_api_payload
        )
        holiday_response_list = json.loads(holiday_api_response.content.decode("UTF-8"))
        for data_dict in holiday_response_list:
            holiday = Holiday(user=user, **data_dict)
            holiday.save()

    return True
