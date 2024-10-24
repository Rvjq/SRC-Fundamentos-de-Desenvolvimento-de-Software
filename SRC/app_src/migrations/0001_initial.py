# Generated by Django 5.1 on 2024-09-25 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import app_src.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("telephone", models.CharField(max_length=20)),
                ("interprise", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=1000, null=True)),
                (
                    "ra",
                    models.CharField(
                        default=app_src.models.generate_unique_ra,
                        max_length=10,
                        unique=True,
                    ),
                ),
                (
                    "contractor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contractor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
