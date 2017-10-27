from colorama import Fore, Back, Style
import re
data = {}
T = []
t_count = []
t_commit_undo = []
t_commit_redo = []
t_inst= 0






def init_values():
    init_file = '../Transactions/initial_values.txt'
    global data
    data = {}
    temp = open(init_file,'r')
    temp = temp.readlines()
    for row in temp:
        x = row.split()
        data[x[0]] = int(x[1])
    return

def init_transactions(n):
    global T,t_count,t_commit_undo,t_commit_redo
    T = []
    t_count = []
    t_path = '../Transactions/'
    for i in range(1,n+1):
        f_path = t_path + 'T' + str(i) + '.txt'
        temp = open(f_path,'r')
        temp = temp.read()
        temp = temp.split('\n')[:-1]
        T.append(temp)
    t_count = [0]*len(T)
    t_commit_undo = [0]*len(T)
    t_commit_redo = [0]*len(T)
    return
def get_variable_list():
    global data
    temp = ''
    temp2 = ['A','B','C','D']
    for var in temp2:
        temp += var + " " + str(data[var]) + " "
    return temp



    return temp
def log(type_of_log,t_no,extra):
    global t_commit_undo,t_commit_redo
    if type_of_log == 'start':
        text = '<start T' + str(t_no) + '> '
        text += get_variable_list()
        with open('../logs' + str(extra['q_num']) + ".txt_redo","a") as myfile:
            myfile.write(text + '\n')
        print(Fore.RED + Back.GREEN + text + 'redo' +  Style.RESET_ALL)
        with open('../logs' + str(extra['q_num']) + ".txt_undo","a") as myfile:
            myfile.write(text + '\n')
        print(Fore.RED + Back.GREEN + text + 'undo' + Style.RESET_ALL)
    elif type_of_log == 'commit':
        if extra['type'] == 'undo':
            if t_commit_undo[t_no -1] == 0: 
                text = '<commit T' + str(t_no) + '> '
                text += get_variable_list()
                print(Fore.RED + Back.GREEN + text + 'undo'   + Style.RESET_ALL)
                with open('../logs' + str(extra['q_num']) + ".txt_undo","a") as myfile:
                    myfile.write(text + '\n')
                    print '../logs' + str(extra['q_num']) + ".txt_undo file"
                    
                t_commit_undo[t_no -1] = 1
        elif extra['type'] == 'redo':
            print "called redo of qnum ",extra['q_num']
            if t_commit_redo[t_no -1] == 0: 
                text = '<commit T' + str(t_no) + '> '
                text += get_variable_list()
                print(Fore.RED + Back.GREEN + text + 'redo' + Style.RESET_ALL)
                with open('../logs' + str(extra['q_num']) + ".txt_redo","a") as myfile:
                    myfile.write(text + '\n')
                    print '../logs' + str(extra['q_num']) + ".txt_redo file"
                t_commit_redo[t_no -1] = 1
        
    elif type_of_log == 'write':
        if extra['type'] == 'undo':
            with open('../logs' + str(extra['q_num']) + ".txt_undo","a") as myfile:
                myfile.write(extra['text'] + '\n')
            print(Fore.RED + Back.GREEN + extra['text'] + 'undo' + Style.RESET_ALL)
        elif extra['type'] == 'redo':
            with open('../logs' + str(extra['q_num']) + ".txt_redo","a") as myfile:
                myfile.write(extra['text'] + '\n')
            print(Fore.RED + Back.GREEN + extra['text'] + 'redo' + Style.RESET_ALL)




    return
def READ(inst,t_no):
    global data
    temp = inst.split('(')[1]
    temp = temp[:-1]
    temp = temp.split(',')
    temp = [ i.strip() for i in temp]
    data[temp[1]] = data[temp[0]]
    #text = "source " + temp[0] + " dest " + temp[1]
    #print(Fore.RED + text + Style.RESET_ALL)
    return
def WRITE(inst,t_no,q_num):
    global data
    temp = inst.split('(')[1]
    temp = temp[:-1]
    temp = temp.split(',')
    temp = [ i.strip() for i in temp]
    ## for undo
    text = ''
    text = '<T' + str(t_no) + " " + temp[0] + " " + str(data[temp[0]]) + '> '
    text += get_variable_list()
    #print(Fore.RED + Back.GREEN + text + Style.RESET_ALL)
    log('write',t_no,{'type':'undo','text':text,'q_num':q_num}) 
    data[temp[0]] = data[temp[1]]
     
    ## for redo
    text = ''
    text = '<T' + str(t_no) + " " + temp[0] + " " + str(data[temp[0]]) + '> '
    text += get_variable_list()
    log('write',t_no,{'type':'redo','text':text,'q_num':q_num}) 
    #print(Fore.RED + Back.GREEN + text + Style.RESET_ALL)


    #text = "source " + temp[0] + " dest " + temp[1]
    #print(Fore.RED + text + Style.RESET_ALL)
    return
