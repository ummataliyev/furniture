"""
Navigation settings.
Icons are: https://fonts.google.com/icons
"""
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = {
    "separator": True,
    "items": [
        {
            "title": _("Категории"),
            "icon": "category",
            "link": reverse_lazy(
                "admin:shop_category_changelist"
            ),
        },
        {
            "title": _("Продукты"),
            "icon": "king_bed",
            "link": reverse_lazy(
                "admin:shop_product_changelist"
            ),
        },
    ],
}

NAVIGATION = [
    PAGES
]
