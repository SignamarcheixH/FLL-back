# Generated by Django 3.1.1 on 2020-09-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200916_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pronunciation',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
