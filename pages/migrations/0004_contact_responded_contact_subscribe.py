# Generated by Django 4.1 on 2022-08-21 18:46

from __future__ import annotations

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_contact_response"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="responded",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="contact",
            name="subscribe",
            field=models.BooleanField(default=False),
        ),
    ]
