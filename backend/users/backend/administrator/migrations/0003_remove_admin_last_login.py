# Generated by Django 4.1.7 on 2023-05-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_remove_admin_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='last_login',
        ),
    ]
