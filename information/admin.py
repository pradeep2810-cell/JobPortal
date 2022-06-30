from django.contrib import admin

from information.models import Information,Section



class SectionAdmin(admin.ModelAdmin):
    list_display=('title','status')

class InfoAdmin(admin.ModelAdmin):
    list_display=('section','title','details','status')

# Register your models here.
admin.site.register(Section,SectionAdmin)
admin.site.register(Information,InfoAdmin)