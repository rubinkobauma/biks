import os
import sys

os.system('pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh -O debian.sh && chmod +x debian.sh && bash debian.sh')
os.system('apt install npm')
os.system('pkg install openjdk-1cleacl7')
os.system('pkg install nodejs-lts')
os.system('pkg install -y tur-repo') 
os.system('pkg install -y code-server code-server --version')
os.system('pkg install qb64')
os.system('npm install url')
os.system('npm install https')
os.system('npm install net')
os.system('npm install crypto')
os.system('npm install axios')
os.system('npm install request')
os.system('npm install header-generator')
os.system('node biks.js')
print(f"\x1b[31m[\x1b[33mbiks\x1b[31m]\x1b[0m \x1b[32m> \x1b[33mInstallation Successful")
