def int_isvalid(a):
    try:
        int(a)
    except ValueError as err:
        return False
    return True

def myinput(msg,**kwargs):
    mode=0
    start=''
    end=''
    for key,value in kwargs.items():
        if key=="mode":
            mode=value
    if mode==0:
        return input(msg+"\n")
    if mode==1:
        num = ''
        while (num==''):
            try:
                return int(myinput("Enter an integer value"))
            except ValueError as err:
                print("value must be a valid integer")
        return num   
    if mode==2:
        pass
        
def Yn_input():
	ans = myinput("Y/n?")
	if ans.lower()=='y':
		return True
	else:
		return False
	
