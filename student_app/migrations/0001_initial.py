# Generated by Django 5.1.1 on 2024-09-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_class', models.CharField(max_length=100)),
                ('s_addr', models.CharField(max_length=100)),
                ('s_school', models.CharField(max_length=100)),
                ('s_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
