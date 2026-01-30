from django.contrib import admin
from .models import User1
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = '__all__'
    list_filter = "__all__"

admin.site.register(User1, UsersAdmin)
