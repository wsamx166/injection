import os
import time
print('')
os.system('sudo apt update')
os.system('sudo apt upgrade')
os.system('sudo apt install apktool')
os.system('wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.9.3.jar')
os.system('keytool -genkey -V -keystore key.keystore -alias elliot -keyalg RSA -keysize 2048 -validity 1000')
os.system('wget http://ftp.de.debian.org/debian/pool/main/a/android-platform-build/zipalign_8.1.0+r23-2_amd64.deb')
os.system('sudo dpkg -i zipalign_8.1.0+r23-2_amd64.deb')
time.sleep(3)
os.system('rm zipalign_8.1.0+r23-2_amd64.deb && mkdir apk && mv key.keystore apktool_2.9.3.jar apk ')
