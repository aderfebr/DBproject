from django.shortcuts import render,HttpResponse
from .models import staff,security_personnel,maintain_personnel,scenic_plot
import random
#测试数据
def delete_data(request):
    staff.objects.all().delete()
    scenic_plot.objects.all().delete()
    return HttpResponse("success")


def insert_test_sc(request):
    sc_plot=scenic_plot(plot_id=1,plot_name="景点",plot_address="上海市")
    sc_plot.save()
    insert_test()
    staff_job()
    return HttpResponse("success")
def randomstr(num):
    list1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str=""
    for i in range(num):
        str=str+random.choice(list1)
    return str

def insert_test():
    for i in range(10):
        scenic_plots=scenic_plot.objects.filter(plot_id=1).get()
        staffs=staff(staff_id=i,join_id="2023-5-9",
                    name=randomstr(5),username=randomstr(8),
                    password=randomstr(6))
        staffs.scenic_plot=scenic_plots
        staffs.save()
def staff_job():
    sec=staff.objects.filter(staff_id__lt=5)
    for data in sec:
        secp=security_personnel(staff_id=data,grade=random.randint(1,10))
        secp.save()


    

# Create your views here.
