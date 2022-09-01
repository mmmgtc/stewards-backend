# Generated by Django 4.0.6 on 2022-07-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='steward',
            name='address',
        ),
        migrations.AddField(
            model_name='workstream',
            name='short_name',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]