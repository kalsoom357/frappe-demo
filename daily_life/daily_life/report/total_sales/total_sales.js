// Copyright (c) 2023, kalsoom and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Total Sales"] = {
	"filters": [
			
		
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.nowdate(), -20),
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.nowdate(),
		}
	]
};
