print('=====================================')
print('======={ FAT By Ali Baghban }========')
print('=====================================')
filename = input('file to decrypt => ')
print('=====================================')
#############################################
f = open(filename)
text = f.read()
f.close()
#############################################
def alphaCounter(text):
    alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
    'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,' ':0,}
    for ch in text :
        if ch == 'a':
            alpha['a'] = alpha['a']+1
        elif ch == 'b':
            alpha['b'] = alpha['b']+1
        elif ch == 'c':
            alpha['c'] = alpha['c']+1
        elif ch == 'd':
            alpha['d'] = alpha['d']+1
        elif ch == 'e':
            alpha['e'] = alpha['e']+1
        elif ch == 'f' :
            alpha['f'] = alpha['f']+1
        elif ch == 'g':
            alpha['g'] = alpha['g']+1
        elif ch == 'h':
            alpha['h'] = alpha['h']+1
        elif ch == 'i':
            alpha['i'] = alpha['i']+1
        elif ch == 'j':
            alpha['j'] = alpha['j']+1
        elif ch == 'k':
            alpha['k'] = alpha['k']+1
        elif ch == 'l':
            alpha['l'] = alpha['l']+1
        elif ch == 'm':
            alpha['m'] = alpha['m']+1
        elif ch == 'n' :
            alpha['n'] = alpha['n']+1
        elif ch == 'o':
            alpha['o'] = alpha['o']+1
        elif ch == 'p':
            alpha['p'] = alpha['p']+1
        elif ch == 'q':
            alpha['q'] = alpha['q']+1
        elif ch == 'r':
            alpha['r'] = alpha['r']+1
        elif ch == 's':
            alpha['s'] = alpha['s']+1
        elif ch == 't':
            alpha['t'] = alpha['t']+1
        elif ch == 'u':
            alpha['u'] = alpha['u']+1
        elif ch == 'v' :
            alpha['v'] = alpha['v']+1
        elif ch == 'w':
            alpha['w'] = alpha['w']+1
        elif ch == 'x':
            alpha['x'] = alpha['x']+1
        elif ch == 'y':
            alpha['y'] = alpha['y']+1
        elif ch == 'z':
            alpha['z'] = alpha['z']+1
        elif ch == ' ':
            alpha[' '] = alpha[' ']+1
        else:
            pass
    return alpha
alpha = alphaCounter(text)
print(alpha)
sss = ''
for item,val in alpha.items():
    sss = sss+item+" => "+str(val)+"\n"
#print(sss)
file = open('data.txt','w')
file.write(sss)
file.close()

#file = open('cipher.txt')
#text = file.read()
#text = text.replace('rn','th')
#text = text.replace('s','e')
#text = text.replace('dq','is')
#text = text.replace('d','a')
#text = text.replace('x','n')
#text = text.replace('j','t')

#file.close()

#file = open('plaintext.txt','w')
#file.write(text)
#file.close()
