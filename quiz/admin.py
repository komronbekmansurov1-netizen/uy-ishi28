from django.contrib import admin
from .models import Quiz
# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Quiz._meta.fields]
    search_fields = []
    list_filter = []

admin.site.register(Quiz, QuizAdmin)
