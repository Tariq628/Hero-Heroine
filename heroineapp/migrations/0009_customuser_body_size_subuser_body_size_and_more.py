# Generated by Django 4.1.7 on 2023-02-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroineapp', '0008_remove_brand_category_category_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='body_size',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subuser',
            name='body_size',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='height',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subuser',
            name='height',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
