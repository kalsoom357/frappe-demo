# Copyright (c) 2023, kalsoom and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}
    columns, data = [], []
    conditions = get_conditions(filters)
    columns = get_columns()
    data = get_data(filters, conditions)
    return columns, data

def get_conditions(filters):
    conds = ""
    conds += " and DATE(si.posting_date) between %(from_date)s and %(to_date)s " if filters.get("from_date") and filters.get("to_date") else ""
    return conds

def get_data(filters, conditions):
    data = frappe.db.sql(f"""
       SELECT
        si.name,
		sii.description,
		sii.qty AS QTY,
		sii.total_weight AS weight,
		(sii.qty * sii.rate) AS gross,
		(sii.qty * sii.rate - si.discount_amount) AS net_sales
		FROM
		`tabSales Invoice` AS si
		JOIN
		`tabSales Invoice Item` AS sii
		ON
			si.name = sii.parent
			{conditions}
		ORDER BY
			net_sales DESC;
			
    """, filters, as_dict=1)

    return data

def get_columns():
    columns = [
        {
             'fieldname': 'name',
            'label': _('ID'),
            'fieldtype': 'Link',
            'options': 'Sales Invoice',
            'width': 200
        },
        {
            'fieldname': 'description',
            'label': _('Description'),
            'fieldtype': 'Data',
            'width': 150
        },
        {
            'fieldname': 'QTY',
            'label': _('Quantity'),
            'fieldtype': 'Float',
            'width': 100
        },
        {
            'fieldname': 'weight',
            'label': _('Weight'),
            'fieldtype': 'Currency',
            'options': 'currency',
            'width': 100
        },
        {
            'fieldname': 'net_sales',
            'label': _('Net Sales'),
            'fieldtype': 'Currency',
            'options': 'currency',
            'width': 120
        },
        {
            'fieldname': 'gross',
            'label': _('Gross'),
            'fieldtype': 'Currency',
            'options': 'currency',
            'width': 120
        }
    ]

    return columns

