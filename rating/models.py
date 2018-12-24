# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import json

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Teacher(models.Model):
    name = models.CharField(max_length=200)
    score1 = models.FloatField(default=0)
    score1_content = models.CharField(max_length=500, default='着装合理，治学严谨。严于律己，从不迟到早退')
    score1_count = models.IntegerField(default=0)

    score2 = models.FloatField(default=0)
    score2_content = models.CharField(max_length=500, default='教学认真，授课内容详细，课堂效率高')    
    score2_count = models.IntegerField(default=0)
    
    score3 = models.FloatField(default=0)
    score3_content = models.CharField(max_length=500, default='教学方法多样，重点与难点内容区分清楚，讲解得当')    
    score3_count = models.IntegerField(default=0)
    
    score4 = models.FloatField(default=0)
    score4_content = models.CharField(max_length=500, default='授课方式诙谐幽默，讲解深入浅出。')
    score4_count = models.IntegerField(default=0)

    score5 = models.FloatField(default=0)
    score5_content = models.CharField(max_length=500, default='采用多媒体辅助教学，制作的电子教案详略得当，效果好。')
    score5_count = models.IntegerField(default=0)

    score6 = models.FloatField(default=0)
    score6_content = models.CharField(max_length=500, default='强调独立思考，启发引导学生发现问题并解决问题。')
    score6_count = models.IntegerField(default=0)

    score7 = models.FloatField(default=0)
    score7_content = models.CharField(max_length=500, default='课堂气氛活跃，师生互动良好。')
    score7_count = models.IntegerField(default=0)

    score8 = models.FloatField(default=0)
    score8_content = models.CharField(max_length=500, default='在上课过程中会讲授做人的道理，帮助学生形成正确的人生观，关心学生成长。')
    score8_count = models.IntegerField(default=0)

    score9 = models.FloatField(default=0)
    score9_content = models.CharField(max_length=500, default='虚心接受学生的建议，能适时调整教学方法和进度，对学生不厌其烦，耐心讲解。')
    score9_count = models.IntegerField(default=0)

    score10 = models.FloatField(default=0)
    score10_content = models.CharField(max_length=500, default='认真批改作业，能及时准确的发现同学们存在的问题并加以解决。')
    score10_count = models.IntegerField(default=0)

    score_total = models.FloatField(default=0)
    tid = models.AutoField(primary_key=True)
    major = models.CharField(max_length=200, default='工学系')
    intro = models.TextField(default='个人简介，待补充')
    stars_filled = models.CharField(max_length=5, default='x')
    stars_empty = models.CharField(max_length=5, default='yyyy')
    score_rater = models.CharField(max_length=5000, default='[1]')

    def add_rater(self, rater):
        tmp = json.loads(self.score_rater)
        tmp.append(rater)
        self.score_rater = json.dumps(tmp)

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@python_2_unicode_compatible  # only if you need to support Python 2
class Major(models.Model):
    name = models.CharField(max_length=30, default=u"工学系")

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)

@python_2_unicode_compatible  # only if you need to support Python 2
class Class(models.Model):
    name = models.CharField(max_length=30)
    num_stu = models.IntegerField(default=30)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name','num_stu',)


@python_2_unicode_compatible  # only if you need to support Python 2
class Course(models.Model):
    name = models.CharField(max_length=30)
    # class_name = models.ManyToManyField(Class)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name',)

@python_2_unicode_compatible  # only if you need to support Python 2
class CourseForClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    room = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return str(self.course) + ' ' + str(self.class_name)


    class Meta:
        ordering = ('course', 'class_name')
        unique_together = ("course", "class_name",)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #For Student User
    school_num = models.CharField(max_length=30, blank=True)
    class_num = models.CharField(max_length=30, blank=True)

    #For Teacher User
    work_id = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    # all_courses = models.ManyToManyField(Course)

@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs): 
    if created: 
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs): 
    instance.profile.save()



class RatingItem(models.Model):
    content = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.content

    class Meta:
        ordering  = ('content', )


class ItemScore(models.Model):
    item = models.ForeignKey(RatingItem, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    rater = models.CharField(max_length=30, default='')

    def __str__(self):
        return str(self.item) + ' ' + str(self.score) + ' ' + str(self.rater)

    class Meta:
        ordering  = ('item','score', 'rater', )

class Teacher2(models.Model):
    name = models.CharField(max_length=30, default='')
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    intro = models.TextField(default='个人简介，待补充')
    stars_filled = models.CharField(max_length=5, default='x')
    stars_empty = models.CharField(max_length=5, default='yyyy')
    score_total = models.FloatField(default=0)
    score_rater = models.CharField(max_length=5000, default='[1]')
    rater_count = models.IntegerField(default=0)
    work_id = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)    
    all_courses = models.ManyToManyField(CourseForClass, blank=True)
    
    def add_rater(self, rater):
        tmp = json.loads(self.score_rater)
        tmp.append(rater)
        self.rater_count = len(tmp)- 1
        self.score_rater = json.dumps(tmp)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class RatingForTeacher(models.Model):
    teacher = models.ForeignKey(Teacher2, on_delete=models.CASCADE)
    item_score = models.ManyToManyField(ItemScore)


    def __str__(self):
        return str(self.teacher)

    class Meta:
        ordering = ('teacher',)




class Student(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=200, default='工学系')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)


    def __str__(self):
        return self.profile.username

    class Meta:
        ordering = ('profile','major', 'class_name')



















