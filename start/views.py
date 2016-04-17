from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Permission, User
import json
from django.utils import timezone
import datetime
from models import *
# Create your views here.
@login_required(login_url='/admin/')
def index(request):
    if request.method=="POST":
        return JsonResponse(request.POST)
    user = request.user
    trackAccesses = TrackAccess.objects.all()
    tracks = []
    for trackAccess in trackAccesses:
        if user in trackAccess.Users.all():
            tracks.append(trackAccess.PrimaryTrack)
    return render(request,"index.html",{"tracks":tracks,"user":user})

@csrf_exempt
def response(request):
    if request.method=="POST":
        data = request.POST
        try:
            artist = data["artist"]
            song = data["song"]
            trackid = data["trackid"]
            userid = data["userid"]
        except:
            return HttpResponse(json.dumps(data) ,status=401)
        if artist=="" or song=="":
            return HttpResponse("Invalid Request" ,status=402)
        resonse = Response.objects.create(Track=Track.objects.get(id=trackid),User=User.objects.get(id=userid),inputArtist=artist,inputSong=song,createdDate=timezone.now())
        return HttpResponse("success")
    else:
        return HttpResponse("Invalid Request" ,status=403)
def bye(request):
    return HttpResponse("bye")
