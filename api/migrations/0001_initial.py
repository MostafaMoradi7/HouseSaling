# Generated by Django 4.2.7 on 2023-11-23 15:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HouseModel",
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
                (
                    "unique_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("area", models.IntegerField()),
                ("floor", models.IntegerField()),
                ("city", models.CharField(max_length=150)),
                ("price", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[("FREE", "FREE"), ("BAUGHT", "BAUGHT")], max_length=50
                    ),
                ),
            ],
        ),
    ]