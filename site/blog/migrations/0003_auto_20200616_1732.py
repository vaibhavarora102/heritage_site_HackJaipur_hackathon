# Generated by Django 3.0.7 on 2020-06-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200616_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image2',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image3',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image4',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image5',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_image6',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
    ]
