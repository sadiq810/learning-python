from django.contrib import admin
from one_app.models import Topic, Webpage, AccessRecord, Users, UserProfileInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Users)
admin.site.register(UserProfileInfo)