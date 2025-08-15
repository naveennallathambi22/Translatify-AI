import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print('All dependencies installed successfully.')
    except Exception as e:
        print(f'Error installing dependencies: {e}')

if __name__ == '__main__':
    install_requirements()
