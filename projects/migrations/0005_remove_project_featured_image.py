# Generated by Django 4.1.3 on 2022-11-22 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='featured_image',
        ),
    ]