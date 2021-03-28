from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

#
@login_required
def home(request):
    return render(request, 'calculations/home_new.html')
@login_required
def calc(request):
    return render(request, 'calculations/home.html')
@login_required
def series(request):
    return render(request, 'calculations/series.html')
@login_required
def solve(request):
    return render(request, 'calculations/solve.html')
@login_required
def calc_for(request):
    return render(request, 'calculations/calc_for.html')

def calculate(request):
    x = int(request.GET['x'])
    n = int(request.GET['n'])
    if x == 0:
        result = "infinite"
    else:
        result = power(x, n)
    context = { 'result' : result }
    return render(request,'calculations/result.html', context)

def power(x,n):
    if n == 0:
        return 0
    elif n == 1:
        return 1/x
    else:
        return 1/(x**n)+power(x,n-1)


def loop(request):
    x = int(request.GET['x'])
    n = int(request.GET['n'])
    if n == 0:
        result = 0
    elif n == 1:
        result = 1/x
    else:
        result = 0
        for i in range(2,n+1):
            result += 1/(x**i)
    context = { 'result' : result }
    return render(request,'calculations/result.html', context)




def nextvalue(request):
    n = int(request.GET['n'])
    if n%2==0:
        result = (n**2)-1
    else:
        result = (n**2)+1
    context = { 'result' : result }
    return render(request,'calculations/result.html', context)



def solution(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    if y==0:
        result = "infinite"
    else:
        result = (x/y)**(a+b)
    context = { 'result' : result }
    return render(request,'calculations/result.html', context)

@api_view(["POST"])
def calculate_api(request):
    try:

        data = request.data
        x = int(data['x'])
        n = int(data['n'])
        if x == 0:
            result = "infinite"
        else:
            result = power(x, n)
        return JsonResponse('result : {} '.format(result), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)