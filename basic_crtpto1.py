string = 'EDVLF FUBSWR GUHDPKDFN'

for i in range(0,26):
    print('i=',i)
    ans = ''
    for s in string :
        if s ==' ' :
            ans += '_'
        else :
            n = ord(s)-i
            if(n<ord('A')) :
                n = n + 26
            ans += chr(n)
    print('ans=',ans)
    
    
    
