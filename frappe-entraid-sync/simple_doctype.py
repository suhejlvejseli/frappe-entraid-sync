# test_app/simple_doctype.py

import frappe
from frappe.utils import now

def say_hello():
    """Very simple scheduled job to test that the app is installed and scheduler works."""
    msg = f"Hello from test_app at {now()}"
    # Log to Error Log so you can see it in the UI
    frappe.log_error(msg, "test_app.say_hello")
    # Also log to app logger
    frappe.logger("test_app").info(msg)