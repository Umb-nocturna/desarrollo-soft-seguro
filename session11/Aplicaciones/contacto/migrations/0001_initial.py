# Generated by Django 4.2.4 on 2023-10-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacto",
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
                ("name", models.CharField(max_length=90)),
                ("address", models.CharField(max_length=90)),
                ("phone", models.CharField(max_length=90)),
                ("message", models.CharField(max_length=2000)),
            ],
        ),
    ]
