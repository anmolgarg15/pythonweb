# Generated by Django 2.2.3 on 2019-07-26 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Life', '0004_auto_20190724_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafiles',
            name='mediafile',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='users',
            name='picture',
            field=models.FileField(upload_to='media'),
        ),
    ]