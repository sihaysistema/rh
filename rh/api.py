# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import frappe
from frappe import _


@frappe.whitelist()
def get_questions():
    fields_dt = ['name', 'category', 'key', 'text']
    questions = frappe.db.get_list('Big Five Factor Model',
                                   fields=fields_dt)

    # Ordenamiendo random: se aplica sobre el objeto original
    suffle_data = random.shuffle(questions)

    return questions
