# -*- coding: utf-8 -*-

# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
# from django.shortcuts import render

# def contact(request):
#     errors = []
#     # 确认request.method的值。
#     # 用户浏览表单时这个值并不存在，
#     # 当且仅当表单被提交时这个值才出现。 
#     if request.method == 'POST':
#         # 使用request.POST.get()方法，
#         # 并提供一个空的字符串作为默认值；
#         # 这个方法很好的解决了键丢失与空数据问题
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             # 我们使用了django.core.mail.send_mail
#             # 函数来发送e-mail。 这个函数有四个必选参数： 
#             # 主题，正文，寄信人和收件人列表。
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     return render(request, 'contact_form.html', {
#         'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', ''),
#         })

from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('Django', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            # 设置初始值
            # initial={'subject':'I love your site!'}
            )
    return render(request, 'contact_form.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html' )