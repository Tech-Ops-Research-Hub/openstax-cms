# Generated by Django 3.2.16 on 2022-12-12 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0104_alter_partner_visible_on_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='testimonial',
        ),
        migrations.RemoveField(
            model_name='school',
            name='testimonial_name',
        ),
        migrations.RemoveField(
            model_name='school',
            name='testimonial_position',
        ),
    ]
