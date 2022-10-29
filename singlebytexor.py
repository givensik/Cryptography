
string = "54586b6458754f7b215c7c75424f21634f744275517d6d"

def findKey(string):

    for i in range(1,256):
        D = int(string[0:2],16)
        H = int(string[2:4],16)
        if(D ^ i == ord('D')) :
            if(H ^ i == ord('H')):
                #print("key = ",i)
                return i

def singlebyteXOR(string,key):
    answer = ''
    length = len(string)
    for i in range(0,length,2):
        if(length-i==1) :
            A = int(string[i],16)
        else:
            A = int(string[i:i+2],16)
        A = A ^ key
        #print(A)
        answer += chr(A)

    return answer

key = findKey(string)
print("key =", key)
print("answer =",singlebyteXOR(string,key))
