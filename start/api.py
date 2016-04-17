from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Permission, User
import json
from django.utils import timezone
def getAllResponse(request):
    responses = Response.objects.all()
