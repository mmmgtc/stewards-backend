# Generated by Django 4.0.6 on 2022-08-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_stats_gtc_balance_alter_stats_gtc_graph_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='gtc_balance',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='stats',
            name='gtc_graph',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='stats',
            name='stable_coin_balance',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='stats',
            name='stable_graph',
            field=models.JSONField(default=dict),
        ),
    ]