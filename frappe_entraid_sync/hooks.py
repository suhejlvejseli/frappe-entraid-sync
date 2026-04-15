# test_app/hooks.py

# This scheduler event will run every hour and log a message
scheduler_events = {
    "hourly": [
        "frappe_entraid_sync.simple_doctype.say_hello"
    ],
}