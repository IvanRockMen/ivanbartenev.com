import functools
import datetime
import inspect
import traceback
import json

from django.db import transaction
from django.http import JsonResponse
from django.views import View

JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}

def ret(json_object, status=200):
    """Отдаёт JSON с правильными HTTP заголовками и в читаемом
    в браузере виде в случае с кирилицей"""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params= JSON_DUMPS_PARAMS
    )

def error_response(exception):
    """Форматирует HTTP ответ с описанием ошибки и Traceback'ом"""
    res = {"errorMessage": str(exception),
    "traceback": traceback.format_exc()}
    return ret(res, status=400)

def base_view(fn):
    """Декоратор для всех вьюшек, обрабатывает исключения"""
    @functools.wraps(fn)
    def inner(requst, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(requst, *args, **kwargs)
        except Exception as e:
            return error_response(e)

    return inner
