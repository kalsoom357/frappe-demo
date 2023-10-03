frappe.query_reports["New Attendance Script Report"] = {
	"filters": [
		{
			"fieldname": "employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			"on_change": function (query_report) {
				const employee = frappe.query_report.get_filter_value('employee');

				if (employee) {
					// Fetch the name of the selected employee
					frappe.call({
						method: "frappe.client.get_value",
						args: {
							doctype: "Employee",
							filters: { name: employee },
							fieldname: "employee_name"
						},
						callback: function (response) {
							const employeeName = response.message.employee_name;
							// Set the value of the "Employee Name" filter
							frappe.query_report.set_filter_value("employee_name", employeeName);
							frappe.query_report.refresh();
						}
					});
				} else {
					// Clear the "Employee Name" filter if "Employee" filter is cleared
					frappe.query_report.set_filter_value("employee_name", "");
					frappe.query_report.refresh();
				}
			}
		},
		{
			"fieldname": "employee_name",
			"label": __("Employee Name"),
			"fieldtype": "Data",
			"read_only": 1
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.nowdate(), -7),
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.nowdate(),
		},

	]	
};





