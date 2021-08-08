from django.contrib import admin
from .models import Video
# Register your models here.
from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Video,AdminVideo)