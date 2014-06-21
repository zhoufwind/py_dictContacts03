import os,sys,re
from prettytable import PrettyTable

def f_insert(contacts):
	#print "This is insert function!", contacts.keys()
	while True:		# Name section, must enter!
		name = raw_input("Insert Name: ").strip().lower()
		if len(name) == 0: continue
		elif contacts.has_key(name):	# Check origin data if user exist already
			print "\033[31;1mTHis user exist already!\033[0m"
		elif len(name) < 2:
			if name == 'q':
				print "\033[31;1mCancel insert name, back to main page!\033[0m"
				break
			else:
				print "\033[31;1mUer name length must greater than 2 bytes\033[0m"
		print "Name OK! GO NEXT -- Tel"
		while True:		# Tel section
			tel = raw_input("Insert Tel(Press 'C' cancel): ").strip().lower()
			pattern = re.compile(r'^\d{11}$|^(0\d{2,3})\d{7,8}$')	# r.e. checking if tel format correct
			match = pattern.match(tel)
			# print match		# r.e. result -- True or False
			if len(tel) == 0: continue
			elif tel == 'c':
				tel = ''
				print "\033[31;1mCancel insert tel, GO NEXT page -- Company!\033[0m"
				break
			elif match == None:
				print "\033[31;1mInvalid Tel Number!\033[0m"
				continue
			print "Tel OK! GO NEXT -- Company"
			break
		# print tel
		while True:		# Company setction
			comp = raw_input("Insert Company(Press 'C' cancel): ").strip().lower()
			if len(comp) == 0: continue
			elif comp == 'c':
				comp = ''
				print "\033[31;1mCancel insert comp, GO NEXT page -- Email!\033[0m"
				break
			print "Company OK! GO NEXT -- Email"
			break
		# print comp
		while True:		# Email setction
			email = raw_input("Insert Email(Press 'C' cancel): ").strip().lower()
			if len(email) == 0: continue
			elif email == 'c':
				email = ''
				print "\033[31;1mCancel insert email, insert finish!\033[0m"
				break
			print "Company OK! Insert finish"
			break
		# print email
		break
	# print name, tel, comp, email
	x = PrettyTable(["Name", "TEL", "Company", "Email"])
	x.add_row([name, tel, comp, email])
	x.align = "l"
	x.padding_width = 2
	print x
	contacts[name] = [tel, comp, email]
	# print contacts.items()
