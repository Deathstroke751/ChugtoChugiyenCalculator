import requests 
import os

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def prred(skk): print("\033[91m {}\033[00m" .format(skk))
def prgreen(skk): print("\033[92m {}\033[00m" .format(skk))
def pryellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prlightpurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prpurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prcyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prlightgray(skk): print("\033[97m {}\033[00m" .format(skk))
def prblack(skk): print("\033[98m {}\033[00m" .format(skk))

def selector():

    def initial(a,b):
        a = float(a)
        b = float(b)
        c = (100*a)/(100+b)
        return c

    def final(a,b):
        a = float(a)
        b = float(b)
        c = (a*100+a*b)/100
        return c

    def percentage(a,b):
        a = float(a)
        b = float(b)
        c = 100*(a-b)/b
        return c

    def compound(a,b,c):
        a=float(a)
        b=float(b)
        c=int(c)
        i=1
        print('')
        heyyow = ''
        while c >= i:
            d = (a*100+a*b)/100
            d = float("{:.2f}".format(d))
            #print(f"\033[96mDay {i}\033[00m : \033[92m{d}\033[00m")
            heyyow += f"\033[96mDay {i}\033[00m : \033[92m{d}\033[00m\n"
            
            #Milestones
            if d<=10 and 10<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 10\033[00m\033[0m")
            if d<=100 and 100<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 100\033[00m\033[0m")
            if d<=1000 and 1000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 1,000\033[00m\033[0m")
            if d<=10000 and 10000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 10,000\033[00m\033[0m")
            if d<=100000 and 100000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 100,000\033[00m\033[0m")
            if d<=1000000 and 1000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 1,000,000\033[00m\033[0m")
            if d<=10000000 and 10000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 10,000,000\033[00m\033[0m")
            if d<=100000000 and 100000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 100,000,000\033[00m\033[0m")
            if d<=1000000000 and 1000000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 1,000,000,000\033[00m\033[0m")
            if d<=10000000000 and 10000000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 10,000,000,000\033[00m\033[0m")
            if d<=100000000000 and 100000000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 100,000,000,000\033[00m\033[0m")
            if d<=1000000000000 and 1000000000000<(d*100+d*b)/100:
                print(f"\033[1m\033[95mDay {i} : Crossed 1,000,000,000,000\033[00m\033[0m")

            i += 1
            a = d
        print('')    
        print(heyyow)
    clear()
    print(''' \033[91m    
    ░█████╗░███╗░░██╗████████╗██╗░░██╗░█████╗░██████╗░░█████╗░  ██╗░░░░░░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗████╗░██║╚══██╔══╝██║░░██║██╔══██╗██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝
    ███████║██╔██╗██║░░░██║░░░███████║███████║██║░░██║███████║  ██║░░░░░██║░░██║██║░░██║█████═╝░
    ██╔══██║██║╚████║░░░██║░░░██╔══██║██╔══██║██║░░██║██╔══██║  ██║░░░░░██║░░██║██║░░██║██╔═██╗░
    ██║░░██║██║░╚███║░░░██║░░░██║░░██║██║░░██║██████╔╝██║░░██║  ███████╗╚█████╔╝╚█████╔╝██║░╚██╗
    ╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝  ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝

        ░█████╗░██╗░░██╗███████╗██╗░░░██╗██╗░░░██╗███╗░░██╗███╗░░██╗███████╗  ░█████╗░
        ██╔══██╗██║░░██║██╔════╝╚██╗░██╔╝██║░░░██║████╗░██║████╗░██║██╔════╝  ██╔══██╗
        ██║░░╚═╝███████║█████╗░░░╚████╔╝░██║░░░██║██╔██╗██║██╔██╗██║█████╗░░  ╚═╝███╔╝
        ██║░░██╗██╔══██║██╔══╝░░░░╚██╔╝░░██║░░░██║██║╚████║██║╚████║██╔══╝░░  ░░░╚══╝░
        ╚█████╔╝██║░░██║███████╗░░░██║░░░╚██████╔╝██║░╚███║██║░╚███║███████╗  ░░░██╗░░
        ░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝  ░░░╚═╝░░
     \033[00m''')

    choice = {
    '1' : 'pc', 
    '2' : 'ia', 
    '3' : 'fa',
    '4' : 'cc',
    '5' : 'bei'
    }
    
    print("\033[96m1. Calculate Percent Change\n2. Calculate Initial Amount\n3. Calculate Final Amount\n4. Compound Calculator\n5. Exit\033[00m")

    opsen = input('\n\033[93mSelect seyy : \033[00m')
    id = choice.get(opsen,'invalid')        

    if id == 'pc':
        clear()
        initial = input("Enter initial amount - ")        
        final = input("Enter final amount - ")
        print(percentage(final,initial)," is the percentage change.")

    elif id == 'ia':
        clear()
        final = input("Enter final amount - ")        
        percent = input("Enter percent change - ")
        print(initial(final,percent)," is the initial amount.")

    elif id == 'fa':
        clear()
        initial = input("Enter initial amount - ")        
        percent = input("Enter percent change - ")
        print(final(initial,percent)," is the final amount.")    

    elif id == 'cc':
        clear()
        init = input("Enter initial amount - ")
        percent = input("Enter percent change - ")        
        final = input("Enter number of days - ")
        compound(init,percent,final)    

    elif id == 'bei':
        exit()

    else:
        print("\n\033[91mInvalid response anedaw. Try again.\033[00m ",end='')
    
while True:
    selector()
    input()