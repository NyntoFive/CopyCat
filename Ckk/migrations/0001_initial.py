# Generated by Django 3.1 on 2020-08-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sku', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=200)),
                ('images', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('link', models.URLField()),
                ('breadcrumbs', models.TextField()),
                ('keywords', models.CharField(max_length=200)),
                ('shop', models.PositiveIntegerField()),
                ('origin_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-shop', '-origin_date'],
            },
        ),
    ]
