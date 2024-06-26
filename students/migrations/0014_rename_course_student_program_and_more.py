# Generated by Django 5.0.6 on 2024-06-11 13:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_review_detail_comment_review_detail_lecturer_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='program',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='first name', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='last name', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default=254722000000, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
