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
    print ' __   __ ___  __  __ _   _  ___  __   __ '
    print '|  \_/  | /\ |\ \/ /| |_| ||  _||  \_/  |'
    print '|   _   | -- | |  | |  _  ||  _ |   _   |'
    print '|__| |__|_||_| |__| |_| |_||___||__| |__|'

def login():

    login = None

    while not login:
        os.system('clear')
        code = raw_input("Enter you password\n")
        answer = code.encode('base64', 'strict').replace('\n', '')

        if answer == 'aWRpb21h':
            print 'Correct Login'
            return True
        else:
            print 'Login Failed'

def tests():
    idioma = 'id1om4'
    maca = 'm$c~~'

    print idioma.encode('base64', 'strict').replace('\n', '')
    print maca.encode('base64', 'strict').replace('\n', '')
    code = raw_input("Enter you password\n")
    print code.encode('base64', 'strict').replace('\n', '')

def main():
    if login:
        welcome()
    #sessao = login()
    #tests()


if __name__ == "__main__":
    main()