# Generated by Django 3.0.4 on 2020-07-16 21:05

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0101_auto_20200716_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orientationfacultyresource',
            name='resource',
        ),
        migrations.AddField(
            model_name='orientationfacultyresource',
            name='creator_fest_resource',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orientationfacultyresource',
            name='resource_description',
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orientationfacultyresource',
            name='resource_heading',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orientationfacultyresource',
            name='resource_unlocked',
            field=models.BooleanField(default=False),
        ),
    ]
