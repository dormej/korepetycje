# Generated by Django 3.2.12 on 2022-12-08 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20221208_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
    ]
