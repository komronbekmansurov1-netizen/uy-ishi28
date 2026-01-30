from django.contrib import admin
from .models import Answer
# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Answer._meta.fields]
    search_fields = []
    list_filter = []

admin.site.register(Answer, AnswerAdmin)
