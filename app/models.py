from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Teachers'
        verbose_name_plural = 'Teachers'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name}, {self.name}'


class Group(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Groups'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return f'{self.name}'


class Student(models.Model):
    SCHOOL_CHOICES = (
        ('Primary School', 'Primary School'),
        ('High School', 'High School')
    )
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.CharField(choices=SCHOOL_CHOICES, max_length=25)
    edu_level = models.CharField('Klasa', max_length=1)
    phone = models.CharField(max_length=9)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Students'
        verbose_name_plural = 'Students'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name}, {self.name}'


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Exercises'
        verbose_name_plural = 'Exercises'

    def __str__(self):
        return f'{self.title}'
