# Generated by Django 2.2.1 on 2019-06-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_nonprofit',
            field=models.BooleanField(default=False, verbose_name='Are you representing a Wake County Based Nonprofit looking to benefit our community?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_artist',
            field=models.BooleanField(default=False, verbose_name='Are you a Wake County Based Artist?'),
        ),
    ]
