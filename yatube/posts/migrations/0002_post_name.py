# Generated by Django 2.2 on 2022-05-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='unknown', max_length=200),
        ),
    ]
