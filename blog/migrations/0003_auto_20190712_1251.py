# Generated by Django 2.2.2 on 2019-07-12 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='shirt_size',
            new_name='school_name',
        ),
    ]
