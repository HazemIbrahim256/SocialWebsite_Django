# Generated by Django 4.0.6 on 2022-08-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-picture.jpg', upload_to='profile_images'),
        ),
    ]
