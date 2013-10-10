# -*- coding: utf-8 -*-

from django.contrib import admin
from books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    search_fields = ('name', 'address', 'city', 'country')

class BookAdmin(admin.ModelAdmin):
    # 查看时显示的列
    list_display = ('title', 'publisher', 'publication_date')
    # 搜索框
    search_fields = ('title', 'publisher')
    # 右侧过滤器选项
    list_filter = ('publication_date',)
    # 2013   2013 9 那一栏过滤
    date_hierarchy = 'publication_date'
    # 逆向排序
    ordering = ('-publication_date',)
    # fields = ('title', 'authors', 'publisher')
    # 使得Authors修改变为JavaScript过滤器
    filter_horizontal = ('authors',)
    # 使publisher这一栏变为文本框而不是下拉栏
    # raw_id_fields = ('publisher',)

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)