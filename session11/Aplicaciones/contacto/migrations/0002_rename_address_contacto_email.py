# Generated by Django 4.2.4 on 2023-10-06 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacto", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contacto", old_name="address", new_name="email",
        ),
    ]