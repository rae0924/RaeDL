# Generated by Django 2.2.4 on 2019-08-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='img_name',
            field=models.TextField(default='x'),
        ),
    ]