import os 
def shutdown_system():
    """Shuts down the system."""
    os.system("shutdown /s /t 1") 
if __name__ == "__main__":
    shutdown_system()