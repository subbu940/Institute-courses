# Generated by Django 2.2.6 on 2019-11-21 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20191120_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='referred_by',
        ),
    ]