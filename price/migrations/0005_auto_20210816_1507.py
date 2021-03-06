# Generated by Django 3.2.6 on 2021-08-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0004_auto_20210816_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricecategory',
            name='title_ru',
            field=models.CharField(max_length=300, verbose_name='Название (РУС)'),
        ),
        migrations.AlterField(
            model_name='pricecategory',
            name='title_uz',
            field=models.CharField(max_length=300, verbose_name='Название (УЗБ)'),
        ),
        migrations.AlterField(
            model_name='pricesubcategory',
            name='title_ru',
            field=models.CharField(max_length=300, verbose_name='Услуга (РУС)'),
        ),
        migrations.AlterField(
            model_name='pricesubcategory',
            name='title_uz',
            field=models.CharField(max_length=300, verbose_name='Услуга (УЗБ)'),
        ),
    ]
