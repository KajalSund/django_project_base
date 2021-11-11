from django.conf.urls import url
from frst_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]