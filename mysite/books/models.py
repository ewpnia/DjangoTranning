# -*- coding: utf-8 -*-
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]
        
    def __unicode__(self):
        return self.name

    

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True,verbose_name = 'e-mail')
    # headshot = models.ImageField(upload_to = 'author_headshots')
    # last_accessed = models.DateTimeField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


# >>> from books.models import Book
# >>> Book.objects.title_count('django')
# class BookManager(models.Manager):
#     def title_count(self, keyword):
#         # 此处self指manager本身
#         return self.filter(title__icontains=keyword).count()

# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(authors='1')


class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank = True, null = True)
    num_pages = models.IntegerField(blank = True, null = True)
    # 取代模型的默认manager（objects）
    # objects = BookManager()

    # Then hook it into the Book model explicitly
    # Book.objects.all()返回了数据库中的所有书本
    # 而Book.dahl_objects.all()只返回了一本
    objects = models.Manager() # The default manager.
    dahl_objects = DahlBookManager() # The Dahl-specific manager

    def __unicode__(self):
        return self.title

# -----------------------------------------------------------------------------------------
# 通用过滤器
# 这个例子允许你执行Person.men.all() ，
#  Person.women.all()，Person.people.all()查询，
# 生成你想要的结果。
# 
# 
# class MaleManager(models.Manager):
#     def get_query_set(self):
#         return super(MaleManager, self).get_query_set().filter(sex='M')

# class FemaleManager(models.Manager):
#     def get_query_set(self):
#         return super(FemaleManager, self).get_query_set().filter(sex='F')

# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
#     people = models.Manager()
#     men = MaleManager()
#     women = FemaleManager()
#     
#     
# Django遇到的第一个Manager
# (以它在模型中被定义的位置为准)
# 会有一个特殊状态。 
# Django将会把第一个Manager 定义为默认Manager 
# -------------------------------------------------------------------------------------------