# Generated by Django 5.0.6 on 2024-05-29 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_publisher_alter_book_publisher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]