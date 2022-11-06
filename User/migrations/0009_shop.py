# Generated by Django 4.1.1 on 2022-10-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_townhouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeof', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='images/Shop')),
                ('price', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
            ],
        ),
    ]
