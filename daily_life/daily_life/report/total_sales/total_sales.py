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
        si.customer AS 'Customer',
        siitem.qty AS 'Quantity',
        siitem.rate AS 'Rate',
        siitem.weight_per_unit AS 'Weight',
        siitem.item_name AS 'Item',
        si.total AS 'Total',
        si.status AS 'Status'
        FROM
            `tabSales Invoice` AS si
        JOIN
            `tabSales Invoice Item` AS siitem
        ON
            si.name = siitem.parent
        WHERE
            1 = 1
			{conditions}
			
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
            'fieldname': 'Customer',
            'label': _('Customer'),
            'fieldtype': 'Link',
            'options': 'Customer',
            'width': 150
        },
        {
            'fieldname': 'Quantity',
            'label': _('Quantity'),
            'fieldtype': 'Float',
            'width': 100
        },
        {
            'fieldname': 'Rate',
            'label': _('Rate'),
            'fieldtype': 'Currency',
            'options': 'currency',
            'width': 100
        },
        {
            'fieldname': 'Weight',
            'label': _('Weight'),
            'fieldtype': 'Float',
            'width': 100
        },
        {
            'fieldname': 'Item',
            'label': _('Item'),
            'fieldtype': 'Link',
            'options': 'Item',
            'width': 150
        },
        {
            'fieldname': 'Total',
            'label': _('Total'),
            'fieldtype': 'Currency',
            'options': 'currency',
            'width': 120
        },
        {
            'fieldname': 'Status',
            'label': _('Status'),
            'fieldtype': 'Data',
            'width': 100
        }
    ]

    return columns

