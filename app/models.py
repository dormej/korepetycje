from django.db import models

# Create your models here.


class Student(models.Model):
    SCHOOL_CHOICES = (
        ('Primary Scool', 'Primary School'),
        ('High School', 'High School')
    )
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.CharField(choices=SCHOOL_CHOICES, max_length=25)
    edu_level = models.IntegerField('Klasa', max_length=1)
    phone = models.IntegerField(max_length=9)

    class Meta:
        verbose_name = 'Students'
        verbose_name_plural = 'Studenci'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name}, {self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Exercise(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Exercises'
        verbose_name_plural = 'Exercises'

    def __str__(self):
        return f'{self.title}'
