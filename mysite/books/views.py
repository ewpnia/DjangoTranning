# -*- coding: utf-8 -*-

# from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

# def search_form(request):
#     return render_to_response('search_form.html')

def search_form(request):
    return render(request,'search_form.html')

# def search(request):
#     if 'q' in request.GET:
#         if request.GET['q'] == '':
#             message = 'You searched for nothing!'
#         else:
#             message = 'You seached for: %s' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)
# 以上判断可以写成 if request.GET("q")，
# 但 if 'q' in request.GET 可以防止用户直接访问.../search/
# 而不是预想的通过.../search_form/ 跳转并显示结果，较为安全
# 
# 其中，if request.GET("q") 用于获取‘q’这个key
# 对应的的value
# if 'q' in request.GET 用于判断是否存在‘q’这个键
# 
# 在HTML里我们定义了一个变量q。
# 当提交表单时，变量q的值通过GET(method="get")
# 附加在URL /search/上。

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books':books, 'query':q})
    return render(request, 'search_form.html', 
        {'errors': errors})


from django.views.generic import ListView
from books.models import Publisher

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favourite_publishers'


# from django.views.generic import DetailView
# from books.models import Publisher, Book

# class PublisherDetail(DetailView):
#     model = Publisher
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(PublisherDetail, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['book_list'] = Book.objects.all()
#         return context

# from django.views.generic import DetailView
# from django.shortcuts import get_object_or_404
# from django.utils import timezone
# from books.models import Author

# class AuthorDetailView(DetailView):
#     queryset = Author.objects.all()

#     def get_object(self):
#         object = super(AuthorDetailVies, self).get_object()
#         object.last_accessed = timezone.now()
#         object.save()
#         return object