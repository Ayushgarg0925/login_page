# Generated by Django 4.2 on 2023-04-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=20)),
                ('eage', models.IntegerField(max_length=10)),
                ('eno', models.CharField(max_length=15)),
                ('eaddress', models.CharField(max_length=50)),
                ('epassword', models.CharField(max_length=10)),
            ],
        ),
    ]