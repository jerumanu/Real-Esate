# Generated by Django 4.0.4 on 2022-05-26 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0003_rename_bathroom_detail_bathroom_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='bedrom_no',
            new_name='bedroom_no',
        ),
    ]
