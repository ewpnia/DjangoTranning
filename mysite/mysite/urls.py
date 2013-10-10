# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
# from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('mysite.views',
    url(r'^$', 'my_homepage_view'), 
    url(r'^hello/$', 'hello'), 
    url(r'^time/$', 'current_datetime'),
    url(r'^another_time/$', 'current_datetime'),
    # (r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    url(r'^time/plus/(?P<offset>\d{1,2})/$', 'hours_ahead'),
    url(r'^meta/$', 'model_meta'),

    # 使用（）传入URL的值
    url(r'^(foo)/$', 'foobar_view', {'template_name':'template1.html'}),
    url(r'^(bar)/$', 'foobar_view', {'template_name':'template2.html'}),

    # 使用缺省视图参数
    url(r'^mydata/$', 'mydata'),
    url(r'^mydata/birthday/$', 'mydata', {'month':'Oct', 'day':'05'}),
    url(r'^mydata/(?P<month>\w{3})/(?P<day>\d{1,2})/$','mydata'),

    # /auth/user/add/ 的请求将会
    # 被 user_add_stage 视图处理。 
    # 尽管URL也匹配第二种模式，
    # 它会先匹配上面的模式。
    # （这是短路逻辑。）
    url('^auth/user/add/$', 'user_add_stage'),
    # [^/]表示非/以外的字符
    # +表示任意长度的字符
    # 这将匹配像 /myblog/entries/add/ 
    # 和 /auth/groups/add/ 这样的URL 
    url('^([^/]+)/([^/]+)/add/$', 'add_stage'),

    url(r'^myimage/$', 'my_image'),

    # (r'^somepage/$', 'method_splitter', {'GET':some_page_get, 'POST':some_page_post}),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('books.views',
    url(r'^search/$', 'search' ),
    # (r'^search_form/$', 'search_form'),
)


urlpatterns += patterns('contact.views',
    url(r'^contact/$', 'contact'),
    url(r'^contact/thanks/$', 'thanks'),
)


from books.views import PublisherList

urlpatterns += patterns('',
    url(r'^publishers/$', PublisherList.as_view()),
)

# from books.views import AuthorDetailView

# urlpatterns = patterns('',
#     url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(),
#         name = 'author-detail'),
# )


# 通用视图
# from django.views.generic import TemplateView
# urlpatterns += patterns('',
#     (r'^about/$', TemplateView.as_view(template_name = 'about.html')),
#     )

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         (r'^debuginfo/$', 'mysite.views.debug'),
#     )



# ----------------------------------------------------------------------
# 在任何时候，你的URLconf都可以
# 包含其他URLconf模块
# from django.conf.urls.defaults import *

# urlpatterns = patterns('',
#     (r'^weblog/', include('mysite.blog.urls')),
#     (r'^photos/', include('mysite.photos.urls')),
#     (r'^about/$', 'mysite.views.about'),
# )
# 这里有个很重要的地方： 例子中的指向 include() 
# 的正则表达式并 不 包含一个 $ （字符串结尾匹配符），
# 但是包含了一个斜杆。 每当Django遇到 include() 时，
# 它将截断匹配的URL，
# 并把剩余的字符串发往包含的URLconf作进一步处理。

# 这里就是被包含的URLconf mysite.blog.urls ：

# from django.conf.urls.defaults import *

# urlpatterns = patterns('',
#     (r'^(\d\d\d\d)/$', 'mysite.blog.views.year_detail'),
#     (r'^(\d\d\d\d)/(\d\d)/$', 'mysite.blog.views.month_detail'),
# )

# /weblog/2007/ ：在第一个URLconf中，
# 模式 r'^weblog/' 被匹配。 因为它是一个 include() ，
# Django将截掉所有匹配的文本，在这里是 'weblog/' 。
# URL剩余的部分是 2007/ ， 将在 mysite.blog.urls 
# 这个URLconf的第一行中被匹配到。 
# URL仍存在的部分为 2007/ ,
# 与第一行的 mysite.blog.urlsURL设置相匹配。


# ---------------------------------------------------------------------------------




