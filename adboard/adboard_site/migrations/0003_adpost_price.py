# Generated by Django 4.0.6 on 2022-07-18 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adboard_site', '0002_alter_category_name_adpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='adpost',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='price'),
        ),
    ]
