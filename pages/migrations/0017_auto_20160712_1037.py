# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 15:37
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20160707_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('person', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('position', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('biography', wagtail.wagtailcore.blocks.RichTextBlock())))))),
        ),
    ]
