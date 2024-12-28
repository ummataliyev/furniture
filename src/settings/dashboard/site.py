"""
the basic admin interface.
"""
from django.utils.translation import gettext_lazy as _

SITE = {
    "SITE_TITLE": _("Aрзон Мебеллар"),
    "SITE_HEADER": _("Aрзон Мебеллар"),
    "SHOW_HISTORY": True,
    "SITE_SYMBOL": "shelves",
    "COLORS": {
        "primary": {
            "50": "220 255 230",
            "100": "190 255 200",
            "200": "160 255 170",
            "300": "130 255 140",
            "400": "100 255 110",
            "500": "70 255 80",
            "600": "50 225 70",
            "700": "40 195 60",
            "800": "30 165 50",
            "900": "20 135 40",
            "950": "10 105 30",
        },
    },
}
