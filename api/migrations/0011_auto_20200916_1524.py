# Generated by Django 3.1.1 on 2020-09-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_meaning_grammatical_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='meaning',
            name='exemple',
            field=models.ManyToManyField(to='api.Exemple'),
        ),
        migrations.AddField(
            model_name='meaning',
            name='families',
            field=models.ManyToManyField(blank=True, to='api.Family'),
        ),
    ]
