# Generated by Django 4.1.2 on 2022-11-10 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Exercises',
                'verbose_name_plural': 'Exercises',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Teachers',
                'verbose_name_plural': 'Teachers',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('school', models.CharField(choices=[('Primary Scool', 'Primary School'), ('High School', 'High School')], max_length=25)),
                ('edu_level', models.IntegerField(max_length=1, verbose_name='Klasa')),
                ('phone', models.IntegerField(max_length=9)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.teacher')),
            ],
            options={
                'verbose_name': 'Students',
                'verbose_name_plural': 'Studenci',
                'ordering': ['last_name'],
            },
        ),
    ]
