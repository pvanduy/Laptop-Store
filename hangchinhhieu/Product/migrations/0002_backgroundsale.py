# Generated by Django 4.0.6 on 2022-12-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackGroundSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BackGroundSaleImg', models.ImageField(upload_to='image')),
                ('BackGroundSaleImgAlt', models.CharField(max_length=300)),
            ],
        ),
    ]
