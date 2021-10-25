# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import random

import frappe
from frappe import _
from frappe.utils import nowdate, get_datetime


@frappe.whitelist()
def get_questions():
    fields_dt = ['name', 'category', 'key', 'text']
    questions = frappe.db.get_list('Big Five Factor Model',
                                   fields=fields_dt)

    # Ordenamiendo random: se aplica sobre el objeto original
    suffle_data = random.shuffle(questions)

    return questions


@frappe.whitelist()
def complete_test(data):
    try:
        res = json.loads(data)
        # DEBUG:
        # with open('respuestas.json', 'w') as f:
        #     f.write(json.dumps(res, indent=2))

        total_questions = len(res.get('extraversion')) + len(res.get('agreeableness')) + len(res.get('conscientiousness')) + \
            len(res.get('neuroticism')) + len(res.get('openness'))

        # Deben completarse las 100 preguntar para completar el proceso
        if total_questions != 100:
            frappe.msgprint(msg=_(f'{total_questions} {_("de")} 100 {_("fueron respondidas, por favor responda todas las preguntas y presione completar")}'),
                            title=_('Process not completed'), indicator='yellow')
            return False, 'Not Completed'

        results = {
            'total_extraversion': sum(x['value'] for x in res.get('extraversion')),  # extraversión
            'total_agreeableness': sum(x['value'] for x in res.get('agreeableness')),  # simpatía
            'total_conscientiousness': sum(x['value'] for x in res.get('conscientiousness')),  # concienciación
            'total_neuroticism': sum(x['value'] for x in res.get('neuroticism')),  # neuroticismo
            'total_openness': sum(x['value'] for x in res.get('openness')),  # apertura
            'user': frappe.db.get_value('User', {'name': frappe.session.user}, 'full_name'),
            'datetimetest': str(get_datetime())
        }

        # DATOS PRUEBA
        # results = {
        #     'total_extraversion': 62,  # extraversión
        #     'total_agreeableness': 56,  # simpatía
        #     'total_conscientiousness': 63,  # concienciación
        #     'total_neuroticism': 57,  # neuroticismo
        #     'total_openness': 63,  # apertura
        #     'user': frappe.db.get_value('User', {'name': frappe.session.user}, 'full_name'),
        #     'datetimetest': str(get_datetime())
        # }

        # Se registran los resultados
        doc = frappe.get_doc({
            'doctype': 'Big Five Results',
            'completed_by': frappe.session.user,
            'date_time': results.get('datetimetest'),
            'results': [
                {'category': 'EXTRAVERSION', 'score': results.get('total_extraversion')},
                {'category': 'AGREEABLENESS', 'score': results.get('total_agreeableness')},
                {'category': 'CONSCIENTIOUSNESS', 'score': results.get('total_conscientiousness')},
                {'category': 'NEUROTICISM', 'score': results.get('total_neuroticism')},
                {'category': 'OPENNESS', 'score': results.get('total_openness')},
            ],
            'docstatus': 1
        })
        doc.insert(ignore_permissions=True)

        return True, results

    except:
        frappe.msgprint(msg=_(f'Calculo no pudo ser completado, copie o tome una captura de pantalla completo de todo este mensaje, \
            para ayudarlo lo mas pronto posible. \n <hr> <code>{frappe.get_traceback()}</code>'),
                        title=_('Process not completed'), indicator='red')

