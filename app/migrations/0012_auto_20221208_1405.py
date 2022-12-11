# Generated by Django 3.2.12 on 2022-12-08 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_student_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='teacher',
        ),
        migrations.AddField(
            model_name='exercise',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.group'),
        ),
    ]
