# Copyright (c) 2024, Ibrahim Sultan and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    
    group_by = filters.get("group_by", "age")  # Default to 'age' if no filter is provided
    
    # Define columns for the report table
    columns = [
        {"fieldname": group_by, "label": _(group_by.capitalize()), "fieldtype": "Data", "width": 150},
        {"fieldname": "count", "label": _("Count"), "fieldtype": "Int", "width": 100},
        {"fieldname": "hb", "label": _("HB (g/dl)"), "fieldtype": "Float", "width": 100},
        {"fieldname": "pcv", "label": _("PCV (%)"), "fieldtype": "Float", "width": 100},
        {"fieldname": "rbc", "label": _("RBC"), "fieldtype": "Float", "width": 100},
        {"fieldname": "wbc", "label": _("WBC"), "fieldtype": "Float", "width": 100},
        {"fieldname": "plt", "label": _("Plt"), "fieldtype": "Float", "width": 100},
        {"fieldname": "mcv", "label": _("MCV (fl)"), "fieldtype": "Float", "width": 100},
        {"fieldname": "mch", "label": _("MCH (Pg)"), "fieldtype": "Float", "width": 100},
        {"fieldname": "mchc", "label": _("MCHC"), "fieldtype": "Float", "width": 100},
        {"fieldname": "rdw", "label": _("RDW"), "fieldtype": "Float", "width": 100},
    ]
    
    # Fetch data for the report table
    data = frappe.db.sql(f"""
        SELECT 
            CASE WHEN {group_by}='' THEN 'Not Specified' ELSE {group_by} END,
            COUNT(*) as count,
            AVG(hb),
            AVG(pcv),
            AVG(rbc),
            AVG(wbc),
            AVG(plt),
            AVG(mcv),
            AVG(mch),
            AVG(mchc),
            AVG(rdw)
        FROM 
            `tabQuestionnaire`
        GROUP BY 
            {group_by}
    """)
    
    # Fetch chart data based on the same query
    chart_data = get_chart_data(data, group_by, filters)

    return columns, data, None, chart_data

def get_chart_data(data, group_by, filters):
    if not data:
        return {}

    labels = [row[0] for row in data]  # Extract labels from the first column of data
    y_fields = ["count", "hb", "pcv", "rbc", "wbc", "plt", "mcv", "mch", "mchc", "rdw"]
    
    datasets = []
    for y_field in y_fields:
        values = [row[y_fields.index(y_field) + 1] for row in data]
        datasets.append({
            "name": _(y_field.upper()),
            "values": values,
        })

    # Prepare chart data structure
    chart_data = {
        "data": {
            "labels": labels,
            "datasets": datasets,
        },
        "type": "bar",
    }

    return chart_data
