from django.shortcuts import render
from django.views.generic import View
from app01 import models
# Create your views here.


class Mac(View):
    def get(self, request):
        pass

    def post(self, request, *args, **kwargs):
        ret = {'code1': 1000, 'msg': None}
        name = request.POST.get('name')
        mac = request.POST.get('mac')
        print(name, mac)
        obj = models.Mac.objects.filter(name=name).first()
        if obj:
            ret['code1'] = 4000
            ret['msg'] = "已登记"

        else:
            # 为用户创建token
            ret['code1'] = 2000
            ret['msg'] = "登记成功"
            # 存进数据库，有就更新，没有就添加
            models.Mac.objects.update_or_create(name=name, mac=mac)

        return ret

