from django.shortcuts import render
from .models import staff,security_personnel,maintain_personnel,scenic_plot,area,device,security_view,maintain_view,warning,security_report,maintain_report
from random import random,randint,choice
import json
import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse

#############################################################################################################
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
    insert_test()
    secstaff()
    mainstaff()
    return HttpResponse("success")

def insert_test():
    for i in range(15):
        staff_insert=staff(staff_id=str(i+10000),join_id=datetime.datetime.now(),name=randomname(),username=randomusername()
                                ,password=randompass)
        staff_insert.staff_id=staff_insert.staff_id
        staff_insert.scenic_plot=scenic_plot.objects.get(plot_id=1)
        staff_insert.save()
    for i in range(15):
        staff_insert=staff(staff_id=str(i+20000),join_id=datetime.datetime.now(),name=randomname(),username=randomusername()
                                ,password=randompass())
        staff_insert.staff_id=staff_insert.staff_id
        staff_insert.scenic_plot=scenic_plot.objects.get(plot_id=1)
        staff_insert.save()

       
def secstaff():
    for i in range(15):
        sec= security_personnel(staff_id=staff.objects.get(staff_id=str(i+10000)),grade=i)
        sec.save()

def mainstaff():
    for i in range(15):
        sec= maintain_personnel(staff_id=staff.objects.get(staff_id=str(i+20000)),professional_field="无")
        sec.save()




###########################################👆人员表测试数据👆#########################################################



######################人员表增删改查############################
def staff_query(request):
    res=staff.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)


def staff_foreignkey(request):
    res=scenic_plot.objects.all().values('plot_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['plot_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)


def add_staff_main(request):   #insert
    staff_id=request.POST.get('staff_id')
    join_time=request.POST.get('join_id')
    name=request.POST.get('name')
    username=request.POST.get('username')
    password=request.POST.get('password')
    plot_id=request.POST.get('scenic_plot_id')

    staff_add=staff(staff_id=staff_id,join_id=join_time,name=name,username=username,password=password)
    staff_add.scenic_plot=scenic_plot.objects.get(plot_id=plot_id)
    
    staff_add.save()
    return JsonResponse('添加成功',json_dumps_params={"ensure_ascii": False},safe=False)

def update_staff_main(request):   #update
    staff_id=request.POST.get('staff_id')
    
    join_time=request.POST.get('join_id')
    name=request.POST.get('name')
    username=request.POST.get('username')
    password=request.POST.get('password')
    plot_id=request.POST.get('scenic_plot_id')


    staff.objects.filter(staff_id=staff_id).update(join_id=join_time,name=name,username=username,password=password,scenic_plot=plot_id)
    return JsonResponse('修改成功',json_dumps_params={"ensure_ascii": False},safe=False)


def delete_staff_main(request):   #insert
    staff_id=request.POST.get('staff_id')
    staff.objects.filter(staff_id=staff_id).delete()
    return JsonResponse('删除成功',json_dumps_params={"ensure_ascii": False},safe=False)


######################区域表增删改查############################

def area_query(request):
    res=area.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def area_foreignkey(request):
    res=scenic_plot.objects.all().values('plot_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['plot_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)

def add_area_main(request):   #insert
    area_id=request.POST.get('area_id')
    area_device=request.POST.get('area_device')
    area_name=request.POST.get('area_name')
    plot_id=request.POST.get('plot_id_id')
    area_add=area(area_id=area_id,area_device=area_device,area_name=area_name)
    area_add.plot_id=scenic_plot.objects.get(plot_id=plot_id)
    area_add.save()
    return JsonResponse('添加成功',json_dumps_params={"ensure_ascii": False},safe=False)

def update_area_main(request):   #update
    area_id=request.POST.get('area_id')
    area_device=request.POST.get('area_device')
    area_name=request.POST.get('area_name')
    plot_id=request.POST.get('plot_id_id')
    area.objects.filter(area_id=area_id).update(area_device=area_device,area_name=area_name,plot_id=plot_id)
    return JsonResponse('修改成功',json_dumps_params={"ensure_ascii": False},safe=False)


def delete_area_main(request):   #insert
    area_id=request.POST.get('area_id')
    area.objects.filter(area_id=area_id).delete()
    return JsonResponse('删除成功',json_dumps_params={"ensure_ascii": False},safe=False)


######################设备表增删改查############################



def device_query(request):
    res=device.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def device_foreignkey(request):
    res=area.objects.all().values('area_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['area_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)

def add_device_main(request):   #insert
    device_id=request.POST.get('device_id')
    device_name=request.POST.get('device_name')
    manufacturer=request.POST.get('manufacturer')
    production_date=request.POST.get('production_date')
    func=request.POST.get('func')
    area_id=request.POST.get('area_id')
    device_add=device(device_id=device_id,device_name=device_name,manufacturer=manufacturer,production_date=production_date,func=func)
    device_add.area_id=area.objects.get(area_id=area_id)
    device_add.save()
    return JsonResponse('添加成功',json_dumps_params={"ensure_ascii": False},safe=False)

