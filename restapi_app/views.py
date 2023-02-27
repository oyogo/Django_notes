from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import subprocess
from django.http import HttpResponse
from dotenv import load_dotenv
import os 

load_dotenv()


# Create your views here.
@api_view(['POST'])
def Greetings(request):
    process = subprocess.run([os.getenv("SCRIPT_LOC")])
    if process.returncode == 0:
        print(process.returncode)
        return HttpResponse("success")
    else:
        return HttpResponse("fail")
        
    
    