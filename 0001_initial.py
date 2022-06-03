# Generated by Django 2.2.3 on 2019-07-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topicname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MediaFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediafile', models.FileField(upload_to='Life/userpics')),
                ('filetype', models.CharField(max_length=50)),
                ('uploadbyemailid', models.CharField(max_length=60)),
                ('uploaddate', models.DateField(max_length=50)),
                ('topicname', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('emailid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('birthdate', models.DateField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='Life/userpics')),
            ],
        ),
    ]
