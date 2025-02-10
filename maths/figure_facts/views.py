from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from math import sqrt
from .utils import get_fun_fact, get_properties, digit_sum

@api_view(["GET"])
def classify_number(request):
    number = request.GET.get("number")
    try:
        number = int(number)
    except (TypeError, ValueError):
       return JsonResponse({"number": "alphabet", "error": True }, status=400)
    return JsonResponse(
            {"number": number,
             "is_prime": False if number < 2 else all(number % i !=0 for i in range(2, int(sqrt(number)) + 1)),
             "is_perfect": number >1 and sum(i for i in range(1, number) if number % i == 0)==number,
             "properties": [get_properties(number)],
             "digit_sum": digit_sum(number),
             "fun_fact": get_fun_fact(number)})