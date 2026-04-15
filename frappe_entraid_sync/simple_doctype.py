# test_app/simple_doctype.py

import frappe
from frappe.utils import now

def say_hello():
    """Very simple scheduled job to test that the app is installed and scheduler works."""
    msg = f"Hello from frappe_entraid_sync at {now()}"
    # Log to Error Log so you can see it in the UI
    frappe.log_error(msg, "frappe_entraid_sync.say_hello")
    # Also log to app logger
    frappe.logger("frappe_entraid_sync").info(msg)