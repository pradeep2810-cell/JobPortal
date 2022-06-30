from django.contrib import admin
from application.models import Application
# Register your models here.


class AppAdmin(admin.ModelAdmin):
    list_display=('apply_date','user_id','job_id','status')

admin.site.register(Application,AppAdmin)
