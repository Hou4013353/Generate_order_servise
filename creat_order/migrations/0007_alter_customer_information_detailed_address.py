# Generated by Django 3.2.5 on 2021-07-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creat_order', '0006_auto_20210723_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_information',
            name='detailed_address',
            field=models.CharField(max_length=255, null=True, verbose_name='详细地址'),
        ),
    ]
