from django.http import JsonResponse
from django.shortcuts import render

def calculate_emi(principal, rate, time):
    rate = rate / (12 * 100)  # monthly interest rate
    time = time * 12  # number of monthly installments
    emi = (principal * rate * ((1 + rate) ** time)) / (((1 + rate) ** time) - 1)
    return round(emi, 2)

def index(request):
    return render(request, 'calculator/index.html')

def emi_calculator(request):
    if request.method == 'GET':
        principal = float(request.GET.get('principal', 0))
        rate = float(request.GET.get('rate', 0))
        time = int(request.GET.get('time', 0))
        emi = calculate_emi(principal, rate, time)
        return JsonResponse({'emi': emi})
