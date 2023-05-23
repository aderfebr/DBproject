from django.shortcuts import render
from .models import staff,security_personnel,maintain_personnel,scenic_plot,area
from random import random,randint,choice
import json
import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse
firstname='''李，王，张，刘，陈，杨，黄，赵，周，吴，徐，孙，朱，马，胡，郭，林，何，高，梁，郑，罗，宋，谢，唐，韩，曹，许，邓，萧，冯，曾，程，蔡，彭，潘，袁，於，董，余，苏，叶，吕，魏，蒋，田，杜，丁，沈，姜，范，江，傅，钟，卢，汪，戴，崔，任，陆，廖，姚，方，金，邱，夏，谭，韦，贾，邹，石，熊，孟，秦，阎，薛，侯，雷，白，龙，段，郝，孔，邵，史，毛，常，万，顾，赖，武，康，贺，严，尹，钱，施，牛，洪，龚'''

Blastname='''豪、言、玉、意、泽、彦、轩、景、正、程、诚、宇、澄、安、青、泽、轩、旭、恒、思、宇、嘉、宏、皓、成、宇、轩、玮、桦、宇、达、韵、磊、泽、博、昌、信、彤、逸、柏、新、劲、鸿、文、恩、远、翰、圣、哲、家、林、景、行、律、本、乐、康、昊、宇、麦、冬、景、武、茂、才、军、林、茂、飞、昊、明、明、天、伦、峰、志、辰、亦'''

Glastname='''佳、彤、自、怡、颖、宸、雅、微、羽、馨、思、纾、欣、元、凡、晴、玥、宁、佳、蕾、桑、妍、萱、宛、欣、灵、烟、文、柏、艺、以、如、雪、璐、言、婷、青、安、昕、淑、雅、颖、云、艺、忻、梓、江、丽、梦、雪、沁、思、羽、羽、雅、访、烟、萱、忆、慧、娅、茹、嘉、幻、辰、妍、雨、蕊、欣、芸、亦'''

username="ajklsdjkckskhncdkbcsidbvniskhdfjkbdjvndksppdka"
password="CHUJABFJAIOQPUYVNNfhihskdkvndkhapmcxjoziahsif5654613267512138"
from random import random,randint

firstname='''李，王，张，刘，陈，杨，黄，赵，周，吴，徐，孙，朱，马，胡，郭，林，何，高，梁，郑，罗，宋，谢，唐，韩，曹，许，邓，萧，冯，曾，程，蔡，彭，潘，袁，於，董，余，苏，叶，吕，魏，蒋，田，杜，丁，沈，姜，范，江，傅，钟，卢，汪，戴，崔，任，陆，廖，姚，方，金，邱，夏，谭，韦，贾，邹，石，熊，孟，秦，阎，薛，侯，雷，白，龙，段，郝，孔，邵，史，毛，常，万，顾，赖，武，康，贺，严，尹，钱，施，牛，洪，龚'''

Blastname='''豪、言、玉、意、泽、彦、轩、景、正、程、诚、宇、澄、安、青、泽、轩、旭、恒、思、宇、嘉、宏、皓、成、宇、轩、玮、桦、宇、达、韵、磊、泽、博、昌、信、彤、逸、柏、新、劲、鸿、文、恩、远、翰、圣、哲、家、林、景、行、律、本、乐、康、昊、宇、麦、冬、景、武、茂、才、军、林、茂、飞、昊、明、明、天、伦、峰、志、辰、亦'''

Glastname='''佳、彤、自、怡、颖、宸、雅、微、羽、馨、思、纾、欣、元、凡、晴、玥、宁、佳、蕾、桑、妍、萱、宛、欣、灵、烟、文、柏、艺、以、如、雪、璐、言、婷、青、安、昕、淑、雅、颖、云、艺、忻、梓、江、丽、梦、雪、沁、思、羽、羽、雅、访、烟、萱、忆、慧、娅、茹、嘉、幻、辰、妍、雨、蕊、欣、芸、亦'''


def randomname():
    firstname1=firstname.split("，")
    Cfirstname=firstname1[int(random()*len(firstname1))]
    Blastname1=Blastname.split("、")
    Glastname1=Glastname.split("、")
    CBlastname=Blastname1[int(random()*len(Blastname1))]
    CBlastname1=Blastname1[int(random()*len(Blastname1))]
    CGlastname=Glastname1[int(random()*len(Glastname1))]
    CGlastname1=Glastname1[int(random()*len(Glastname1))]
    lan=[2,3]
    Clan=lan[int(random()*len(lan))]
    Sex=[0,1]
    CSex=Sex[int(random()*len(Sex))]
    if (CSex==0):
        if (Clan==2):return Cfirstname+CBlastname
        if (Clan==3):return Cfirstname+CBlastname+CBlastname1
    else:
        if (Clan==2):return Cfirstname+CGlastname
        if (Clan==3):return Cfirstname+CGlastname+CGlastname1 

def randomusername():
    str=''
    for i in range(6):
        str=str+choice(username)
    return str
def randompass():
    str=''
    for i in range(12):
        str=str+choice(password)
    return str
#测试数据
def delete_data(request):
    staff.objects.all().delete()
    scenic_plot.objects.all().delete()
    return HttpResponse("success")

def insert_test_sc(request):
    sc_plot=scenic_plot(plot_id=1,plot_name="景点",plot_address="上海市")
    sc_plot.save()
    insert_test()
    secstaff()
    mainstaff()
    insertarea()
    return HttpResponse("success")

def insert_test():
    for i in range(30):
        staff_insert=staff(staff_id=i+10000,join_id=datetime.datetime.now(),name=randomname(),username=randomusername()
                           ,password=randompass())
        staff_insert.scenic_plot=scenic_plot.objects.get(plot_id=1)
        staff_insert.save()
def secstaff():
    for i in range(15):
        sec= security_personnel(staff_id=staff.objects.get(staff_id=i+10000),grade=i)
        sec.save()

def mainstaff():
    for i in range(15):
        sec= maintain_personnel(staff_id=staff.objects.get(staff_id=i+10015),professional_field="无")
        sec.save()
def insertarea():
    for i in range(5):
        sec=area(area_id=i,area_device="摄像头",area_name="未命名",plot_id=scenic_plot.objects.get(plot_id=1))
        sec.save()


def query(request):
    res=staff.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def home(request):
    return render(request, "index.html")
