// Copyright (c) 2024, Ibrahim Sultan and contributors
// For license information, please see license.txt

frappe.query_reports["Lab Results"] = {
	"filters": [
		{
			"fieldname": "group_by",
			"label": __("Group By"),
			"fieldtype": "Select",
			"options": "age\nresidence\noccupation\nincome_average_monthly\nnumber_of_children\ngestational_age\nspacing_between_pregnancies\nhas_health_problems\nhistory_of_abortion\nbleeding_on_current_pregnant\nironfolic_acid_supplementation\nvegetables\nfruits\nmeat\ndrinking_tea_or_coffee_with_meals_daily",
			reqd: 1,
		}		
	]
};
