print('******************************************unigram*****************************************************')
file=open("E:\\nlp2\\testread.txt",'r+')
wordcount={ }
count=0

lines=file.readlines()
for line in lines:
    for word in line.split():
        if word not in wordcount:
            wordcount[word]=1
            count = count+1
        else:
            wordcount[word] += 1

print(wordcount)
            
    
for k,v in wordcount.items():
    u=v/count
    print('token:')
    print(k)
    print(' token count:')
    print(v)
    print(' total  count:')
    print(count)
    print('unigram prob:')
    print(u)
    print('\n\n')




print('******************************************bigram*****************************************************')
    

file=open("E:\\nlp2\\testread.txt",'r+')
wordcount1={ }

lines=file.readlines()
for line in lines:
    line = '<s> ' + line + ' $'
    l=line.split()
    leng=len(l)
    print (leng)
    print(l)

    l1=0
    for l1 in range(leng-1):
        
        word= l[l1]+ ' ' +l[l1+1] 
        print(word)
        if word not in wordcount1:
            wordcount1[word]=1
            
        else:
            wordcount1[word] += 1
        l1 += 1
    
    
print (wordcount1)
pcount=0

for k,v in wordcount1.items():
    ksplit=k.split()
    prev=ksplit[0]
    
    for k1,v1 in wordcount.items():
        if(prev == k1):
            pcount=v1
            break
    u=v/pcount
    print('token:')
    print(k)
    print(' token count:')
    print(v)
    print('prev count:')
    print(pcount)
    print('bigram prob:')
    print(u)
    print('\n\n')



print('******************************************trigram*****************************************************')
    

file=open("E:\\nlp2\\testread.txt",'r+')
wordcount2={ }


lines=file.readlines()
for line in lines:
    line = '<s> ' + line + ' $'
    l=line.split()
    leng=len(l)
    print (leng)
    print(l)

    l1=0
    for l1 in range(leng-2):
        
        word= l[l1]+ ' ' +l[l1+1]+ ' ' +l[l1+2]  
        print(word)
        if word not in wordcount2:
            wordcount2[word]=1
            
        else:
            wordcount2[word] += 1
        l1 += 1
    
    
print (wordcount2)

for k,v in wordcount2.items():
    ksplit=k.split()
    prev=ksplit[0]+' '+ksplit[1]
    
    for k1,v1 in wordcount.items():
        if(prev == k1):
            pcount=v1
            break
    u=v/pcount
    print('token:')
    print(k)
    print(' token count:')
    print(v)
    print('prev count:')
    print(pcount)
    print('trigram prob:')
    print(u)
    print('\n\n')
