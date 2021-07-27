from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
import base64
from creat_order import models
import json, datetime
import re


# 状态码
# 200  正常
# 201  没有该用户
# 202  账号或密码错误
# 203  session过期，重新登录

# 注意事项：user_name后续不能重复，作为唯一值查询用户ID，不然会有问题

# Create your views here.
# 检查session
def check_session(request):
    session_islogin = request.session.get("is_login")
    uname = request.session.get("user_name")
    # print(uname, session_islogin)
    if session_islogin == 1:
        return uname
    else:
        return False


# 获取当前时间
def registration_time(time=datetime.datetime.now()):
    """截取时分秒"""
    new_time = str(time)
    hour = new_time[0:19]
    return "".join(hour)


# 登录接口
class login(View):
    def get(self, request):
        return JsonResponse(data={"code": 200}, status=200, safe=False)

    def post(self, request):
        login_info = request.POST
        uname = login_info.get("user")
        pwd = login_info.get("password")
        # print(uname)
        # 去数据库校验账号密码是否正确
        userinfo_models = models.user_info.objects
        try:
            user_result = userinfo_models.get(user_name=uname)
            # print(user_result)
            if uname == user_result.user_name and pwd == user_result.password:
                request.session["is_login"] = 1
                request.session["user_name"] = uname
                # 登录成功
                return JsonResponse(data={"msg": "登录成功", "username": uname}, safe=False, status=200,
                                    headers={"is_login": 1})
            else:
                return JsonResponse(data={"msg": "账号或密码错误"}, safe=False, status=202)
        except models.user_info.DoesNotExist as e:
            # print(e)
            return JsonResponse(data={"msg": "没有此用户"}, safe=False, status=201)

        # 存进数据库
        # encryption_pwd = base64.b64encode(pwd.encode("utf-8"))
        # print(encryption_pwd)
        # session = request.session["user_login"]


class get_card(View):
    def get(self, request):
        session_result = check_session(request)
        if session_result:
            user_obj = models.user_info.objects
            customer_information_obj = models.customer_information.objects
            order_status_obj = models.order_status.objects
            customer_channel_obj = models.customer_channel.objects
            close_reason_obj = models.close_reason.objects
            work_time_obj = models.work_time.objects
            aunt_type_obj = models.auntie_type.objects
            rest_mode_obj = models.rest_mode.objects
            uname = session_result
            user_id = user_obj.get(user_name=uname)
            customer_Query = user_id.customer_information_set.all().order_by("-order_switch", "-customer_id")
            # print(customer_Query)
            customer_data = []
            for i in customer_Query:

                connect = ""
                custom_dict = {}
                custom_dict["id"] = i.customer_id
                custom_dict["date"] = "{}-{}-{}".format(i.registration_time.year, i.registration_time.month,
                                                        i.registration_time.day)
                custom_dict["name"] = i.customer_name
                custom_dict["phone"] = i.customer_phone
                custom_dict["work_money"] = i.work_money
                custom_dict["poiname"] = i.poiname
                if len(i.poiaddress) > 25:
                    custom_dict["poiaddress"] = i.poiaddress[6:31] + "..."
                else:
                    custom_dict["poiaddress"] = i.poiaddress[6:]
                custom_dict["order_switch"] = i.order_switch
                try:
                    custom_dict["close_reason"] = close_reason_obj.get(close_reason_id=i.close_reson_id).close_reason
                except models.close_reason.DoesNotExist:
                    pass
                custom_dict["other_close_reason"] = i.other_reason
                custom_dict["order_status"] = order_status_obj.get(order_status_id=i.order_status_id).order_status
                custom_dict["aunt_type"] = aunt_type_obj.get(type_id=i.auntie_type_id).type
                custom_dict["work_time"] = work_time_obj.get(worktime_id=i.type_of_work_id).worktime
                custom_dict["rest_mode"] = rest_mode_obj.get(rest_id=i.rest_mode_id).rest_value

                customer_data.append(custom_dict)
            # print(customer_data)
            return JsonResponse(data={"msg": "获取页面成功", "data": customer_data}, safe=False, status=200)
        else:
            return JsonResponse(data={"msg": "session过期，重新登录"}, safe=False, status=203)

    def post(self, request):
        pass


