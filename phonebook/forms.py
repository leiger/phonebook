from django import forms
from django.utils.translation import ugettext as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=30,
                               widget=forms.TextInput(attrs={'id': 'username', 'class': 'form-control', 'placeholder': _('姓名'),
                                                             'required': '', 'tabindex': 1, 'autofocus': '1'}))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'id': 'password', 'class': 'form-control',
                                                                                      'placeholder': _('密码'),
                                                                                      'required': '', 'tabindex': 2}))


class ContactForm(forms.Form):
    name = forms.CharField(label=_("name"), max_length=100,
                                widget=forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'required': '', 'tabindex': 1,
                                                              'placeholder': _('请输入姓名'), 'autofocus': '1'}))
    company = forms.CharField(label=_("company"), max_length=100, required=False,
                               widget=forms.TextInput(attrs={'id': 'company', 'placeholder': _('公司'),
                                                             'class': 'form-control', 'tabindex': 2}))
    position = forms.CharField(label=_("position"), max_length=100, required=False,
                             widget=forms.TextInput(attrs={'id': 'position', 'class': 'form-control',
                                                            'placeholder': _('职位'), 'tabindex': 3}))
    phoneType = forms.CharField(label=_("phoneType"), max_length=100, required=False,
                            widget=forms.TextInput(attrs={'id': 'phone', 'required': '', 'tabindex': 4, 'name': 'phoneType',
                                                          'list': 'phoneType', 'value': _('手机')}))
    phone = forms.CharField(label=_("Phone"), max_length=100,
                            widget=forms.NumberInput(attrs={'id': 'phone', 'required': '', 'tabindex': 5}))
    emailType = forms.CharField(label=_("emailType"), max_length=100, required=False,
                               widget=forms.TextInput(attrs={'id': 'email', 'tabindex': 6, 'name': 'emailType',
                                                             'list': 'emailType', 'value': _('个人')}))
    email = forms.EmailField(label=_("email"), max_length=100, required=False,
                               widget=forms.EmailInput(attrs={'id': 'email', 'tabindex': 7}))
    socialType = forms.CharField(label=_("socialType"), max_length=100, required=False,
                               widget=forms.TextInput(attrs={'id': 'social', 'tabindex': 8, 'name': 'socialType',
                                                             'list': 'socialType', 'value': _('QQ')}))
    social = forms.CharField(label=_("social"), max_length=100, required=False,
                               widget=forms.TextInput(attrs={'id': 'social', 'tabindex': 9}))
    remark = forms.CharField(label=_("remark"), max_length=100, required=False,
                               widget=forms.TextInput(attrs={'id': 'remark', 'tabindex': 10}))


class SearchForm(forms.Form):
    query = forms.CharField(label=_('Query'), max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control system-search', 'required': '',
                                                          'tabindex': 1, 'placeholder': _('搜索联系人')}))