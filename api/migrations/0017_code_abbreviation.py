# Generated by Django 3.1.1 on 2020-09-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200922_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
