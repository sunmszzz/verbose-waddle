from django.shortcuts import render
from django.views.generic import View
from app01 import models
from django.http import HttpResponse, JsonResponse
# Create your views here.


class Mac(View):

    def get(self, request):
        pass

    def post(self, request, *args, **kwargs):
        def is_chinese(word):
            for ch in word:
                if '\u4e00' <= ch <= '\u9fff':
                    return True
            return False

        def is_seventeen(word):
            if len(word) == 17:
                return True
            return False

        ret = {'code1': 1000, 'msg': None}
        name = request.POST.get('name')
        mac = request.POST.get('mac')
        print(name, mac)
        obj = models.Mac.objects.filter(name=name, mac=mac).first()
        if is_chinese(name) and is_seventeen(mac):
            if obj:
                ret['code1'] = 4000
                ret['msg'] = "Have registered"
            else:
                ret['code1'] = 2000
                ret['msg'] = "Registration successful"
                # 存进数据库，有就更新，没有就添加
                models.Mac.objects.update_or_create(name=name, defaults={'mac': mac})
        else:
            ret['code1'] = 8000
            ret['msg'] = "Illegal"

        return JsonResponse(ret)
