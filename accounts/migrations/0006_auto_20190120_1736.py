# Generated by Django 2.0.6 on 2019-01-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190119_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]