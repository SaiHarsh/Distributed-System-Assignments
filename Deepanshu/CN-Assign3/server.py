import socket
import os.path,time
import hashlib
import datetime
from colorama import Fore, Back, Style

class server:
    s = socket.socket()
    host = ''
    port = ''
    client_is_active = 1
    server_is_active = 1
    def __init__(self,portnumber):
        self.host = socket.gethostname()
        self.port = portnumber
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(10)

    def runserver(self):
        print "Starting server"
        while self.server_is_active:
            print "waiting for a client"
            c, addr = self.s.accept()
            self.client_is_active = 1
            print 'Got connection from', addr
            while self.client_is_active:
                #print "listening"
                print "waiting"
                x = c.recv(1024)
                if x.endswith('EOM'):
                    #valid message
                    #c.send("okfineEOM")
                    print "received",x
                    command  = x[:-3]
                    print command
                    if command == 'exit':
                        print "client disconnected"
                        self.client_is_active = 0
                        self.server_is_active = 0
                        c.close()
                    elif command == 'FileHash checkall':
                        #print "going to execute check all function"
                        self.checkall(c)
                    elif ''.join(command.split(' ')[:-1]) == 'FileHashverify':
                        print "single file"
                        filename = command.split(' ')[-1]
                        result = self.verify(os.getcwd() + '/' + filename)
                        #print result
                        try :
                            c.send(result)
                        except:
                            c.send("yolo")
                        #print "sent"
                        c.send('EOM')
                    elif command.split(' ')[0] == 'FileDownload':
                        self.FileDownload(command.split(' ')[1],c)
                    elif ''.join(command.split(' ')) == 'IndexGetlonglist' :
                        if len(command.split()) == 2:
                            self.longlist(c)
                        else:
                            c.send("Invalid arguments given.EOM")
                    elif ''.join(command.split()[:-2]) == 'IndexGetshortlist':
                        if len(command.split()) == 4:
                            startdate = command.split(' ')[2]
                            enddate = command.split(' ')[3]
                            self.shortlist(startdate, enddate, c)
                        else:
                            c.send("Invalid number of arguments.EOM")
                    elif command.split()[0] == 'verify':
                        if not len(command.split()) == 2:
                            c.send('Invalid input.please send the filename.EOM')
                        else:
                            c.send(self.verify(command.split()[1]))
                            c.send('File Exists.EOM')


        print "killing server"
        return

    def md5(self, fname):
        hash = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash.update(chunk)
        return hash.hexdigest()

    def last_modified(self,fname):
        return time.ctime(os.path.getmtime(fname))

    def verify(self,fname):
        try:
            return fname.split('/')[-1] + '\t' + self.md5(fname) + '\t' + self.last_modified(fname)
        except IOError:
            return fname.split('/')[-1] + "  is a directory,or is not found"
    def checkall(self,c):
        base_dir = os.getcwd() + '/'
        list = os.listdir(base_dir)
        for l in list:
            print self.verify(base_dir + l)
            try:
                c.send(self.verify(base_dir + l))
            except:
                c.send("Bad file")
        c.send('EOM')
        return

    def FileDownload(self,fname,c):
        try:
            x = self.md5(fname)
            c.send("okEOM")

            f = open(fname, 'rb')
            while True:
                data = f.read()
                if not data:
                    break
                c.sendall(data)
            f.close()
            c.send("EOIF")


        except IOError:
            c.send(fname + "  is not found.EOIF")

    def longlist(self,c):
        base_path= '.'
        files = os.listdir(".")
        for file in files:
            filename = os.path.basename(file)
            query = os.stat(file)
            timestamp = query[8]
            date  = datetime.datetime.fromtimestamp(timestamp)
            size = str(query.st_size) + ' KB'
            type = file.split('.')[-1] + ' file'
            final_ans = filename  + "  " + str(date) + "  " +  str(size) + '  ' + type + "\n"
            c.sendall(final_ans)
        c.send("EOM")


    def shortlist(self,a,b,c):
        files = os.listdir(".")
        try:
            start = datetime.datetime.strptime(a,'%Y-%m-%d')
        except ValueError:
            c.send("INVALID FORMAT for the starting timestamp")
            c.send('EOM')
            return
        try:
            end = datetime.datetime.strptime(b,'%Y-%m-%d')
        except ValueError:
            c.send("INVALID FORMAT for the ending timestamp")
            c.send('EOM')
            return
        for file in files:
            filename = os.path.basename(file)
            query = os.stat(file)
            timestamp = query[8]
            date  = datetime.datetime.fromtimestamp(timestamp)
            size = str(query.st_size) + ' KB'
            type = file.split('.')[-1] + ' file'
            final_ans = filename  + "  " + str(date) + "  " +  str(size) + '  ' + type + "\n"
            if date > start and date < end :
                c.sendall(final_ans)
        c.send("EOM")




def serverscript(portnumber):
    server1 = server(portnumber)
    server1.runserver()


if __name__ == '__main__':
    print "server program started"
    serverscript(8889)



