# Generated by Django 2.2.13 on 2020-09-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0093_resource_email_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceaccessibility',
            name='shortage_count',
            field=models.IntegerField(default=0, verbose_name='Accessibility shortage count'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unitaccessibility',
            name='shortage_count',
            field=models.IntegerField(default=0, verbose_name='Accessibility shortage count'),
            preserve_default=False,
        ),
    ]
