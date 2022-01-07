# Generated by Django 3.2.9 on 2022-01-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0005_auto_20211021_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundraiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_scheme', models.CharField(blank=True, choices=[('Red', 'red'), ('Blue', 'blue'), ('Green', 'green'), ('Orange', 'orange')], default='', max_length=255)),
                ('message_type', models.CharField(blank=True, choices=[('Goal', 'goal'), ('Message', 'message')], default='', max_length=255)),
                ('headline', models.TextField(blank=True, default='', null=True)),
                ('message', models.TextField(blank=True, default='', null=True)),
                ('button_text', models.CharField(max_length=255)),
                ('button_url', models.CharField(max_length=255)),
                ('box_headline', models.TextField(blank=True, default='', null=True)),
                ('box_html', models.TextField(blank=True, default='', null=True)),
                ('fundraiser_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('goal_amount', models.IntegerField(blank=True, null=True)),
                ('goal_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
