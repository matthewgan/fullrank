from django.contrib import admin
from .models import visitor

# Register your models here.
class admin_log(admin.ModelAdmin):
    list_display = ('pagename', 'ip', 'user_agent', 'referer', 'timestamp') #this is models admin for view result

admin.site.register(visitor,admin_log)
