# Generated by Django 3.1 on 2020-09-28 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ckk', '0005_auto_20200927_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc_txt',
            new_name='desc_text',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='url',
            new_name='link',
        ),
    ]
