# Generated by Django 2.0.6 on 2018-06-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='lesson_number',
            field=models.IntegerField(default='1'),
        ),
    ]
