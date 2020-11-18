response=["Hello My Name is Addam","Welcome to Smart Calculator","Iam Sorry","Hello Sir How Can i Help You","This is beyond My Ability","THANKS"]
def extract(text):
    l=[]
    for i in text.split(' '):
        try:
            l.append(float(i))
        except ValueError:
             pass
    return l  
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def lcm(a,b):
    L=a if a>=b else b
    while(L<=a*b):
        if l%a==0 and L%b==0:
            return L
         
    l+=1
def hcf():
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
    h-=1
def div(a,b):
    return a/b
def sorry():
    print(response[2])
def name():
    print(response[0])
def addam():
    print(response[3])
def end():
    print(response[5])
    input("enter any key for exit")
    exit()
    
operation={"ADD":add,"SUMATION":add,"SUM":add,"+":add,"-":sub,"MINUS":add,"PLUS":add,"SUBTRACTION":sub,"MULTIPLY":mul,"*":mul,"MULTIPLICATION":mul,"HCF":hcf,"LCM":lcm,"DIVISON":div,"/":div,"D":div,"DIVIDE":div}
comands={"END":end,"EXIT":end,"CLOSE":end,"NAME":name,"HELLO":addam,"HI":addam,"CLOSE":end}
    
