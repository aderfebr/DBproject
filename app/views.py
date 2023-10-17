from django.shortcuts import render
from .models import 物料表,调配构成表,库存表,MPS,BS,Query_BS
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

def wuliao(request):
    res=物料表.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def kucun(request):
    res=库存表.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def tiaopei(request):
    res=调配构成表.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def mps(request):
    res=MPS.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def add_mps(request):
    name=request.POST.get('name')
    num=request.POST.get('num')
    date=request.POST.get('date')
    mps=MPS(产品名称=name,数量=num,完工日期=date)
    mps.save()
    return HttpResponse("添加成功")

def clear_mps(request):
    MPS.objects.all().delete()
    return HttpResponse("清空成功")

def cal_mps(name,num,date):
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
    return ans

def answer_mps(request):
    ans=[]
    res=MPS.objects.all().values()
    for i in res:
        for j in cal_mps(i["产品名称"],i["数量"],i["完工日期"]):
            ans.append(j)
    ans=sorted(ans,key=lambda x:x["date_start"])

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

    ans=sorted(ans,key=lambda x:x["id"])
    return JsonResponse(ans,json_dumps_params={"ensure_ascii": False},safe=False)

def bs(request):
    res=BS.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def query_bs(request):
    res=Query_BS.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def add_bs(request):
    name=request.POST.get('name')
    mps=Query_BS(变量名=name)
    mps.save()
    return HttpResponse("添加成功")

def clear_bs(request):
    Query_BS.objects.all().delete()
    return HttpResponse("清空成功")

def answer_bs(request):
    ans=[]
    res=Query_BS.objects.all().values()
    for i in res:
        tmp=""
        id=BS.objects.filter(变量名=i["变量名"]).values()[0]["id"]
        for j in BS.objects.filter(资产类汇总序号=id).values():
            tmp+=j["变量名"]+"+"
        tmp=tmp[:-1]
        ans.append({"id":i["变量名"],"ans":tmp})
    return JsonResponse(ans, json_dumps_params={"ensure_ascii": False},safe=False)