
from django.contrib import admin
from .models import User, Book, Assignment
from import_export.admin import ImportExportModelAdmin


admin.site.register(User)
admin.site.register(Book)

@admin.register(Assignment)
class AssignmentAdmin(ImportExportModelAdmin):
    pass