class Initialize_form(View):
    def get(self, request):
        # session_result = check_session(request)
        # if session_result:
        data = {}
        aunt_info = []
        work_time = []
        assit_work = []
        custom_channel_list = []
        rest_list = []
        aunt_obj = models.auntie_type.objects.all()
        work_time_obj = models.work_time.objects.all()
        assit_work_obj = models.assist_work.objects.all()
        custom_channel_obj = models.customer_channel.objects.all()
        rest_obj = models.rest_mode.objects.all()
        for i in aunt_obj:
            aunt_json = {}
            aunt_json["value"] = i.type_id
            aunt_json["text"] = i.type
            aunt_info.append(aunt_json)

        for j in work_time_obj:
            work_time_json = {}
            work_time_json["value"] = j.worktime_id
            work_time_json["text"] = j.worktime
            work_time.append(work_time_json)

        for k in assit_work_obj:
            assit_work_json = {}
            assit_work_json["value"] = k.assist_work_id
            assit_work_json["text"] = k.assist_work
            assit_work.append(assit_work_json)

        for l in custom_channel_obj:
            custom_channel_json = {}
            custom_channel_json["value"] = l.customer_id
            custom_channel_json["text"] = l.customer_channel
            custom_channel_list.append(custom_channel_json)

        for m in rest_obj:
            rest_json = {}
            rest_json["value"] = m.rest_id
            rest_json["text"] = m.rest
            rest_list.append(rest_json)

        data["aunt_info"] = aunt_info
        data["work_time"] = work_time
        data["assit_work"] = assit_work
        data["custom_channel"] = custom_channel_list
        data["rest_mode"] = rest_list

        return JsonResponse(data={"msg": "成功", "data": data}, safe=False, status=200)
        # else:
        #     return JsonResponse(data={"msg": "session过期，重新登录"}, safe=False, status=203)

    def post(self, request):
        pass


class put_custom(View):
    def get(self, request):
        pass

    def post(self, request):
        session_result = check_session(request)
        if session_result:
            uname = session_result
            form_data = json.loads(request.POST.get("formdata"))
            complete_address = json.loads(request.POST.get("complete_address"))
            customer_information_obj = models.customer_information.objects
            user_obj = models.user_info.objects
            user_id = user_obj.get(user_name=uname)
            print(form_data)
            # print(complete_address)
            if "start_time" not in form_data:
                form_data["start_time"] = ""
                form_data["end_time"] = ""
            if "other_work" not in form_data:
                form_data["other_work"] = ""
            if "wx_num" not in form_data:
                form_data["wx_num"] = ""
            if "assist_work" not in form_data:
                form_data["assist_work"] = ""
            if "detailed_address" not in form_data:
                form_data["detailed_address"] = ""
            # Sql没写完，继续写录入时间
            return_customer = customer_information_obj.create(customer_name=form_data["user_name"],
                                                              customer_phone=form_data["phone"],
                                                              cityname=complete_address["cityname"],
                                                              latlng_lat=complete_address["latlng"]["lat"],
                                                              latlng_lng=complete_address["latlng"]["lng"],
                                                              poiaddress=complete_address["poiaddress"],
                                                              poiname=complete_address["poiname"],
                                                              detailed_address=form_data["detailed_address"],
                                                              work_money=form_data["work_money"],
                                                              family_size=form_data["family_size"],
                                                              other_work=form_data["other_work"],
                                                              work_start_time=form_data["start_time"],
                                                              work_end_time=form_data["end_time"],
                                                              wx_num=form_data["wx_num"],
                                                              registrant="admin", registration_time=registration_time(),
                                                              assist_work_id=form_data["assist_work"],
                                                              auntie_type_id=form_data["defult_order"],
                                                              order_status_id=1,
                                                              type_of_work_id=form_data["type_of_work"],
                                                              rest_mode_id=form_data["rest_mode"],
                                                              customer_qudao_id=form_data["customer_channel"]

                                                              )
            print(return_customer, type(return_customer))
            user_id.customer_information_set.add(return_customer)

            return JsonResponse(data={"msg": "成功"}, safe=False, status=200)
        else:
            return JsonResponse(data={"msg": "session过期，重新登录"}, safe=False, status=203)


class session_check(View):
    def get(self, request):
        session_result = check_session(request)
        if session_result:

            return JsonResponse(data={"msg": "session获取成功"}, safe=False, status=200)
        else:
            return JsonResponse(data={"msg": "session过期，重新登录"}, safe=False, status=203)

    def post(self, request):
        pass


class close_reason(View):
    def get(self, request):
        session_result = check_session(request)
        if session_result:
            return_reason = []
            reason_queryset = models.close_reason.objects.all()
            for i in reason_queryset:
                if i.close_reason == "老单换人":
                    continue
                data = {}
                data["value"] = i.close_reason_id
                data["text"] = i.close_reason
                return_reason.append(data)
            return JsonResponse(data={"msg": "成功", "data": return_reason}, safe=False, status=200)
        else:

            return JsonResponse(data={"msg": "session过期，重新登录"}, safe=False, status=203)

    def post(self, request):
        pass


class put_close_reason(View):
    def get(self, request):
        pass

    def post(self, request):
        user_name = request.session.get("user_name")
        card_id = request.POST.get("card_id")
        chose_data = json.loads(request.POST.get("chose_data"))
        switch_type = request.POST.get("switch_type")
        print(user_name, chose_data, card_id)
        user_obj = models.user_info.objects
        customer_obj = models.customer_information.objects
        customer_info = user_obj.get(user_name=user_name).customer_information_set.get(customer_id=card_id)
        if "other_reason" not in chose_data:
            chose_data["other_reason"] = ""
        customer_info.close_reson_id = chose_data["defult_chose"]
        customer_info.other_reason = chose_data["other_reason"]
        customer_info.order_switch = False
        customer_info.save()
        return JsonResponse(data={"msg": "成功"}, safe=False, status=200)


