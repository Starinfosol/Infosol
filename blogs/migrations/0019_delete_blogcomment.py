# Generated by Django 3.2.3 on 2021-05-26 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_rename_comment_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
