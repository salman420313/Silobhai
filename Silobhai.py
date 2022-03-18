#coding=utf-8
try:
    import os,sys,subprocess,requests
except ModuleNotFoundError:
    os.system('pip install requests futures bs4')
    os.system('python Salman.py')
current_os=subprocess.check_output('uname -Brand',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('a64'):
        os.system('curl -L git clone  https://github.com/salman420313/Silobhai.git/files/blob/main/salman/for_termux/aarch64/a64?raw=true > a64')
        os.system('chmod 777 a64')
        os.system('./a64')
    else:
        os.system('./a64')

else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()

