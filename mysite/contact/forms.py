# -*- coding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    # subject = forms.CharField(min_length=100)
    # 每一个字段都默认是必填。
    # 要使email成为可选项，
    # 我们需要指定required=False
    email = forms.EmailField(required = False, label='Your e-mail address')
    # message = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

# 以下校检只是用于用空格分隔单词的英文输入
#
# Django的form系统自动寻找匹配的函数方法，
# 该方法名称以clean_开头，并以字段名称结束。 
# 如果有这样的方法，它将在校验时被调用
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            # 抛出forms.ValidationError型异常。
            # 这个异常的描述会被作为错误列表中的一项显示给用户。
            raise forms.ValidationError('Not enough words!')
        return message
# 在函数的末尾显式地返回字段的值非常重要。 
# 我们可以在我们自定义的校验方法中修改它的值
# （或者把它转换成另一种Python类型）。
#  如果我们忘记了这一步，
# None值就会返回，原始的数据就丢失掉了。