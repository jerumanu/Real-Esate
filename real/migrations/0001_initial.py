# Generated by Django 4.0.4 on 2022-05-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amentitis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security', models.CharField(max_length=10)),
                ('parking', models.CharField(max_length=10)),
                ('power', models.CharField(max_length=10)),
                ('pool', models.CharField(max_length=10)),
                ('water', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail_descripe', models.CharField(max_length=50)),
                ('photos', models.ImageField(upload_to='')),
                ('bedRooms', models.IntegerField()),
                ('bathRoom', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locations', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
