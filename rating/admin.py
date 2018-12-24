from django.contrib import admin

# Register your models here.
from .models import Teacher, Course, Major, Class, CourseForClass, Teacher2, RatingItem, ItemScore, RatingForTeacher, Student

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', )

class MajorAdmin(admin.ModelAdmin):
    list_display = ('name',  )

class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_stu', )

class CourseForClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'class_name', )

class StudentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'major', 'class_name', )

class Teacher2Admin(admin.ModelAdmin):
    list_display = ('name', )

class RatingItemAdmin(admin.ModelAdmin):
	list_display = ('content', )

class ItemScoreAdmin(admin.ModelAdmin):
	list_display = ('item', 'score', 'rater', )

class RatingForTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, TeacherAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(CourseForClass, CourseForClassAdmin)
admin.site.register(Teacher2, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(RatingItem, RatingItemAdmin)
admin.site.register(ItemScore, ItemScoreAdmin)
admin.site.register(RatingForTeacher, RatingForTeacherAdmin)



from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from rating.models import Profile

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





