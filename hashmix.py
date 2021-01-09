#!/bin/python
#####################################################################################code by Matrix#######################################################################################################################################################################################
import sys as n
import os as matrix
import time as mm
from platform import system
import hashlib
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m' # gray
try:
    def Matrix():
        
        
        
           
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
        slow(R+'\t\t\t\t\n\n\n\n\n Insta:d7_nn\t\t\t\t\t\tFB:matrix.gov')        
        print(R+'''
                                                                      .uuu
    z@#"%c                      .uuzm**"""""*%mu..             z*"` .e@#N      
   @!!!R.  #c              .z*"                    ^*c       z    dT!!!!!>     
  '!!!!!!N   "i         u*"                            #s  :"   @?!!!!!!!R     
  t!!!!!!!#u   "i    .@                                  ^$   :R!!!!!!!!!X     
  '!!!!!!!!!#c   "i:#                                      ?> R!!!!!!!!!!X     
  '!!!!!!!!!!!N   @                                         4W!!!!!!!!!!!>     
  '!!!!!!!!!!!!Ru"                                           ?!!!!!!!!!!X      
  'X!!!!!!!!!!!9~                                      .  .  'X!!!!!!!!!6      
   R!!!!!!!!!!tF                                     z$#`   h &!!UR!!!!!F      
   ?!!!!!$X!!!$                                    .@       X $WTR!!!!!X       
    M!!!!!i#U!E  .                                @F        ! FdR!!!!!!f       
    'X!!!!!#c'?u@#"*$N.                         :$          F'9!!!!!!!@        
     9!!!!!!!?NM      ^*c                      dF          ' @!!!!!!!X>        
      R!!!!!!!!&         "e                   d            K<!!!!!!!XF         
      'X!!!!!!!M>          ^N                f            < E!!!!!!X"          
        t!!!!!!!#            ^N            :"      .e$"^  Fn!!!!!XP            
         #X!!!!!!ML             *c       z"    .e$$$$$   M'!!!!W*              
           "*UX!!X@t  ^%u.         ""**#).zd$$#$$$$$$$  <\*@**"                
                    'N    4$$$$$@$$$)$$#$$k4$$$$$$$$$E :$                      
                       ?>  "$$$$$$":$$$W$$$ "$$$$$$$$   %                      
                      :"           ? ^#*"  S  "$$$$$     ?                     
                      F            L      d$L            X                     
                      &           t$i    @$$$           f                      
                       *          $$$$$$$$$$\&        @                        
                        '*.      W'$$$$$$$$FM h    u#                          
                           ^*muz* % $$$$$$":    `"                             
                   {}
               	       https://github.com/Matrix07ksa     ''').format(W)
        
        slow(G+'''


[1]}> Encrypt name or password
[2]}> Cracked hash
[3]}> Hash type 
            	[99]}> exit

            ''')
        numper = int(input('Enter numper:: '))
        while True:
     
            if numper == 1:
                slow(C+'''
    [1]}> MD4
    [2]}> MD5
    [3]}> SHA1
    [4]}> SHA224
    [5]}> SHA256
    [6]}> SHA384
    [7]}> SHA512
              [00]}> Back
              [99]}> exit
    ''')
                numper2 =  int(input(W+'Enter numper type hash:: '))
                if numper2 ==99:
                    break
                elif numper2 ==1:
                    nampas = raw_input('Enter text:: ')
                    nampas2 = nampas.encode('utf-8')
                    h = hashlib.new('md4')
                    h.update(nampas)
                    haa=h.hexdigest()
                    m = open('hash.txt','a').write('\n'+haa+'{{md4}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
                    print(haa,len(haa),nampas) 
                elif numper2 ==2:
                    nampas = raw_input('Enter text:: ')
                    nampas2 = nampas.encode('utf-8')
                    h = hashlib.new('md5')
                    h.update(nampas)
                    haa=h.hexdigest()
                    m = open('hash.txt','a').write('\n'+haa+'{{md5}}'+'\t{{'+nampas+'}}'+'{{'+str(len(haa))+'}}')
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
                elif numper2 == 00:
                    Matrix()
                   
                elif numper2 ==99:
                    break   
                    
                
        
            elif numper==2:
                slow(C+'''
    [1}>  MD5
    [2]}> SHA1
    [3]}> SHA224
    [4]}> SHA256
    [5]}> SHA384
    [6]}> SHA512

          [00]}> Back
          [99]}> exit 

    ''')
                num_c=  input(W+'Enter numper type hash:: ')
                if num_c ==1:
                    nampas = raw_input('Enter hash:: ')
                    list_f=  raw_input('Enter list :: ')
                    file_o= open(list_f,'r')
                    for f in file_o :
                        f = f.strip()
                        if hashlib.md5(f.encode()).hexdigest()==nampas:
                           print('CRACKED HASH::',f)
                           sleep(0)
                        else:
                            print('no crack found ',f)
                if num_c ==2:
                    nampas = raw_input('Enter hash:: ')
                    list_f=  raw_input('Enter list :: ')
                    file_o= open(list_f,'r')
                    for f in file_o :
                        f = f.strip()
                        if hashlib.sha1(f.encode()).hexdigest()==nampas:
                           print('CRACKED HASH::',f)
                           sleep(0)
                        else:
                            print('NO Crack found ',f)
                if num_c ==3:
                    nampas = raw_input('Enter hash:: ')
                    list_f=  raw_input('Enter list :: ')
                    file_o= open(list_f,'r')
                    for f in file_o :
                        f = f.strip()
                        if hashlib.sha224(f.encode()).hexdigest()==nampas:
                            print('CRACKED HASH::',f)
                            sleep(10)
                        else:
                            print('NO Crack found ',f)
                            
                
                if num_c ==4:
                    nampas = raw_input('Enter hash:: ')
                    list_f=  raw_input('Enter list :: ')
                    file_o= open(list_f,'r')
                    for f in file_o :
                        f = f.strip()
                        if hashlib.sha256(f.encode()).hexdigest()==nampas:
                            print('CRACKED HASH::',f)
                            sleep(0)
                        else:
                            print('NO Crack found ',f)
                
                if num_c ==5:
                    nampas = raw_input('Enter hash:: ')
                    list_f=  raw_input('Enter list :: ')
                    file_o= open(list_f,'r')
                    for f in file_o :
                        f = f.strip()
                        if hashlib.sha384(f.encode()).hexdigest()==nampas:
                            print('CRACKED HASH::',f)
                            sleep(0)
                        else:
                            print('NO Crack found ',f)
                if num_c ==6:
                    nampas = raw_input('Enter hash:: ')
                    list_f=  raw_input('Enter list :: ')
                    file_o= open(list_f,'r')
                    for f in file_o :
                        f = f.strip()
                        if hashlib.sha512(f.encode()).hexdigest()==nampas:
                           print('CRACKED HASH::',f)
                           sleep(0)
                        else:
                            print('NO Crack found ',f)
                elif num_c == 00:
                    Matrix()
                elif num_c ==99:
                    break
            elif numper ==3 :
                ty_h=raw_input(B+'Enter hash:: ')
                if len(ty_h)==32:
                    print(G+'Hash_Type::MD5')
                elif len(ty_h)==40:
                    print(G+'Hash_Type::SHA_1')
                elif len(ty_h)==56:
                    print(G+'Tash_Type::SHA_224')
                elif len(ty_h)==64:
                    print(G+'Hash_Type::SHA_256')
                elif len(ty_h)==96:
                    print(G+'Hash_Type::SHA_384')
                elif len(ty_h)==128:
                    print(G+'Hash_Type::SHA_512')
                else:
                    print(R+'Not Type Hash Found')
                 
            elif numper == 99:
                break
            else:
                Matrix()
                continue



                
                    
                 
                    
                    
        
                
                                   
        


                
                
                
         
         
        
             
                
            
    
            
        
            
            
                
    

    
  
            
            
    if __name__=='__main__':
        Matrix()
    
except KeyboardInterrupt:
    pass
except SyntaxError:
    print('FALSE ENTER ')
except NameError :
    pass
























#####################################################################################The-END#######################################################################################################################################################################################


