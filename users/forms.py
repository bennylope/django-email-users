# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import (UserCreationForm as BaseCreationForm,
        UserChangeForm as BaseChangeForm)
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserCreationForm(BaseCreationForm):

    error_messages = {
        'duplicate_email': _("A user with that email address already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')

    def clean_email(self):
        # Since User.email is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )


class UserChangeForm(BaseChangeForm):

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields.pop('username')
