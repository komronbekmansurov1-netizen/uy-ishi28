from django.contrib import admin
from .models import Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]
    search_fields = []
    list_filter = []

admin.site.register(Question, QuestionAdmin)
