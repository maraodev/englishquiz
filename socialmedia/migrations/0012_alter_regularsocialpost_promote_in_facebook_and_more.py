# Generated by Django 4.0.5 on 2022-07-27 09:40

from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("socialmedia", "0011_instagrampost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="regularsocialpost",
            name="promote_in_facebook",
            field=models.BooleanField(default=True, verbose_name="Promote in Facebook"),
        ),
        migrations.AlterField(
            model_name="scheduledsocialpost",
            name="promote_in_facebook",
            field=models.BooleanField(default=True, verbose_name="Promote in Facebook"),
        ),
    ]
