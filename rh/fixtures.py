# -*- coding: utf-8 -*-
#  Si Hay Sistema and Contributors 2021
from __future__ import unicode_literals


def fill_fixtures():
    fixtures_fillup = []

    custom_fields = {
        "dt": "Custom Field", "filters": [
            [
                "name", "in", []
            ]
        ]
    }

    translation = {
        "dt": "Translation", "filters": [
            [
                "source_text", "in", []
            ]
        ]
    }

    big_five_factor_model = {
        "dt": "Big Five Factor Model"
    }

    # fixtures_fillup.append(custom_fields)
    # fixtures_fillup.append(translation)
    fixtures_fillup.append(big_five_factor_model)

    return fixtures_fillup
