# Generated by Django 3.2.6 on 2021-08-16 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesubcategory',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='price.pricecategory', verbose_name='Для категории'),
        ),
    ]