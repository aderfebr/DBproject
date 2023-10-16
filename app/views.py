from django.shortcuts import render
from .models import 物料表,调配构成表,库存表
import json
import math
import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse

class node():
    def __init__(self,id,name,num,date,delta,method):
        self.id=id
        self.name=name
        self.num=num
        self.date_start=date-datetime.timedelta(days=delta)
        self.date_end=date
        self.method=method

def home(request):
    return render(request, "index.html")

def print(request):
    res=调配构成表.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def answer(request):
    name="眼镜"
    num=100
    date_y=2022
    date_m=5
    date_d=30
    date=datetime.date(date_y,date_m,date_d)
    delta=物料表.objects.filter(名称=name).values()[0]["作业提前期"]
    method=物料表.objects.filter(名称=name).values()[0]["调配方式"]

    queue=[]
    ans=[]

    root=node(物料表.objects.filter(名称=name).values()[0]["物料号"],name,num,date,delta,method)
    queue.append(root)
    
    while len(queue)!=0:
        father=queue.pop()
        ans.append({"id":father.id,"name":father.name,"num":father.num,"date_start":father.date_start,"date_end":father.date_end,"method":father.method})
        tmp=调配构成表.objects.filter(父物料号=father.id).values()
        for i in tmp:
            son=i["子物料号_id"]
            name=i["子物料名称"]
            num=math.ceil(father.num*i["构成数"]/(1-物料表.objects.filter(物料号=son).values()[0]["损耗率"]))
            date=father.date_start
            delta=i["配料提前期"]+i["供应商提前期"]+物料表.objects.filter(物料号=son).values()[0]["作业提前期"]
            method=物料表.objects.filter(物料号=son).values()[0]["调配方式"]
            queue.append(node(son,name,num,date,delta,method))
    
    ans=sorted(ans,key=lambda x:x["date_start"])
    res=[]

    for i in ans:
        stock1=库存表.objects.filter(物料号=i["id"]).values()[0]["工序库存"]
        stock2=库存表.objects.filter(物料号=i["id"]).values()[0]["资材库存"]
        if stock1>0:
            stock_num=min(i["num"],stock1)
            i["num"]-=stock_num
            库存表.objects.filter(物料号=i["id"]).update(工序库存=stock1-stock_num)
        if stock2>0:
            stock_num=min(i["num"],stock2)
            i["num"]-=stock_num
            库存表.objects.filter(物料号=i["id"]).update(资材库存=stock2-stock_num)

    return JsonResponse(ans,json_dumps_params={"ensure_ascii": False},safe=False)