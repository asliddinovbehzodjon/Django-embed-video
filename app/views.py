from django.shortcuts import render
from .models import Video
# Create your views here.
def homepage(request):
    videos=Video.objects.all()
    return render(request,'index.html',{'videos':videos})
