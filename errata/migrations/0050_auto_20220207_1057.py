# Generated by Django 3.2.5 on 2022-02-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0049_alter_errata_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtext',
            name='email_case',
            field=models.CharField(blank=True, choices=[('Created in Fall', 'Created in Fall'), ('Created in Spring', 'Created in Spring'), ('Reviewed and (will not fix, or duplicate, or not an error, or major book revision)', 'Reviewed and (will not fix, or duplicate, or not an error, or major book revision)'), ('Reviewed and Approved', 'Reviewed and Approved'), ('Completed and Sent to Customer Support', 'Completed and Sent to Customer Support'), ('More Information Requested', 'More Information Requested'), ('Getting New Edition', 'Getting New Edition'), ('Partner Product', 'Partner Product'), ('Generic Completed Response', 'Generic Completed Response'), ('Technical Error', 'Technical Error'), ('Deprecated', 'Deprecated')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errata',
            name='resolution',
            field=models.CharField(blank=True, choices=[('Duplicate', 'Duplicate'), ('Not An Error', 'Not An Error'), ('Will Not Fix', 'Will Not Fix'), ('Approved', 'Approved'), ('Major Book Revision', 'Major Book Revision'), ('Technical Error', 'Technical Error'), ('Partner Product', 'Partner Product'), ('Sent to Customer Support', 'Sent to Customer Support'), ('More Information Requested', 'More Information Requested'), ('Deprecated', 'Deprecated')], max_length=100, null=True),
        ),
    ]