def evaluate(inst,t_no):
    global data
    S = inst
    S = S.replace(':=','=')
    x = re.split("\+|\-|\*|\/|=",S)
    final = []
    for i in x:
        try:
            i = int(i)
        except:
            i = i.strip()
            if not i in final:
                final.append(i)
    for i in final:
        S = S.replace(i,"data['" + i + "']")
    #print(Fore.GREEN + Back.RED + S + Style.RESET_ALL)
    exec(S)
    return
    
def execute(t_no,q_num):
    global T,t_count,data,t_inst,t_commit_redo
    present_count = t_count[t_no-1]
    q_num_new = q_num
    if present_count + q_num  > len(T[t_no-1]):
        q_num_new = len(T[t_no-1]) - present_count
    start = present_count
    end = start + q_num_new
    temp_inst = T[t_no-1][start:end]
    if present_count == 0:
        log('start',t_no,{'q_num':q_num})
    t_count[t_no-1] = end
    for inst in temp_inst:
        print "T",str(t_no)," --> ",inst
        if 'READ' in inst:
            READ(inst,t_no)
        elif 'WRITE' in inst:
            WRITE(inst,t_no,q_num)
        elif '=' in inst:
            evaluate(inst,t_no)
        elif 'OUTPUT' in inst:
            log('commit',t_no,{'type':'undo','q_num':q_num})
    
    if t_count[t_no-1] == len(T[t_no-1]):
        log('commit',t_no,{'type':'redo','q_num':q_num})

    
    print "T",str(t_no)," --> ",temp_inst
    return
       

def init_logger():
    global data,T,t_count,t_inst
    init_values()
    init_transactions(3)
    temp = [len(i) for i in T]
    t_inst = sum(temp)
    return max(temp)

def start_logging():
    global data,T,t_count,t_inst,t_commit_undo,t_commit_redo
    max_q = init_logger()
    correct_t = []
    
    
    t_count = [0]*len(T)
    t_commit_undo = [0]*len(T)
    t_commit_redo = [0]*len(T)
    print "Executing all transactions one by one"
    for i in range(1,len(T)+1):
        execute(i,len(T[i-1]))
        print "Transaction ",i," executed"
    ref_data = data    
    temp = ['A','B','C','D']
    ref_data = {i:ref_data[i] for i in temp}
    print "ref_data is ",ref_data
    
    print "Starting iteration over all quantun numbers"
    
    
    #max_q = 1
    for q_num in range(1,max_q +1):
        t_count = [0]*len(T)
        t_commit_undo = [0]*len(T)
        t_commit_redo = [0]*len(T)
        t_no = 1
        init_values()

        print "logging of quantum_number ",q_num
        while 1:
            if t_no == len(T)+1:
                t_no = 1
                continue
            elif sum(t_count) == t_inst:
                break
            elif t_count[t_no-1] == len(T[t_no-1]):
                #log('commit',t_no,{'type':'redo','q_num':q_num})
                t_no += 1
                continue
            else:
                execute(t_no,q_num)
                t_no += 1
        print q_num,"  completed"
        temp = ['A','B','C','D']
        data = {i:data[i] for i in temp}
        print "data ",data
        print "ref_data ",ref_data
        
        score = cmp(data,ref_data)
        
        if score == 0:
            print "correct transaction"
            correct_t.append(q_num)
            with open('../logs' + str(q_num) + ".txt_redo","a") as myfile:
                myfile.write(str(q_num) + '\n')
            print(Fore.RED + Back.GREEN + str(q_num) + 'redo' +  Style.RESET_ALL)
            with open('../logs' + str(q_num) + ".txt_undo","a") as myfile:
                myfile.write(str(q_num) + '\n')
            print(Fore.RED + Back.GREEN + str(q_num) + 'undo' + Style.RESET_ALL)

        else:
            print "wrong transaction"
        print "\n\n\n\n"
    print "list of correct q_num ",correct_t
    return
        
if __name__ == "__main__":
    start_logging()
