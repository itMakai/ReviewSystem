# Generated by Django 5.0.6 on 2024-06-09 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_remove_reviewdetail_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review_detail',
            old_name='lecturer',
            new_name='lecturername',
        ),
    ]
