# Generated by Django 2.2.5 on 2020-12-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201212_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='path',
            field=models.CharField(max_length=100),
        ),
    ]