'''
This program converts entered binary numbers into decimal numbers using the bindec function.
'''
def pow(n):
    po = [] # list to contain my indices.
    res = 0 # number to hold my final output.
    for i in range(len(list(n))):
        po.append(2 ** int(i))
    po1 = po[::-1]
    resu = map( lambda x, y : int(x) *  int(y) , n, po1)
    for i in resu:
        res += i
    print(res)

def bindec():

    num = [] #list to store my number from input
    inp = input("Enter The binary : ")# accepting user input

    # appending number to the list
    for i in list(inp):
        try:
            if int(i) >= 0 and int(i) <= 1:
                num.append(i)
            else:
                print("You have entered another number other than 1 and 0!!!")
                return

        except ValueError:
            print("You have entered another number other than 1 and 0!!!")
            break
    pow(inp)

bindec()
