from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def employeeView(request):
    emp = {
        'id': 1,
        'name': 'Vinay'
    }

    return JsonResponse(emp)