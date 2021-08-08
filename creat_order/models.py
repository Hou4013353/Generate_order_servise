from django.db import models


# Create your models here.

class user_info(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name="用户ID")
    user_name = models.CharField(max_length=18,verbose_name="用户名")
    password = models.CharField(max_length=255, verbose_name="用户密码")
    nick_name = models.CharField(max_length=255, verbose_name="昵称", null=True)
    phone_num = models.CharField(max_length=50, verbose_name="用户名", null=True)
    user_header_pic = models.CharField(max_length=255, verbose_name="用户头像", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class head_tail(models.Model):
    user = models.OneToOneField("user_info", on_delete=models.DO_NOTHING)
    head_value = models.TextField(null=True, verbose_name="表头")
    end_value = models.TextField(null=True, verbose_name="表尾")
    small_tail_value = models.TextField(null=True,verbose_name="小尾巴")
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class auntie_type(models.Model):
    type_id = models.AutoField(primary_key=True, verbose_name="阿姨类型ID")
    type = models.CharField(max_length=255, verbose_name="阿姨类型")
    scope_of_work = models.CharField(max_length=255, verbose_name="工作范围",null=True)
    auntie_value = models.CharField(max_length=255, verbose_name="value", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class work_time(models.Model):
    worktime_id = models.AutoField(primary_key=True, verbose_name="工作时间ID")
    worktime = models.CharField(max_length=255, verbose_name="工作时间")
    work_value = models.CharField(max_length=255, verbose_name="value", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class assist_work(models.Model):
    assist_work_id = models.AutoField(primary_key=True, verbose_name="辅助工作ID")
    assist_work = models.CharField(max_length=255, verbose_name="辅助工作")
    assist_value = models.CharField(max_length=255, verbose_name="value", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class order_status(models.Model):
    order_status_id = models.AutoField(primary_key=True, verbose_name="成交状态ID")
    order_status = models.CharField(max_length=255, verbose_name="成交状态")
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class close_reason(models.Model):
    close_reason_id = models.AutoField(primary_key=True, verbose_name="关闭状态ID")
    close_reason = models.CharField(max_length=255, verbose_name="关闭原因")
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class customer_channel(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name="客户渠道ID")
    customer_channel = models.CharField(max_length=255, verbose_name="客户渠道")
    customer_value = models.CharField(max_length=255, verbose_name="对应value", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)


class rest_mode(models.Model):
    rest_id = models.AutoField(primary_key=True, verbose_name="自增ID")
    rest = models.CharField(max_length=255, verbose_name="休息方式")
    rest_value = models.CharField(max_length=255, verbose_name="对应value", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间")
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)



class customer_information(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name="客户ID")
    user_id = models.ManyToManyField(user_info)
    customer_name = models.CharField(max_length=255, verbose_name="客户姓名")
    customer_phone = models.CharField(max_length=255, verbose_name="客户电话")
    wx_num = models.CharField(max_length=255, verbose_name="微信号", null=True)
    cityname = models.CharField(max_length=255, verbose_name="城市名")
    latlng_lat = models.CharField(max_length=255, verbose_name="经度")
    latlng_lng = models.CharField(max_length=255, verbose_name="纬度")
    poiaddress = models.CharField(max_length=255, verbose_name="前缀地址")  # 例：江苏省徐州市鼓楼区大马路99
    poiname = models.CharField(max_length=255, verbose_name="地址名")  # 例：红星美凯龙
    detailed_address = models.CharField(max_length=255, verbose_name="详细地址",null=True)  # 门牌号，例：A5-2-2231
    work_money = models.CharField(max_length=255, verbose_name="工资")
    family_size = models.CharField(max_length=255, verbose_name="家庭面积", null=True)
    auntie_type = models.ForeignKey("auntie_type", on_delete=models.DO_NOTHING, verbose_name="阿姨类型")  # 月嫂、育儿、保姆
    type_of_work = models.ForeignKey("work_time", on_delete=models.DO_NOTHING, verbose_name="工作时间")  # 24小时、白班
    other_work = models.TextField(verbose_name="其他要求", null=True)
    assist_work = models.ForeignKey("assist_work", on_delete=models.DO_NOTHING, verbose_name="辅助工作", null=True)  # 辅助工作
    work_start_time = models.CharField(max_length=255, verbose_name="工作开始时间", null=True)
    work_end_time = models.CharField(max_length=255, verbose_name="工作结束时间", null=True)
    order_switch = models.BooleanField(verbose_name="订单开关状态",default=True)
    order_status = models.ForeignKey("order_status", on_delete=models.DO_NOTHING, verbose_name="成交状态", null=True)# 新订单还是老单换人
    close_reson = models.ForeignKey("close_reason", on_delete=models.DO_NOTHING, verbose_name="关闭原因", null=True)
    other_reason = models.CharField(max_length=255, verbose_name="其他原因", null=True)
    customer_qudao = models.ForeignKey("customer_channel", on_delete=models.DO_NOTHING, verbose_name="客户渠道", null=True)
    rest_mode = models.ForeignKey("rest_mode", on_delete=models.DO_NOTHING, verbose_name="休息时间", null=True)
    registration_time = models.DateTimeField(max_length=255, verbose_name="创建时间",auto_now_add=True)
    registrant = models.CharField(max_length=255, verbose_name="创建人")
    revision_time = models.DateTimeField(max_length=255, verbose_name="修改时间", null=True)
    reviser = models.CharField(max_length=255, verbose_name="修改人", null=True)
