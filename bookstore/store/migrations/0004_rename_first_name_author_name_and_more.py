# Generated by Django 5.0.6 on 2024-05-29 09:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_book_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="author",
            old_name="first_name",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="author",
            name="last_name",
        ),
    ]