# Generated by Django 5.0.6 on 2024-06-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_reviewdetail_rating_delete_lecturerrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=models.CharField(max_length=10), max_length=100),
        ),
    ]
