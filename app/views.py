from django.shortcuts import render
from .models import 物料表,调配构成表,库存表,MPS,BS,Query_BS
import datetime
import math
import pandas as pd
from django.http import JsonResponse,HttpResponse

class node():
    def __init__(self,name,date_start,date_end):
        self.id=None
        self.name=name
        self.date_start=date_start
        self.date_end=date_end
        self.num=None
        self.method=None
        self.tree=None
        self.father=None

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

def cal_mps(father,ans):
    tree=1
    tmp=调配构成表.objects.filter(父物料名称=father.name).values()
    for i in tmp:
        delta=i["配料提前期"]+i["供应商提前期"]+物料表.objects.filter(物料号=i["子物料号_id"]).values()[0]["作业提前期"]
        son=node(i["子物料名称"],father.date_start-datetime.timedelta(days=delta),father.date_start)
        son.father=father
        tree+=cal_mps(son,ans)
    father.id=物料表.objects.filter(名称=father.name).values()[0]["物料号"]
    father.method=物料表.objects.filter(名称=father.name).values()[0]["调配方式"]
    father.tree=tree
    ans.append(father)
    return tree

def answer_mps(request):
    ans=[]
    mps=MPS.objects.all().values()
    for i in mps:
        delta=物料表.objects.filter(名称=i["产品名称"]).values()[0]["作业提前期"]
        root=node(i["产品名称"],i["完工日期"]-datetime.timedelta(days=delta),i["完工日期"])
        root.num=i["数量"]
        cal_mps(root,ans)

    ans=sorted(ans,key=lambda x:(-x.tree,x.date_start))

    for i in ans:
        if i.num is None:
            for j in ans:
                if i.father==j:
                    i.num=math.ceil(j.num*调配构成表.objects.filter(子物料名称=i.name,父物料名称=j.name).values()[0]["构成数"]/(1-物料表.objects.filter(名称=i.name).values()[0]["损耗率"]))
                    break
        stock1=库存表.objects.filter(物料名称=i.name).values()[0]["工序库存"]
        stock2=库存表.objects.filter(物料名称=i.name).values()[0]["资材库存"]
        if stock1>0:
            stock_num=min(i.num,stock1)
            i.num-=stock_num
            库存表.objects.filter(物料名称=i.name).update(工序库存=stock1-stock_num)
        if stock2>0:
            stock_num=min(i.num,stock2)
            i.num-=stock_num
            库存表.objects.filter(物料名称=i.name).update(资材库存=stock2-stock_num)

    res=[]
    for i in ans:
        if i.num!=0:
            res.append({"id":i.id,"name":i.name,"date_start":i.date_start,"date_end":i.date_end,"method":i.method,"num":i.num})
    df=pd.DataFrame(res)
    grouped=df.groupby(["id","name","date_start","date_end","method"]).sum().reset_index()
    res=grouped.to_dict(orient="records")
    res=sorted(res,key=lambda x:(x["id"],x["date_start"]))

    return JsonResponse(res,json_dumps_params={"ensure_ascii": False},safe=False)

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