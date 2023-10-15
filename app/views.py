from django.shortcuts import render
from .models import 物料表,调配构成表,库存表
import json
import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse

def home(request):
    return render(request, "index.html")

def print(request):
    res=调配构成表.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def answer(request):
    pass