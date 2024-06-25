import time

def get_time() -> str:
    """
    Get the current time and returns it as str 
    Example: '14:57:03 (28/01/23)'
    """
    return time.strftime('%X (%d/%m/%y)')
