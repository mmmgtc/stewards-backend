# Generated by Django 4.0.6 on 2022-08-17 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_steward_address_workstream_short_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtc_balance', models.JSONField()),
                ('stable_coin_balance', models.JSONField()),
                ('gtc_graph', models.JSONField()),
                ('stable_graph', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='workstream',
            name='short_name',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]