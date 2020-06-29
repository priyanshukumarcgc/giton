import os

def check_rebot():
    """returns true if computer has a pending rebot request ."""
    return os.path.exists("run/rebot-required")

    
def main():
    pass
main()