# Generated by Django 3.2.5 on 2021-07-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creat_order', '0007_alter_customer_information_detailed_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='close_reason',
            name='other_reason',
        ),
        migrations.AddField(
            model_name='customer_information',
            name='other_reason',
            field=models.CharField(max_length=255, null=True, verbose_name='其他原因'),
        ),
    ]
