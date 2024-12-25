"""
Product Table Editor
"""
from django import forms
from unfold.contrib.forms.widgets import WysiwygWidget

from apps.shop import models


class Product(forms.ModelForm):
    class Meta:
        model = models.Product
        widgets = {
            "description": WysiwygWidget(),
        }
        fields = "__all__"
