# Generated by Django 3.1 on 2020-09-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile/images/default.png', upload_to='statics/profile/images', verbose_name='Image'),
        ),
    ]