# Generated by Django 3.2.12 on 2022-12-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20221208_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, to='app.Student'),
        ),
    ]