class reopen(View):
    def get(self, request):
        pass

    def post(self, request):
        user_name = request.session.get("user_name")
        card_id = request.POST.get("card_id")
        user_obj = models.user_info.objects
        order_status_obj = models.order_status.objects
        customer_obj = models.customer_information.objects
        customer_info = user_obj.get(user_name=user_name).customer_information_set.get(customer_id=card_id)
        customer_info.order_switch = True
        customer_info.order_status_id = 2
        customer_info.other_reason = ""
        customer_info.close_reson_id = 7
        return_data = {}
        order_text = order_status_obj.get(order_status_id=2).order_status
        customer_info.save()
        return_data["order_text"] = order_text
        return_data["close_reason"] = "老单换人"

        return JsonResponse(safe=False, data=return_data, status=200)


class head_end_content(View):
    def get(self, request):
        user_name = request.session.get("user_name")
        user_obj = models.user_info.objects
        head_obj = models.head_tail.objects
        head_content = head_obj.get(user_id=user_obj.get(user_name=user_name).user_id)
        data = {}
        data["head_value"] = head_content.head_value
        data["end_value"] = head_content.end_value
        return JsonResponse(safe=False, data=data, status=200)

    def post(self, request):
        print(request.POST)
        user_name = request.session.get("user_name")
        head_word = request.POST.get("head_word")
        end_word = request.POST.get("end_word")
        user_obj = models.user_info.objects
        user_info = user_obj.get(user_name=user_name).user_id
        user_asdas = 2
        head_content_obj = models.head_tail.objects
        try:
            head_content = head_content_obj.get(user_id=user_info)
            head_content.head_value = str(head_word)
            head_content.end_value = str(end_word)
            head_content.registration_time = registration_time()
            head_content.save()
        except:
            head_content_obj.create(head_value=str(head_word), end_value=str(end_word),
                                    registration_time=registration_time(),
                                    registrant="admin", user_id=user_info)
        return JsonResponse(safe=False, data={"msg": "成功"}, status=200)


class generate_order(View):
    def get(self, request):
        pass

    def post(self, request):
        count = 0
        separator = "[玫瑰]"
        order_data = ""
        uname = request.session["user_name"]
        carry_head = request.POST.get("carry_head_end")  # 是否携带头部
        generate_order_type = request.POST.get("generate_order_type")   # 类型
        customer_info = models.customer_information.objects.filter(order_switch=True).order_by("-customer_id")
        rest_mode_obj = models.rest_mode.objects
        work_time_obj = models.work_time.objects
        aunt_type_obj = models.auntie_type.objects
        head_obj = models.head_tail.objects
        user_obj = models.user_info.objects
        head_content = head_obj.get(user_id=user_obj.get(user_name=uname).user_id)
        if int(generate_order_type) == 0:
            order_count = request.POST.get("order_count")  # 生成几条
        else:
            order_count = len(customer_info)
        for i in customer_info:
            poiadress = i.poiaddress.split("市")[1]
            try:
                address = re.search(".*?[0-9a-zA-Z]", poiadress).group()[:-1]
            except:
                address = poiadress
            work_time = work_time_obj.get(worktime_id=i.type_of_work_id).worktime
            if work_time == "白班":
                work_time = "早{}晚{}".format(i.work_start_time, i.work_end_time)
                pass
            count += 1
            if count > int(order_count):
                break
            else:
                order_str = "{count}、{separator}{poiname}({poiaddress})".format(count=i.customer_id, separator=separator,
                                                                                poiname=i.poiname,
                                                                                poiaddress=address, ) + "\n" + "{aunt_type},{work_money}元/{rest_mode}天,{work_time}".format(
                    aunt_type=aunt_type_obj.get(type_id=i.auntie_type_id).type, work_money=i.work_money,
                    rest_mode=rest_mode_obj.get(rest_id=i.rest_mode_id).rest_value,
                    work_time=work_time, ) + "\n" + "{scop_of_work},{other_work}".format(
                    scop_of_work=aunt_type_obj.get(type_id=i.auntie_type_id).scope_of_work,
                    other_work=i.other_work
                ) + "\n"
                order_data = order_data + order_str + "\n"
        if int(carry_head) == 0:
            order_data = head_content.head_value + "\n""\n" + order_data + head_content.end_value

        return JsonResponse(safe=False, data={"msg": "成功", "data": order_data}, status=200)

# class put_custom(View):
#     def get(self, request):
#         session_result = check_session(request)
#         if session_result:
#             return JsonResponse(data={"msg": "获取页面成功"}, safe=False, status=200)
#         else:
#             return JsonResponse(data={"msg": "session过期，重新登录"}, safe=False, status=203)
#
#     def post(self, request):
#         pass
