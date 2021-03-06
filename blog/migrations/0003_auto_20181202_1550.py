# Generated by Django 2.0.6 on 2018-12-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(default='profiles/no-img.jpg', upload_to='profiles/'),
        ),
    ]
