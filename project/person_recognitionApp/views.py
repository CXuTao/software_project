from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import User
import json

# Create your views here.
def index(request):
    return render(request, 'person_recognitionApp/index.html')

#登录验证
def loginCheck(request):
    # response = HttpResponse(json.dumps({'code':2000, 'data':{'token':"123", 'admin':'admin'}}))
    # response['Access - Control - Allow - Origin'] = " * "
    # response["Access - Control - Allow - Methods"] = "POST, GET, OPTIONS"
    # response["Access - Control - Max - Age"] = "1000"
    # response["Access - Control - Allow - Headers"] = " * "
    # return render(request, 'person_recognitionApp/index.html', {'code':2000, 'data':{'token':"123", 'admin':'admin'}})
    # return response
    return JsonResponse({'code':2000, 'data':{'token':"123", 'admin':'admin'}})