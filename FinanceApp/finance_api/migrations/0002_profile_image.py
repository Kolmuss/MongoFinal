# Generated by Django 3.0.5 on 2021-05-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
