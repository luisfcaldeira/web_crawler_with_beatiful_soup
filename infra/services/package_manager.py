import subprocess
import sys


class PackageManager():
    
    @staticmethod
    def install(package):
        if package not in sys.modules:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            
    @staticmethod
    def uninstall(package):
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", package])