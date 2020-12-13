# Generated by Django 3.1.3 on 2020-12-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]