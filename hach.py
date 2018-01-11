import sys as n
import os as matrix
import time as mm
from platform import system
import hashlib
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
        mm.sleep(2. / 100)


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
    [4}> SHA-224
    
    
    [99]}> exit''')
        numper2 =  input('Enter numper type hach:: ')
        
        if numper2 ==1:
            
            text = str(input('Enter text:: '))
            text = text.encode('utf-8')
            h = hashlib.new('md4')
            h.update(text)
            haa=h.hexdigest()
            print(haa,len(haa))
            
        elif numper2 ==2:
            text = str(input('Enter text:: '))
            text = text.encode('utf-8')
            h = hashlib.new('md5')
            h.update(text)
            haa=h.hexdigest()
            print(haa,len(haa))
        elif numper2 ==3:
            text = str(input('Enter text:: '))
            text = text.encode('utf-8')
            h = hashlib.new('sha1')
            h.update(text)
            haa=h.hexdigest()
            print(haa,len(haa))
        elif numper2 ==4:
            
            text = str(input('Enter text:: '))
            text = text.encode('utf-8')
            h = hashlib.new('sha-227')
            h.update(text)
            haa=h.hexdigest()
            print(haa,len(haa))
        


        
        elif numper2 ==99:
            break
        else:
            
            print('numper false not hach',numper)
            
            
                
    
        
            
            
    
    