def update_device_main(request):   #update
    device_id=request.POST.get('device_id')
    device_name=request.POST.get('device_name')
    manufacturer=request.POST.get('manufacturer')
    production_date=request.POST.get('production_date')
    func=request.POST.get('func')
    area_id=request.POST.get('area_id')
    device.objects.filter(device_id=device_id).update(device_name=device_name,manufacturer=manufacturer,production_date=production_date,func=func,area_id=area_id)
    return JsonResponse('修改成功',json_dumps_params={"ensure_ascii": False},safe=False)


def delete_device_main(request):   #insert
    device_id=request.POST.get('device_id')
    device.objects.filter(device_id=device_id).delete()
    return JsonResponse('删除成功',json_dumps_params={"ensure_ascii": False},safe=False)




def security_view_query(request):
    res=security_view.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def maintain_view_query(request):
    res=maintain_view.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)



#######################警报处理######################
def warn_query(request):
    res=warning.objects.filter(info='未处理').all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def deal_warning(request):
    id=request.POST.get('id')
    warning.objects.filter(id=id).update(info='已处理')
    return JsonResponse('删除成功',json_dumps_params={"ensure_ascii": False},safe=False)

#######################安保单#########################

def report_query(request):
    staff_id=request.GET.get('staff_id_id')
    res=security_report.objects.filter(staff_id=staff_id).all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)


def report_foreignkey_area(request):
    res=area.objects.all().values('area_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['area_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)

def report_foreignkey_staff(request):
    res=security_view.objects.all().values('staff_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['staff_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)

def add_report(request):
    sreport_date=request.POST.get('sreport_date')
    sreport=request.POST.get('sreport')
    area_id_id=request.POST.get('area_id_id')
    staff_id_id=request.POST.get('staff_id_id')
    sradd=security_report(sreport_date=sreport_date,sreport=sreport,area_id_id=area_id_id,staff_id_id=staff_id_id)
    sradd.save()
    return JsonResponse('添加成功',json_dumps_params={"ensure_ascii": False},safe=False)

def update_report(request):
    sreport_id=request.POST.get('sreport_id')
    sreport_date=request.POST.get('sreport_date')
    sreport=request.POST.get('sreport')
    area_id_id=request.POST.get('area_id_id')
    staff_id_id=request.POST.get('staff_id_id')
    security_report.objects.filter(sreport_id=sreport_id).update(sreport_date=sreport_date,sreport=sreport,area_id_id=area_id_id,staff_id_id=staff_id_id)

    return JsonResponse('修改成功',json_dumps_params={"ensure_ascii": False},safe=False)


def delete_report(request):   
    sreport_id=request.POST.get('sreport_id')
    security_report.objects.filter(sreport_id=sreport_id).delete()
    return JsonResponse('删除成功',json_dumps_params={"ensure_ascii": False},safe=False)

#######################维护单#########################
#mreport_id,mreport_date,mreport,device_id_id,staff_id_id

def mreport_query(request):
    staff_id=request.GET.get('staff_id_id')
    res=maintain_report.objects.filter(staff_id=staff_id).all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)


def mreport_foreignkey_device(request):
    res=device.objects.all().values('device_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['device_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)

def mreport_foreignkey_staff(request):
    res=maintain_view.objects.all().values('staff_id')
    res=list(res)
    res_id=[]
    for data in res:
        res_id.append(data['staff_id'])
    return JsonResponse(res_id, json_dumps_params={"ensure_ascii": False},safe=False)

def madd_report(request):
    mreport_date=request.POST.get('mreport_date')
    mreport=request.POST.get('mreport')
    device_id_id=request.POST.get('device_id_id')
    staff_id_id=request.POST.get('staff_id_id')
    mradd=maintain_report(mreport_date=mreport_date,mreport=mreport,device_id_id=device_id_id,staff_id_id=staff_id_id)
    mradd.save()
    return JsonResponse('添加成功',json_dumps_params={"ensure_ascii": False},safe=False)

def mupdate_report(request):
    mreport_id=request.POST.get('mreport_id')
    mreport_date=request.POST.get('mreport_date')
    mreport=request.POST.get('mreport')
    device_id_id=request.POST.get('device_id_id')
    staff_id_id=request.POST.get('staff_id_id')
    maintain_report.objects.filter(mreport_id=mreport_id).update(mreport_date=mreport_date,mreport=mreport,device_id_id=device_id_id,staff_id_id=staff_id_id)

    return JsonResponse('修改成功',json_dumps_params={"ensure_ascii": False},safe=False)


def mdelete_report(request):   
    mreport_id=request.POST.get('mreport_id')
    maintain_report.objects.filter(mreport_id=mreport_id).delete()
    return JsonResponse('删除成功',json_dumps_params={"ensure_ascii": False},safe=False)









def home(request):
    return render(request, "index.html")
