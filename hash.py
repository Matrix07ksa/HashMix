import sys as n
import os as matrix
import time as mm
from platform import system
import hashlib
try:
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    B = '\033[34m'  # blue
    def clear():
        if system() == 'Linux':
            matrix.system("clear")
        if system() == 'Windows':
            matrix.system('cls')
            matrix.system('color a')
        else:
            pass
    clear()


    def slow(M):
        for c in M + '\n':
            n.stdout.write(c)
            n.stdout.flush()
            mm.sleep(1. / 100)
    slow(R+'\t\t\t\t\n\n\n insta:d7_nn\t\t\t\tfb:matrix.gov')        
    print(B+'''
                             ___                                      
                            (   )                                     
     ___ .-. .-.     .---.   | |_      ___ .-.      .--.    ___  ___  
    (   )   '   \   / .-, \ (   __)   (   )   \    /    \  (   )(   ) 
     |  .-.  .-. ; (__) ; |  | |       | ' .-. ;  |  .-. ;  | |  | |  
     | |  | |  | |   .'`  |  | | ___   |  / (___) |  | | |   \ `' /   
     | |  | |  | |  / .'| |  | |(   )  | |        |  |/  |   / ,. \   
     | |  | |  | | | /  | |  | | | |   | |        |  ' _.'  ' .  ; .  
     | |  | |  | | ; |  ; |  | ' | |   | |        |  .'.-.  | |  | |  
     | |  | |  | | ' `-'  |  ' `-' ;   | |        '  `-' /  | |  | |  
    (___)(___)(___)`.__.'_.   `.__.   (___)        `.__.'  (___)(___)
    ''')
    slow(G+'''
    [1]}> Encrypt name or password
    [99]}> exit

    ''')
    numper = input('Enter numper:: ')
    while True:
            if numper==1: 
                slow(G+'''
[1]}> MD4
[2]}> MD5
[3]}> SHA1
[4]}> SHA224
[5]}> SHA256
[6]}> SHA384
[7]}> SHA512

[99]}> exit\t\t''') 
                
            else:
                break
            numper2 =  input('Enter numper type hach:: ')
            if numper2 ==1:
                nampas = raw_input('Enter text:: ')
                nampas2 = nampas.encode('utf-8')
                h = hashlib.new('md4')
                h.update(nampas)
                haa=h.hexdigest()
                m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                print(haa,len(haa),nampas)    
            elif numper2 ==2:
                nampas = raw_input('Enter text:: ')
                nampas = nampas.encode('utf-8')
                h = hashlib.new('md5')
                h.update(nampas)
                haa=h.hexdigest()
                m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                print(haa,len(haa),nampas)   
            elif numper2 ==3:
                 nampas = raw_input('Enter text:: ')
                 nampas = nampas.encode('utf-8')
                 h = hashlib.new('sha1')
                 h.update(nampas)
                 haa=h.hexdigest()
                 m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                 print(haa,len(haa),nampas)
            elif numper2 ==4:
                 nampas = raw_input('Enter text:: ')
                 nampas = nampas.encode('utf-8')
                 h = hashlib.new('sha224')
                 h.update(nampas) 
                 haa=h.hexdigest()
                 m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                 print(haa,len(haa),nampas)
            elif numper2 ==5:
                 nampas = raw_input('Enter text:: ')
                 nampas = nampas.encode('utf-8')
                 h = hashlib.new('sha256')
                 h.update(nampas)
                 haa=h.hexdigest()
                 m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                 print(haa,len(haa),nampas)
            elif numper2 ==6:
                 nampas = raw_input('Enter text:: ')
                 nampas = nampas.encode('utf-8')
                 h = hashlib.new('sha384')
                 h.update(nampas)
                 haa=h.hexdigest()
                 m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                 print(haa,len(haa),nampas)
            elif numper2 ==7:
                 nampas = raw_input('Enter text:: ')
                 nampas = nampas.encode('utf-8')
                 h = hashlib.new('sha512')
                 h.update(nampas)
                 haa=h.hexdigest()
                 m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                 print(haa,len(haa),nampas)    
            elif numper2 ==99:
                break
            else:
                print('numper false not hach',numper)

except KeyboardInterrupt:
    print('ctrl keyboard false')
except SyntaxError:
    print('FALSE ENTER ')
except NameError :
    print('((NO string exit))')
    



            
            
            
         
         
        
             
                
            
    
            
        
            
            
                
    

    
    
        
                
            
            
    
    
