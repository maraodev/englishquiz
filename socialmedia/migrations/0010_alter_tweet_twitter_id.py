# Generated by Django 4.0.5 on 2022-07-18 17:48

from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("socialmedia", "0009_alter_facebookpost_facebook_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="twitter_id",
            field=models.PositiveBigIntegerField(),
        ),
    ]