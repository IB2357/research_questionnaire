# Copyright (c) 2024, Ibrahim Sultan and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    
    x_field = filters.get("x_field")  # Default to 'age' if no filter is provided
    
    columns = [
        {"fieldname": x_field, "label": _(x_field.capitalize()), "fieldtype": "Data", "width": 150},
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
    
    data = frappe.db.sql(f"""
        SELECT 
            CASE WHEN {x_field}='' THEN 'Not Specified' ELSE {x_field} END,
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
            {x_field}
    """)
    
    return columns, data
