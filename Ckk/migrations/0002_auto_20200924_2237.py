# Generated by Django 3.1 on 2020-09-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='testCat', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='subcat',
            field=models.CharField(default='TestSubCat', max_length=50),
            preserve_default=False,
        ),
    ]
