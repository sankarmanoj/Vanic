from django.conf.urls import url
import views
from django.contrib import admin
urlpatterns = [
    url(r'^$',views.index),
    url(r'^bye/',views.bye),
    url(r'^login/',admin.site.urls),
    url(r'^response/',views.response)
]
