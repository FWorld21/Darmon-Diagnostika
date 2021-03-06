# Generated by Django 3.2.6 on 2021-08-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xray', '0002_rename_uziitem_xrayitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xrayitem',
            options={'verbose_name': 'Текст для страницы рентген-кабинет', 'verbose_name_plural': 'Текста для страницы рентген-кабинет'},
        ),
        migrations.RemoveField(
            model_name='xrayitem',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='xrayitem',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='xrayitem',
            name='title_uz',
        ),
        migrations.AlterField(
            model_name='xrayitem',
            name='description_ru',
            field=models.TextField(verbose_name='Содержание (РУС)'),
        ),
        migrations.AlterField(
            model_name='xrayitem',
            name='description_uz',
            field=models.TextField(verbose_name='Содержание (УЗБ)'),
        ),
    ]
