# Generated by Django 4.1.7 on 2023-02-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroineapp', '0002_subuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subuser',
            name='phone',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
