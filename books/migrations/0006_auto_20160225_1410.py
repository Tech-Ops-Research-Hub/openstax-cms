# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0004_capitalizeverbose'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('books', '0005_auto_20160224_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('description', wagtail.core.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('link_text', models.CharField(help_text='Call to Action Text', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BookStudentResources',
            fields=[
                ('studentresources_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='books.StudentResources')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('book_student_resource', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_student_resources', to='books.Book')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('books.studentresources', models.Model),
        ),
        migrations.AddField(
            model_name='studentresources',
            name='link_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='studentresources',
            name='link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='studentresources',
            name='resource',
            field=models.ForeignKey(help_text='Manage resources through snippets.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.StudentResource'),
        ),
    ]
