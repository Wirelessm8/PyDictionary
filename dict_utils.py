from input_utils import *
from prettytable import PrettyTable  
import numpy as np

th =["№","Тоҷкӣ","Русский","Комметарий"]
def unique(a):
    ret = []
    for i in a:
        if not(i in ret):
            ret.append(i)
    return ret
    
#pick tags from a list by number
def num_to_tag(number,tags):
    tag=[]
    for i in number:
        tag.append(tags[i])
    return tag
    

def filt_by_tags(data,tags):
    res=[]
    for i in data:
        for j in tags:
            if j in i[3].split(","):
                res.append(i)
                break;
    return res

def collect_tags(data):
    tags=[]
    for i in data:
       
        temp=i[3].split(",")
        for j in temp:
            if not (j in tags):
                tags.append(j)
    return sorted(tags)

def choose_tags(data,tags):
    
    print("Choose tags to show")
    print("e.g. 1,2,3,5")
    for i in range(len(tags)):
        print(i+1,tags[i],sep=" : ",end = ".\n")
    chosen=unique(myinput("Enter list of numbers").split(","))
    for i in chosen:
        if not(int_isvalid(i)):
            print("All numbers must be integers")
            print("e.g. 1,2,3,6,5")
            return []
    res = []
    for i in chosen:
        res.append(int(i)-1)
    return res
    
def show(data):
	global th
	size = len(data)
	
	table = PrettyTable(th)
	for i in range(len(data)):
		row = [str(i+1),data[i][0],data[i][1],data[i][2]]
		table.add_row(row)
		
	print(table)	

def askword(data,mode):
	
	rnd=np.random.randint(0,len(data))
	if mode==1:
		print(data[rnd][0],end=": ")
		res = input()
		print(data[rnd][0],data[rnd][1],sep=" - ")
		return res
	if mode==2:
		print(data[rnd][1],end=": ")
		res = input()
		print(data[rnd][1],data[rnd][0],sep=" - ")
		return res
	if mode==3:
		new_mode=np.random.choice([1,2])
		return askword(data,new_mode)			
			





