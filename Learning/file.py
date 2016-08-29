import os
import urllib2
from time import sleep
from thread import start_new_thread



def deface_verify(target):
    site = target
    response = urllib2.urlopen(site)
    htmlold = response.read()
    sleep(60)
    response = urllib2.urlopen(site)
    htmlnew = response.read()

    if htmlold == htmlnew:
        print 'Checked! Everything is ok !'
    else:
        print 'WARNING'
    response.close()

def welcome():
    logo =  '\033[1;31m __   __ ___  __  __ _   _  ___  __   __ \033[1;m\n'
    logo += '\033[1;31m|  \_/  | /\ |\ \/ /| |_| ||  _||  \_/  |\033[1;m\n'
    logo += '\033[1;31m|   _   | -- | |  | |  _  ||  _ |   _   |\033[1;m\n'
    logo += '\033[1;31m|__| |__|_||_| |__| |_| |_||___||__| |__|\033[1;m\n'
    return logo

def login():
    from time import sleep
    import getpass
    login = None

    while not login:
        os.system('clear')
        code = getpass.getpass("Enter your password\n")
        answer = code.encode('base64', 'strict').replace('\n', '')

        if answer == 'aWRpb21h':
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\033[1;32mWelcome!\033[1;m \nLoading...'
            sleep(5)
            return True
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print '\033[1;31mBad password!\033[1;m \nTry again.'
            sleep(2)

def tests():
    idioma = 'id1om4'
    maca = 'm$c~~'

    print idioma.encode('base64', 'strict').replace('\n', '')
    print maca.encode('base64', 'strict').replace('\n', '')
    code = raw_input("Enter you password\n")
    print code.encode('base64', 'strict').replace('\n', '')

def my_ip():
    #os.system('cls' if os.name == 'nt' else 'clear')
    ip = os.popen('ifconfig | grep "inet" | awk "{print $2}"').read()
    mac = os.popen("ifconfig | grep 'ether' | awk '{print $2}'").read()
    result = ip + '\n' + mac
    return result

def menu():

    os.system('cls' if os.name == 'nt' else 'clear')
    print welcome()
    print '\n'
    print '1 - Find my ip'
    print '2 - Deface Verify (Background)'
    print '0 - to exit'
    menuop = int(raw_input("How do you want to continue? (Menu Number).\n"))
    if menuop == 1:
        # print 'Correct Login'
        print my_ip()

    elif menuop == 2:
        target = raw_input("Type the website that you want to verify? (Copy your browser url to a great verify)\n")
        start_new_thread(deface_verify(target), (60,))

    elif menuop == 3:
        print 3

    ctn = int(raw_input("Do you want to use another function? 1-Yes / 2-No\n"))

    if ctn == 1:
        menu()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'The quieter you become, the more you are able to hear'
        exit (1)



def main():
    if login():
        menu ()



if __name__ == "__main__":
    main()
