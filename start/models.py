from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import Permission, User
# Create your models here.
class Track(models.Model):
    Artist = models.CharField(max_length=200)
    Track = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.Track+" by "+self.Artist

class TrackAccess(models.Model):
    PrimaryTrack = models.OneToOneField(Track)
    Users = models.ManyToManyField(User)
class Response(models.Model):
    Track = models.ForeignKey(Track)
    User = models.ForeignKey(User)
    createdDate = models.DateTimeField()
    inputArtist = models.CharField(max_length=200)
    inputSong = models.CharField(max_length=200)
    def __unicode__(self):
        return str(self.Track)+" - "+str(self.User)
class ResponseAdmin(admin.ModelAdmin):
    pass
class TrackAdmin(admin.ModelAdmin):
    pass
class TrackAccessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Track,TrackAdmin)
admin.site.register(Response,ResponseAdmin)
admin.site.register(TrackAccess,TrackAccessAdmin)
