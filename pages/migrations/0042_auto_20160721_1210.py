# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-21 17:10
from __future__ import unicode_literals

from django.db import migrations
import pages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_auto_20160721_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='row_2',
            field=wagtail.wagtailcore.fields.StreamField((('multicolumn', wagtail.wagtailcore.blocks.StreamBlock((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_3',
            field=wagtail.wagtailcore.fields.StreamField((('multicolumn', wagtail.wagtailcore.blocks.StreamBlock((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_4',
            field=wagtail.wagtailcore.fields.StreamField((('multicolumn', wagtail.wagtailcore.blocks.StreamBlock((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),))),)),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='row_5',
            field=wagtail.wagtailcore.fields.StreamField((('multicolumn', wagtail.wagtailcore.blocks.StreamBlock((('column', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('alignment', pages.models.ImageFormatChoiceBlock())), required=False)), ('cta', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(required=False))))),))),)),
        ),
    ]
