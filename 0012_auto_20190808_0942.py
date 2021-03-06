# Generated by Django 2.2.3 on 2019-08-08 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Life', '0011_auto_20190803_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediafile', models.FileField(upload_to='')),
                ('filetype', models.CharField(max_length=50)),
                ('uploadbyemailid', models.CharField(max_length=50)),
                ('uploadbyadminoruser', models.CharField(max_length=10)),
                ('uploaddate', models.DateField()),
                ('topicname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('likescount', models.IntegerField()),
                ('videostatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('emailid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='')),
                ('userstatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MediaFiles',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
