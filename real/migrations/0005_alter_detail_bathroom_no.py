# Generated by Django 4.0.4 on 2022-05-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0004_rename_bedrom_no_detail_bedroom_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='bathroom_no',
            field=models.IntegerField(),
        ),
    ]
