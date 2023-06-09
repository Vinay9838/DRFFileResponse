# Generated by Django 4.2.1 on 2023-05-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=500)),
                ('gender', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('image', models.URLField(max_length=2000)),
            ],
        ),
    ]
