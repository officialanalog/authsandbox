# Generated by Django 3.2.6 on 2021-08-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_useraccount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
