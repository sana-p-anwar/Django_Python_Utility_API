from django.shortcuts import render
from django.http import JsonResponse 
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class FactorialView(View):

    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)

        n = form_data.get('num')

        fact = 1
        for i in range(1, n + 1):
            fact = fact * i

        print(request_body)

        data = {
            "Number": n,
            "Factorial": fact
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class ArmstrongView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        num = form_data.get('num')

        original = num
        sum = 0

        while num > 0:
            digit = num % 10
            sum = sum + (digit ** 3)
            num = num // 10

        if sum == original:
            result = "Armstrong Number"
        else:
            result = "Not an Armstrong Number"

        data = {
            "Number": original,
            "Result": result
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class ProductProfitView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        cost_price = form_data.get("cost_price")
        selling_price = form_data.get("selling_price")
        quantity = form_data.get("quantity")

        total_cost = cost_price * quantity
        total_sales = selling_price * quantity
        profit = total_sales - total_cost

        data = {
            "cost_price": cost_price,
            "selling_price": selling_price,
            "quantity": quantity,
            "total_cost": total_cost,
            "total_sales": total_sales,
            "profit": profit
        }

        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class WorkSalaryView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        hours_worked = form_data.get("hours_worked")
        regular_hours = form_data.get("regular_hours")
        hourly_rate = form_data.get("hourly_rate")
        overtime_rate = form_data.get("overtime_rate")

        overtime_hours = hours_worked - regular_hours

        regular_salary = regular_hours * hourly_rate
        overtime_salary = overtime_hours * overtime_rate

        total_salary = regular_salary + overtime_salary

        data = {
            "hours_worked": hours_worked,
            "regular_hours": regular_hours,
            "hourly_rate": hourly_rate,
            "overtime_rate": overtime_rate,
            "overtime_hours": overtime_hours,
            "regular_salary": regular_salary,
            "overtime_salary": overtime_salary,
            "total_salary": total_salary
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class AgeDetailsView(View):

    def post(self, request):

        request_body = request.body
        form_data = loads(request_body)

        age = form_data.get("age")

        months = age * 12
        weeks = age * 52
        days = age * 365

        data = {
            "age": age,
            "months": months,
            "weeks": weeks,
            "days": days
        }

        return JsonResponse(data)

