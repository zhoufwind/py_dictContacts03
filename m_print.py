import os,sys
from prettytable import PrettyTable

def f_print(contacts):
	#print _contacts.keys()
	x = PrettyTable()
	x.field_names = ["Name", "TEL", "Company", "Email"]
	for k,v in contacts.items():
		x.add_row([k, v[0], v[1], v[2]])
	x.align = "l"
	#print x.get_string(sortby="Name")
	x.sortby = "Name"
	#x.reversesort = True
	#x.border = False
	#x.header = False
	x.padding_width = 2
	print x