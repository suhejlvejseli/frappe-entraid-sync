# test_app/hooks.py

# This scheduler event will run every hour and log a message
scheduler_events = {
    "hourly": [
        "test_app.simple_doctype.say_hello"
    ],
}