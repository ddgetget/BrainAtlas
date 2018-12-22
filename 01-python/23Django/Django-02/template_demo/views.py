from _datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import View


# /temp//use_template/
class TemplateView(View):
    def get(self, request):

        # 使用temo.html模板文件
        # render方法是一个简写的函数
        # context = {
        #     'name': 'turing'
        # }
        # return render(request, 'demo.html', context)
        # 下面的是前后段不分离的形式，就是把前段的大妈复制到服务器，然后在送到前段
        # 1. 加载模板(指定所要使用的模板)，获取模板对象
        temp = loader.get_template('hello.html')
        # 2. 模板渲染（给模板文件传递数据，将模板文件中的变量进行替换，返回替换之后html页面）-
        context = {
            'content': 'hello',
            'city': '北京',
            'adict': {
                'name': '西游记',
                'author': '吴承恩'
            },
            'alist': [1, 2, 3, 4, 5],
            'now_date': datetime.now()
        }

        res_html = temp.render(context)
        print(res_html)

        # 3. 返回应答
        return HttpResponse(res_html)
