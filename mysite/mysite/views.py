# -*- coding: utf-8 -*-
# 
# from django.template.loader import get_template
# from django.template import Context
from django.shortcuts import render_to_response,render
from django.http import Http404
from django.http import HttpResponse
import datetime

def my_homepage_view(request):
    return render(request, 'homepage.html')

def hello(request):
    name = 'Isis'
    return render(request, 'hello.html', {'name': name})
    # return HttpResponse("Hello world!")
    # return HttpResponse('Welcome to the page at %s!' % request.path )
    # return HttpResponse('Welcome to the page at %s!' % request.get_host() )
    # return HttpResponse('Welcome to the page at %s!' % request.get_full_path() )
    # return HttpResponse('Welcome to the page at %s!' % request.is_secure() ) #HTTPS访问为True

# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template("current_datetime.html")
#     html = t.render(Context({"current_date": now}))
#     return HttpResponse(html)
def current_datetime(request):
    # now = datetime.datetime.now()
    # return render_to_response("current_datetime.html", {"current_date": now})
    current_date = datetime.datetime.now()
    return render_to_response("dateapp/current_datetime.html", locals())

# def hours_ahead(request, offset):
#     try:
#         offset = int(offset)
#     except ValueError:
#         raise Http404()
#     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#     # assert False
#     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
#     return HttpResponse(html)
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # c = Context({"offset": offset, "dt": dt})
    return render_to_response("dateapp/hours_ahead.html", {"offset": offset, "dt": dt})
    # return render_to_response("hours_ahead.html", c)


# def ua_display_good1(request):
#     try:
#         ua = request.META['HTTP_USER_AGENT']
#     except KeyError:
#         ua = 'unknown'
#     return HttpResponse('Your browser is %s.' % ua)

# def ua_display_good2(request):
#     ua = request.META.get('HTTP_USER_AGENT','unknown')
#     return HttpResponse('Your browser is %s.' % ua)

# request.META 是一个Python字典，
# 包含了所有本次HTTP请求的Header信息
def model_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('dateapp/meta.html', {'all_meta':values})

def foobar_view(request, url, template_name):
    return render(request, template_name, {'url':url, 'template_name':template_name}) 


# 使用缺省视图参数
# 设置默认参数值是字符串,不是整数
def mydata(request, month='Aug', day='27'):
    return render(request, 'mydata.html', {'month':month, 'day':day})

def add_stage(request, app_label, model_name):
    # 不优雅： 因为它把URL逻辑放在了视图中
    # if app_label == 'auth' and model_name == 'user':
    #     # do something
    # else:
    #     # do something
    return HttpResponse('Special URLs: \n add_stage')

def user_add_stage(request):
    return HttpResponse('User Add Stage!')

def my_image(request):
    image_data = open('D:/Python/DjangoBook/djcode/mysite/static/08.jpg', 'rb').read()
    return HttpResponse(image_data, mimetype = 'image/jpg')






# -----------------------------------------------------------------------
# def method_splitter(request, GET=None, POST=None):
#     if request.method == 'GET' and GET is not None:
#         return GET(request)
#     elif request.method == 'POST' and POST is not None:
#         return POST(request)
#     raise Http404

# def method_splitter(request, *args, **kwargs):
#     get_view = kwargs.pop('GET', None)
#     post_view = kwargs.pop('POST', None)
#     if request.method == 'GET' and get_view is not None:
#         return get_view(request, *args, **kwargs)
#     elif request.method == 'POST' and post_view is not None:
#         return post_view(request, *args, **kwargs)
#     raise Http404

# def some_page_get(request):
#     assert request.method == 'GET'
#     return render(request, 'page.html')

# def some_page_post(request):
#     assert request.method == 'POST'
#     return HttpResponseRedirect('/someurl/')

# ------------------------------------------------------------------------------
