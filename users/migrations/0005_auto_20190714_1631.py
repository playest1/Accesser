# Generated by Django 2.2.3 on 2019-07-14 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190714_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='users.Profession'),
        ),
    ]
