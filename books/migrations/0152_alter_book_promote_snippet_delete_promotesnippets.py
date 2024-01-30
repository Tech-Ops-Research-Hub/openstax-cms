# Generated by Django 4.1.7 on 2024-01-29 22:44

import books.models
from django.db import migrations
import snippets.models
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0151_book_promote_snippet_promotesnippets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="promote_snippet",
            field=wagtail.fields.StreamField(
                [("content", books.models.PromoteSnippetContentChooserBlock(snippets.models.PromoteSnippet))],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.DeleteModel(
            name="PromoteSnippets",
        ),
    ]
