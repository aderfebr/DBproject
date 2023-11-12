from django.shortcuts import render
from .models import Items,Orders
from django.db.models import Avg,Max,Min,Sum,Count
from django.http import JsonResponse,HttpResponse

def dis(arr):
    ans=0
    for i in arr:
        ans+=i**2
    return ans**0.5

def home(request):
    return render(request, "index.html")

def items(request):
    id=request.GET.get('id')
    if id is None:
        res=Items.objects.all().values()
    else:
        res=Items.objects.filter(item_id=id).all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def orders(request):
    res=Orders.objects.all().values()
    res=list(res)
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def knn(request):
    res=[]
    id=request.GET.get('id')
    father=Items.objects.filter(item_id=id).all().values()[0]
    price=Items.objects.aggregate(Max("price"),Min("price"))
    score=Items.objects.aggregate(Max("score"),Min("score"))
    for i in Items.objects.all().values():
        if i["item_id"]==father["item_id"]:
            continue
        type=0 if i["type"]==father["type"] else 0.3
        ans=dis([abs(i["price"]-father["price"])/(price["price__max"]-price["price__min"]),abs(i["score"]-father["score"])/(score["score__max"]-score["score__min"]),type])
        res.append([i["item_id"],i["item_name"],ans])
    res=sorted(res,key=lambda x:x[2])
    res=list(res[:5])
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)

def apriori(request):
    tmp={}
    res=[]
    id=request.GET.get('id')
    num=Orders.objects.all().values("user_id").distinct().count()
    pb=Orders.objects.filter(item_id=id).all().values("user_id").distinct().count()/num
    father=Orders.objects.filter(item_id=id).all().values()
    for i in father:
        son=Orders.objects.filter(user_id=i["user_id"]).all().values()
        for j in son:
            if j["item_id"]==int(id):
                continue
            if j["item_id"] in tmp:
                tmp[j["item_id"]]+=1
            else:
                tmp[j["item_id"]]=1
    for i in tmp:
        res.append([i,Items.objects.filter(item_id=i).all().values()[0]["item_name"],tmp[i]/num/pb])
    res=sorted(res,key=lambda x:-x[2])
    res=list(res[:5])
    return JsonResponse(res, json_dumps_params={"ensure_ascii": False},safe=False)