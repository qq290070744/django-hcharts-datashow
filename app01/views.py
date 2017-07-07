from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
import time, json, pymysql, collections, os, pymongo
from app01.models import *
from django.http import JsonResponse




def acc_login(request):
    if request.method == "POST":
        print(request.POST)
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect('/')
        else:
            error = "error"
            return render(request, "login.html", {"login_error": error})
    print("用户正在访问登陆页")
    return render(request, "login.html")


@login_required
def acc_logout(requrst):
    logout(requrst)
    return redirect("/")


@login_required
def index(request):
    print("用户正在访问主页")
    return render(request, 'index.html')


def ret_dic(filename):
    # 获取json数据并返回
    data = ''
    with open(os.path.join('static/json', filename), encoding='utf-8') as f:
        for i in f:
            data += i
    data = json.loads(data)
    return data


@login_required
def pvuv(request):
    # Day,访问量（PV）,访问用户（UV）
    data = 'Day,访问量（PV）,访问用户（UV）\n'
    with open("static/json/pvuv") as f:
        for i in f:
            data+=i
    # dat = 访问量.objects.all()
    # for i in dat:
    #     data += '{},{},{}\n'.format(i.Day, i.PV, i.UV)
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    # return JsonResponse(data, safe=False)
    return render(request, 'pvuv.html')


@login_required
def 可缩放的时间轴(request):
    # 在json文件里面的数据 1370131200000去掉3个0就是时间戳
    data = ret_dic('可缩放的时间轴.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '可缩放的时间轴.html')


@login_required
def 百分比堆叠面积图(request):
    data = ret_dic('堆叠面积图.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '百分比堆叠面积图.html')


@login_required
def 误差线图(request):
    data = ret_dic('误差线图.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '误差线图.html')


@login_required
def 颜色渐变的饼图(request):
    data = [
        ['Firefox', 45.0],
        ['IE', 26.8],
        ['Chrome', 12.8],
        ['Safari', 8.5],
        ['Opera', 6.2],
        ['其他', 0.7]
    ]

    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '颜色渐变的饼图.html')


@login_required
def 带辅助线的气泡图(request):
    data = ret_dic('带辅助线的气泡图.json')

    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '带辅助线的气泡图.html')


@login_required
def 多个图表共用一个提示框(request):
    data = ret_dic('多个图表共用一个提示框.json')

    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '多个图表共用一个提示框.html')


@login_required
def 混合图堆叠图(request):
    data = ret_dic('混合图堆叠图.json')

    b = zip(*data["column"])
    c = list(round(sum(i) / len(i), 2) for i in b)
    # print(c)
    data['spline'] = c
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '混合图+堆叠图.html')


@login_required
def 气泡图(requrst):
    data = ret_dic('气泡图.json')
    if requrst.is_ajax():
        return JsonResponse(data, safe=False)
    return render(requrst, '气泡图.html')


@login_required
def 散点图(request):
    data = ret_dic('散点图.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '散点图.html')
