# common_utils.py

def log_message(message):
    """
    Logs a message to the console.
    """
    print(f"[LOG]: {message}")

def validate_data(data):
    """
    Validates data for basic integrity checks.
    """
    if not data:
        raise ValueError("Data cannot be empty")
    return True