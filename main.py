import numpy as np

import dict_utils as du
from input_utils import *

comm = "-2"

data_path="data/"
data_name="dict"

dict_all=[]
dict_filtered=[]


def Debug(*args):
	print("Debug:",*args)


def change_path():
	print("Do you want to change path?")
	if (Yn_input()):
		data_path=myinput("Enter new path")
		print("Path set to ",data_path)
	print("Change dict name?")
	if (Yn_input()):
		data_name=myinput("Enter new name")
		print("name set to ",data_name)
		

def data_filter():
	global dict_filtered,dict_all
	tags=du.collect_tags(dict_all)
	chosen=du.choose_tags(dict_all,tags)
	tags_mask=du.num_to_tag(chosen,tags)
	dict_filtered=du.filt_by_tags(dict_all,tags_mask)
	print(len(dict_filtered)," were selected, show them?")
	if (Yn_input()):
		du.show(dict_filtered)
	

def data_load():
	global dict_all
	dict_all = np.genfromtxt(data_path+data_name,delimiter = ';',dtype=str)
	print("Total number of loaded items: ",len(dict_all))
	print("Show all?")
	if (Yn_input()):
		du.show(dict_all)



def test():
	global dict_filtered,dict_all
	if len(dict_all)==0:
		print("Dictionary must be loaded first, use L to Load")
		return 0
	print("what language should the words be asked in?")
	print("1.",du.th[1])
	print("2.",du.th[2])
	print("3. both")
	mode = 0
	while (mode>3 or mode<1):
		mode = myinput("Enter mode",mode=1)
	
	print("How much times? 0 for until zero")
	option = myinput("Enter an integer value",mode=1)
	
	
	entire = myinput("Use entire dict? 1 - yes, any other - no")
	if entire=="1":
		using_dict=dict_all
	else:
		using_dict=dict_filtered
	if len(dict_filtered)==0:
		print("Filter words first")
		return 0
	
	if option:
		for i in range(option):
			du.askword(using_dict,mode)
	else:
		while du.askword(using_dict,mode)!="0":
			pass
def help():
	print("This is a dictonary using python")
	print("-1,H - shows this page")
	print("1,Load,L - load")
	print("2,Add,Append - \tadd")
	print("ChP,3 - change path ")
	print("0,q - exit")
	print("filt - filter words")
	print("test - for testing")



while not(comm in ["0","q"]):
	comm = myinput("Enter command, -1 or H for help, 0 to exit")
	if comm in ["-1","H"]:
		help()
	if comm in ["3","ChP"]:
		change_path()
	if comm in ["1","L","Load"]:
		data_load()
	if comm.lower() in ["filt"]:
		data_filter()
	if comm.lower() in ["test"]:
		test()

print("Goodbye")
	
