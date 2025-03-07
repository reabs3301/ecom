# Generated by Django 5.1.6 on 2025-03-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp', '0006_acheter_client'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='user_name',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user_password',
        ),
        migrations.AddField(
            model_name='client',
            name='role',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default='', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
