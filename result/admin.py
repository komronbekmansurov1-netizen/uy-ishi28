from django.contrib import admin
from .models import Result
# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Result._meta.fields]
    search_fields = []
    list_filter = []

admin.site.register(Result, ResultAdmin)