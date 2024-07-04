# Generated by Django 5.0.6 on 2024-05-31 18:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_rename_first_name_author_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["title"]},
        ),
        migrations.AlterModelOptions(
            name="categorie",
            options={"ordering": ["title"]},
        ),
        migrations.AlterModelOptions(
            name="publisher",
            options={"ordering": ["title"]},
        ),
    ]
