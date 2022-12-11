from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedModelAdmin, NestedStackedInline

from app.models import Teacher, Student, Exercise, Group


# Register your models here.


class StudentInline(NestedStackedInline):
    model = Student
    extra = 1


class GroupInline(NestedTabularInline):
    model = Group
    extra = 0
    inlines = [StudentInline]


class TeacherAdmin(NestedModelAdmin):
    list_display = ['name', 'last_name', 'email', 'owner']
    list_filter = ['last_name']
    fieldsets = [
        ('General Information', {'fields': ['name', 'last_name', 'email']}),
        ('Owner', {'fields': ['owner']})
    ]
    inlines = [GroupInline]


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Teacher', {'fields': ['teacher']}),
    ]
    inlines = [StudentInline]

    @admin.display
    def get_student(self, obj):
        if obj.student is not None:
            return f"{obj.student.name} ({obj.student.surname})"
        return "---"


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'school', 'edu_level', 'phone', 'group']
    list_filter = ['last_name', 'school', 'edu_level']
    fieldsets = [
        ('General Information', {'fields': ['name', 'last_name', 'email', 'phone']}),
        ('Education', {'fields': ['school', 'edu_level', 'group']})
    ]

    def has_add_permission(self, request):
        return False


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Exercise),
admin.site.register(Group, GroupAdmin)
