# Generated by Django 2.0.4 on 2019-10-14 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='blog_image',
            new_name='image',
        ),
    ]
