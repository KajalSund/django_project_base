from django.shortcuts import render
from django.http import HttpResponse
from frst_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    #my_dict = {'insert_me': "Now I am coming from frst_app/index.html!"}
    return render(request, 'frst_app/index.html', context = date_dict)