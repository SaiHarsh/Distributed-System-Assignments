import socket
import os
from colorama import Fore, Back, Style


class Client:
    s = socket.socket()
    host = ''
    port = ''
    alive = 1
    list_of_commands = ['FileHashcheckall','FileHashverify','FileDownload','IndexGetlonglist','IndexGetshortlist','verify']
    def __init__(self, portnumber):
        self.host = socket.gethostname()
        self.port = portnumber
        self.s.connect((self.host, self.port))

    def receivefromserver(self):
        #print "waiting to recive something"
        close = 0
        while close == 0:
            #print "yeah"
            m = self.s.recv(1024)
            if m.endswith('EOM'):
                close = 1
                print m[:-3]
            elif len(m):
                print m
        #print "receiving done"
        return

    def receivefile(self,fname):
        close = 0
        m = self.s.recv(1024)
        if m.endswith("is not found.EOM"):
            print fname + "  is not found"
        else:
            f =  open(fname, 'wb')
            while close == 0:
            #print "yeah"
                m = self.s.recv(1024)
                if m.endswith('EOIF'):
                    close = 1
                    f.write(m[:-4])
                elif len(m):
                    f.write(m)
            f.close()
        #print "receiving done"
        return

    def send_to_server(self, data):
        #print "sending ",data
        self.s.send(data+'EOM')
        #self.s.send('EOM')
        return

    def takeinput(self):
        print(Fore.RED +  'command>'),
        print(Style.RESET_ALL),
        x = raw_input()
        if x.strip() == 'help' or x.strip() == 'Help':
            self.print_help()
        elif x.strip() == 'clear':
            os.system('clear')
        elif len(x):
            if x == 'exit':
                self.alive = 0
                self.s.send("exitEOM")
                self.s.close()
            else:
                '''
                if ''.join(x.split(' ')[:-1]).translate(None,' ') in self.list_of_commands:
                    self.send_to_server(x.strip())
                    if ''.join(x.split(' ')[:-1]).translate(None,' ') == 'FileDownload':
                        self.receivefile(x.split(' ')[1].replace("'",""))
                    else:
                        #print "command is " + ''.join(x.split(' ')[:-1]).translate(None,' ')
                        self.receivefromserver()
                elif x.translate(None,' ') in  self.list_of_commands:
                    #print "command is " + x.translate(None,' ')
                    self.send_to_server(x.strip())
                    self.receivefromserver()
                elif ''.join(x.split(' ')[:-2]) in self.list_of_commands and len(x.split(' ')) == 4:
                    self.send_to_server(x.strip())
                    self.receivefromserver()
                else:
                    print "Command not found"
                '''

                if x.split()[0] in self.list_of_commands:
                    #for filedownload
                    if x.split()[0] == 'FileDownload':
                        if len(x.split()) == 2:
                            self.send_to_server(x.strip())
                            self.receivefile(x.split()[1].replace("'",""))
                        else:
                            print 'invalid number of arguments'
                    else:
                        self.send_to_server(x.strip())
                        self.receivefromserver()
                elif ''.join(x.split()) in self.list_of_commands:
                    if ''.join(x.split()) == 'IndexGetshortlist':
                        print "please provide 2 arguments"
                    else:
                        self.send_to_server(x.strip())
                        self.receivefromserver()
                elif ''.join(x.split()[0:2]) in self.list_of_commands and len(x.split()) == 4:
                    self.send_to_server(x.strip())
                    self.receivefromserver()
                else:
                    print "Command not found"


        return

    def print_help(self):
        print "                                USER GUIDE               \n\n"
        print "----------------------------------------------------------------------------\n"
        print "- COMMAND                 |  DESCRIPTION                                   -\n"
        print "---------------------------------------------------------------------------\n"
        print "- IndexGet longlist       | Get name,size,timestamp,type                   -\n"
        print "---------------------------------------------------------------------------\n"
        print "- IndexGet shortlist      | Get name,size,timestamp between 2 timestamps   -\n"
        print "---------------------------------------------------------------------------\n"
        print "- verify <Filename>       | verify if the file                             -\n"
        print "---------------------------------------------------------------------------\n"
        print "- FileHash Checkall       | returns the last                               -\n"
        print "----------------------------------------------------------------------------\n"
        print "- FileDownload <filename> | saves the file in the local directory          -\n"
        print "----------------------------------------------------------------------------\n"
        print "- clear                   | clears the screen                              -\n"
        print "----------------------------------------------------------------------------\n"
        print "- help                    |  Displays list of all commands available       -\n"
        print "----------------------------------------------------------------------------\n"
        print "- clear                   |  Clears the screen                             -\n"
        print "----------------------------------------------------------------------------\n"
        print "- exit                    |  Exists the terminal                           -\n"
        print "----------------------------------------------------------------------------\n"

        return

    def runclient(self):
        while self.alive:
            self.takeinput()
        print "closing client"
        return


if __name__ == '__main__':
    client1 = Client(8889)
    client1.runclient()
