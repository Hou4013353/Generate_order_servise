# Generated by Django 3.2.5 on 2021-07-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creat_order', '0008_auto_20210723_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='auntie_type',
            name='scope_of_work',
            field=models.CharField(max_length=255, null=True, verbose_name='工作范围'),
        ),
    ]
