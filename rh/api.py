# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import random

import frappe
from frappe import _
from frappe.utils import nowdate, get_datetime, cint


@frappe.whitelist()
def get_questions():
    """Retorna las preguntas de BIG5"""
    fields_dt = ['name', 'category', 'key', 'text']
    questions = frappe.db.get_list('Big Five Factor Model',
                                   fields=fields_dt)

    # Ordenamiendo random: se aplica sobre el objeto original
    suffle_data = random.shuffle(questions)

    return questions


@frappe.whitelist()
def complete_test(data):
    """Endpoint para calcular los resultados BIG5, los resultados se guardan en `Big Five Results`
    y buscar que perfil de personalidad se adecua a los resultados"""
    try:
        res = json.loads(data)
        # DEBUG:
        # with open('respuestas.json', 'w') as f:
        #     f.write(json.dumps(res, indent=2))

        # Debe ser 100
        total_questions = len(res.get('extraversion')) + len(res.get('agreeableness')) + len(res.get('conscientiousness')) + \
            len(res.get('neuroticism')) + len(res.get('openness'))

        # Deben completarse las 100 preguntar para completar el proceso
        if total_questions != 100:
            return False, f'{total_questions} {_("de")} 100 {_("fueron respondidas, por favor responda todas las preguntas y presione completar")}'

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

        # Los resultados se asignan a variables, para no repetir el acceso al dict origen
        res_extraversion = cint(res.get('total_extraversion'))
        res_agreeableness = cint(res.get('total_agreeableness'))
        res_conscientiousness = cint(res.get('total_conscientiousness'))
        res_neuroticism = cint(res.get('total_neuroticism'))
        res_openness = cint(res.get('total_openness'))

        # Los resultados se comparan con los perfiles de personalidad ya establecidos en ERP para obtener el que mejor
        # que se adapte a la persona. NOTA: pueden ser varios estos se guardaran en una tabla hija de `Big Five Results`
        query_str = f"""SELECT PF.name AS profile
        FROM `tabPersonality Profile` AS PF
        WHERE
        ({res_openness} >= PF.minimum_result_for_openness AND {res_openness} <= PF.maximun_result_for_openness) AND
        ({res_neuroticism} >= PF.minimum_result_for_neuroticism AND {res_neuroticism} <= PF.maximun_result_for_neuroticism) AND
        ({res_agreeableness} >= PF.minimum_result_for_agreeableness AND {res_agreeableness} <= PF.maximun_result_for_agreeableness) AND
        ({res_conscientiousness} >= PF.minimum_result_for_conscientiousness AND {res_conscientiousness} <= PF.maximun_result_for_conscientiousness) AND
        ({res_extraversion} >= PF.minimum_result_for_extraversion AND {res_extraversion} <= PF.maximum_result_for_extraversion);"""

        ok_profiles = frappe.db.sql(query_str, as_dict=True)
        # DEBUG:
        # with open('ok_profiles_b5.json', 'w') as f:
        #     f.write(json.dumps(ok_profiles, indent=2))

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
            'recommended_profiles': ok_profiles,
            'docstatus': 1
        })
        doc.insert(ignore_permissions=True)

        return True, results

    except:
        frappe.msgprint(msg=_(f'Calculo no pudo ser completado, copie o tome una captura de pantalla completo de todo este mensaje, \
            para ayudarlo lo mas pronto posible. \n <hr> <code>{frappe.get_traceback()}</code>'),
                        title=_('Process not completed'), indicator='red')

