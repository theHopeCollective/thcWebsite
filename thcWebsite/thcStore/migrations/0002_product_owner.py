# Generated by Django 2.2.2 on 2019-06-26 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thcStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.CharField(db_index=True, default='', max_length=200),
        ),
    ]
