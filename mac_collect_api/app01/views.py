import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.views.generic import View
from app01 import models
from django.http import HttpResponse, JsonResponse
# Create your views here.
from mac_collect_api import settings


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


class Homework(View):
    def get(self):
        pass

    def post(self, request, *args, **kwargs):
        # 判断本地是否已经存在
        def is_local_file(local_file_dir, get_file_name):
            for root, dirs, files in os.walk(local_file_dir):
                # print('root_dir:', root)  # 当前目录路径
                # print('sub_dirs:', dirs)  # 当前路径下所有子目录
                print('files:', files)  # 当前路径下所有非目录子文件
                local_files = files
            for item in local_files:
                print('本地文件判断：', get_file_name, item)
                if get_file_name == item:
                    return True
            return False

        # 返回的数据
        ret = {'code1': 1000, 'msg': None}
        # 获取提交的data中的数据
        name = request.POST.get('name')
        number = request.POST.get('number')
        file_name = request.POST.get('file_name')
        upload_time = request.POST.get('upload_time')
        # 获取文件
        homework = request.FILES.get('file')
        print('姓名:{},学号:{}\n作业:{} 时间:{}'.format(name, number, homework.name, upload_time))
        # 获取本地目录下的文件名
        local_file_dir = os.path.join(settings.MEDIA_ROOT, upload_time.split(' ')[0])

        obj = models.Homework.objects.filter(name=name, number=number).first()
        # 判断，并赋返回值
        print('提交在20点之前：', upload_time, int(upload_time.split(' ')[-1].split(':')[0]))
        if int(upload_time.split(' ')[-1].split(':')[0]) < 20:
            if obj:
                if is_local_file(local_file_dir, file_name):
                    ret['code1'] = 4000
                    ret['msg'] = "请勿重复上传"
                else:
                    ret['code1'] = 2000
                    ret['msg'] = "上传成功"
                    models.Homework.objects.update_or_create(name=name, number=number, defaults={'is_upload': file_name, 'upload_time': upload_time})
                    # 保存文件
                    tmp_file = os.path.join(settings.MEDIA_ROOT, upload_time.split(' ')[0], homework.name)
                    path = default_storage.save(tmp_file, ContentFile(homework.read()))

                    print('tmp_file: {}'.format(path))
            else:
                ret['code1'] = 8000
                ret['msg'] = "用户不存在"
        else:
            ret['code1'] = 8000
            ret['msg'] = "当前时间不能上传"
        return JsonResponse(ret)