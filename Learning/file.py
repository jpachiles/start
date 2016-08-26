import os



"""
os.system()
import urllib2
response = urllib2.urlopen('http://pythonforbeginners.com/')
print response.info()
html = response.read().replace('="http://', '\n')
print html
response.close()

"""


def welcome():
    print '\033[1;31m __   __ ___  __  __ _   _  ___  __   __ \033[1;m'
    print '\033[1;31m|  \_/  | /\ |\ \/ /| |_| ||  _||  \_/  |\033[1;m'
    print '\033[1;31m|   _   | -- | |  | |  _  ||  _ |   _   |\033[1;m'
    print '\033[1;31m|__| |__|_||_| |__| |_| |_||___||__| |__|\033[1;m'

def login():

    login = None

    while not login:
        os.system('clear')
        code = raw_input("Enter your password\n")
        answer = code.encode('base64', 'strict').replace('\n', '')

        if answer == 'aWRpb21h':
            #print 'Correct Login'
            return True
        else:
            print 'Bad password !'

def tests():
    idioma = 'id1om4'
    maca = 'm$c~~'

    print idioma.encode('base64', 'strict').replace('\n', '')
    print maca.encode('base64', 'strict').replace('\n', '')
    code = raw_input("Enter you password\n")
    print code.encode('base64', 'strict').replace('\n', '')

def my_ip():
    ip = os.popen('ifconfig | grep "inet" | awk "{print $2}"').read()
    mac = os.popen("ifconfig | grep 'ether' | awk '{print $2}'").read()
    print ip
    print mac

def menu():
    logoff = None
    welcome()
    while not logoff:
        os.system('clear')
        print '\n'
        print '1 - Find my ip'
        print '2 - bla bla'
        print 'exit - to exit'
        menu = raw_input("How do you want to continue? (Menu Number).\n")
        if menu == '1':
            # print 'Correct Login'
            my_ip()

        elif menu == '2':
            print 2

        elif menu == '3':
            print 3

        elif menu == 'exit':
            logoff = True
            print "\n\nThe quieter you become, the more you are able to hear\n\n"

def main():
    if login():
        menu ()
    #sessao = login()
    #tests()


if __name__ == "__main__":
    main()