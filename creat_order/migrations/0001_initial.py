# Generated by Django 3.2.5 on 2021-07-21 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assist_work',
            fields=[
                ('assist_work_id', models.AutoField(primary_key=True, serialize=False, verbose_name='辅助工作ID')),
                ('assist_work', models.CharField(max_length=255, verbose_name='辅助工作')),
                ('assist_value', models.CharField(max_length=255, null=True, verbose_name='value')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='auntie_type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False, verbose_name='阿姨类型ID')),
                ('type', models.CharField(max_length=255, verbose_name='阿姨类型')),
                ('auntie_value', models.CharField(max_length=255, null=True, verbose_name='value')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='close_reason',
            fields=[
                ('close_reason_id', models.AutoField(primary_key=True, serialize=False, verbose_name='关闭状态ID')),
                ('close_reason', models.CharField(max_length=255, verbose_name='关闭原因')),
                ('other_reason', models.CharField(max_length=255, null=True, verbose_name='其他原因')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='customer_channel',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='客户渠道ID')),
                ('customer_channel', models.CharField(max_length=255, verbose_name='客户渠道')),
                ('customer_value', models.CharField(max_length=255, null=True, verbose_name='对应value')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='order_status',
            fields=[
                ('order_status_id', models.AutoField(primary_key=True, serialize=False, verbose_name='成交状态ID')),
                ('order_status', models.CharField(max_length=255, verbose_name='成交状态')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('user_name', models.CharField(max_length=16, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='用户密码')),
                ('nick_name', models.CharField(max_length=255, null=True, verbose_name='昵称')),
                ('phone_num', models.CharField(max_length=50, null=True, verbose_name='用户名')),
                ('user_header_pic', models.CharField(max_length=255, null=True, verbose_name='用户头像')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='work_time',
            fields=[
                ('worktime_id', models.AutoField(primary_key=True, serialize=False, verbose_name='工作时间ID')),
                ('worktime', models.CharField(max_length=255, verbose_name='工作时间')),
                ('work_value', models.CharField(max_length=255, null=True, verbose_name='value')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
            ],
        ),
        migrations.CreateModel(
            name='head_tail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_value', models.TextField(null=True, verbose_name='表头')),
                ('end_value', models.TextField(null=True, verbose_name='表尾')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.user_info')),
            ],
        ),
        migrations.CreateModel(
            name='customer_information',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='客户ID')),
                ('customer_name', models.CharField(max_length=255, verbose_name='客户姓名')),
                ('customer_phone', models.CharField(max_length=255, verbose_name='客户电话')),
                ('wx_num', models.CharField(max_length=255, null=True, verbose_name='微信号')),
                ('cityname', models.CharField(max_length=255, verbose_name='城市名')),
                ('latlng_lat', models.CharField(max_length=255, verbose_name='经度')),
                ('latlng_lng', models.CharField(max_length=255, verbose_name='纬度')),
                ('poiaddress', models.CharField(max_length=255, verbose_name='前缀地址')),
                ('poiname', models.CharField(max_length=255, verbose_name='地址名')),
                ('detailed_address', models.CharField(max_length=255, verbose_name='详细地址')),
                ('work_money', models.CharField(max_length=255, verbose_name='工资')),
                ('family_size', models.CharField(max_length=255, null=True, verbose_name='家庭面积')),
                ('other_work', models.TextField(null=True, verbose_name='其他要求')),
                ('work_start_time', models.CharField(max_length=255, null=True, verbose_name='工作开始时间')),
                ('work_end_time', models.CharField(max_length=255, null=True, verbose_name='工作结束时间')),
                ('registration_time', models.DateTimeField(max_length=255, verbose_name='创建时间')),
                ('registrant', models.CharField(max_length=255, verbose_name='创建人')),
                ('revision_time', models.DateTimeField(max_length=255, null=True, verbose_name='修改时间')),
                ('reviser', models.CharField(max_length=255, null=True, verbose_name='修改人')),
                ('assist_work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.assist_work', verbose_name='辅助工作')),
                ('auntie_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.auntie_type', verbose_name='阿姨类型')),
                ('close_reson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.close_reason', verbose_name='关闭原因')),
                ('customer_qudao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.customer_channel', verbose_name='客户渠道')),
                ('order_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.order_status', verbose_name='成交状态')),
                ('type_of_work', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='creat_order.work_time', verbose_name='工作时间')),
                ('user_id', models.ManyToManyField(to='creat_order.user_info')),
            ],
        ),
    ]