# -----------------------------------------------------------------------------
# 一个被包含的URLconf接收
# 任何来自parent URLconfs的被捕获的参数
# 
# root urls.py
# 
# from django.conf.urls.defaults import *
# 
# urlpatterns = patterns('',
#     (r'^(?P<username>\w+)/blog/', include('foo.urls.blog')),
# )
# 
# foo/urls/blog.py
# 
# from django.conf.urls.defaults import *
# 
# urlpatterns = patterns('',
#     (r'^$', 'foo.views.blog_index'),
#     (r'^archive/$', 'foo.views.blog_archive'),
# )
# 
# 在这个例子中，
# 被捕获的 username 变量将传递给被包含的 URLconf，
# 进而传递给那个URLconf中的 每一个 视图函数。
# 
# 注意，这个被捕获的参数总是 
# 传递到被包含的URLconf中的每一行，
# 不管那些行对应的视图是否需要这些参数。 
# -----------------------------------------------------------------------------------






# ----------------------------------------------------------------------------
# # from django.conf.urls import patterns, include, url
# # from mysite.views import model_meta
# # from mysite.views import *

# from django.conf.urls import *
# from mysite import views
# import books.views
# import contact.views

# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     (r'^$', views.my_homepage_view), # http://127.0.0.1:8000/
#     (r'^hello/$', views.hello), # http://127.0.0.1:8000/hello/
#     (r'^time/$', views.current_datetime),
#     (r'^another_time/$', views.current_datetime),
#     # (r"^time/plus/(\d+)/$", views.hours_ahead),
#     # "正则表达式也是用圆括号来从文本里 提取 数据的"。 
#     # urls文件中的(r'^time/plus/(\d{1,2})/$', 
#     # hours_ahead)语句定义了要传递的参数(\d{1,2})，
#     # 传递给hours_ahead作为其第二个参数，即offset。
    
#     # 若把 (r'^time/plus/(\d{1,2})/$', hours_ahead)
#     # 改成 (r'^time/plus/\d{1,2}/$', hours_ahead) 
#     # 會拋出錯誤，所以是用 "()"來指定要丟給 view.py 的參數。
#     # 多個參數也可以用一樣的方法指定。
#     (r'^time/plus/(\d{1,2})/$', views.hours_ahead),
#     # (r'^ua1/$', ua_display_good1),
#     # (r'^ua2/$', ua_display_good2),
#     (r'^meta/$', views.model_meta),



#     # (r'^search_form/$', views.search_form),
#     # (r'^search/$', books.views.search),

#     # (r'^contact/$', contact.views.contact),
#     # (r'^contact/thanks/$', contact.views.thanks),



#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^mysite/', include('mysite.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# )

# ---------------------------------------------------------------------------------





# -----------------------------------------------------------------------------
# urlpatterns = patterns('',
#     (r'^articles/(\d{4})/$', views.year_archive),
#     (r'^articles/(\d{4})/(\d{2})/$', views.month_archive),
# )

# urlpatterns = patterns('',
#     (r'^articles/(?P<year>\d{4})/$', views.year_archive),
#     (r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
# )

# (?P<name>pattern)

# (r'^tag/(\w+)/$', 'tag'),


# (r'^(foo)/$', views.foobar_view),
# 带括号的正则表达式会传一个变量到后面的函数中
# def foobar_view(request, url):
#     m_list = MyModel.objects.filter(is_new=True)
#     if url == 'foo':
#         template_name = 'template1.html'
#     elif url == 'bar':
#         template_name = 'template2.html'
#     return render_to_response(template_name, {'m_list': m_list})
# ---------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------
# (r'^mydata/(?P<id>\d+)/$', views.my_view, {'id': 3}),
# 这里，正则表达式和额外字典都包含了一个 id 。
# 硬编码的（额外字典的） id 将优先使用。 
# 就是说任何请求（比如， /mydata/2/ 
# 或者 /mydata/432432/ ）都会作 id 设置为 3 对待，
# 不管URL里面能捕捉到什么样的值。
# -------------------------------------------------------------------------------