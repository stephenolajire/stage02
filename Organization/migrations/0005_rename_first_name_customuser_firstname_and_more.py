# Generated by Django 5.0.6 on 2024-07-06 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0004_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='last_name',
            new_name='lastName',
        ),
    ]
