# Generated by Django 3.1.1 on 2020-09-16 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_meaning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meaning',
            name='language',
        ),
        migrations.AddField(
            model_name='meaning',
            name='word',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api.word'),
        ),
    ]
