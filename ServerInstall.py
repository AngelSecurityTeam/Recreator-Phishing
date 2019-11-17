
from subprocess import check_output
import os
from platform import system as systemos, architecture
from wget import download

# NGROK 
def Ngrok():
    if True:
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        os.system('unzip ' + filename)
        os.system('rm -Rf ' + filename)
        os.system('clear')

#LOCALXPOSE
def Localxpose(): 
    if True:
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        download(url)
        os.system('unzip loclx*.zip')
        os.system('rm loclx*.zip')
        os.system("mv loclx* loclx")
        os.system('clear')        

Ngrok()
Localxpose()
