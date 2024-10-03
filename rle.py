s ="ABBBBCCCCCCCCAB"
count = 0
c = ''
pc = s[0]
rs = ''
l = len(s) 
i = 0
while (i!=l):
        chatacter = s[i]
        
        if pc == c:
            c += 1
        else:
            rs = rs + str(count) + pc
            count = 1

        pc = c
        i += 1
        
        print(rs + str(count) + str(pc))