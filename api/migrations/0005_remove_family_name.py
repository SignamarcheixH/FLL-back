# Generated by Django 3.1.1 on 2020-09-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200916_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='name',
        ),
    ]