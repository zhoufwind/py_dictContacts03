import os,sys,re
from prettytable import PrettyTable

def f_insert(contacts):
	quit = False
	name = ''
	tel = ''
	comp = ''
	email = ''
	while True:
		name = raw_input("Insert Name: ").strip().lower()		# input name
		pattern = re.compile(r'^\w{2,16}$')	# r.e. checking if name format correct
		match = pattern.match(name)
		if contacts.has_key(name):		# Check origin data if user exist already
			print "\033[31;1mTHis user exist already!\033[0m"
			continue
		if len(name) == 0:
			print '\033[31;1mCANNOT NULL!\033[0m'		# name cannot empty
			continue
		elif name == 'q':
			quit = True
			break
		elif not match:
			print '\033[31;1mInvalid format!\033[0m'
			continue
		else:
			print "\033[32;1mInsert Name: \'%s\' done!\033[0m" % name
			break
	if quit == True:
		print "QUIT"
		return		# using 'return' return to main
	while True:
		tel = raw_input("Insert Telephone: ").strip().lower()			# input tel
		pattern = re.compile(r'^\d{11}$|^(0\d{2,3})\d{7,8}$')	# r.e. checking if tel format correct
		match = pattern.match(tel)
		if len(tel) == 0:
			# tel = ''			# tel can be empty, let it equal null if no input
			break
		elif tel == 'q':
			quit = True
			break
		elif not match:			# however, if format incorrect, need re-input
			print '\033[31;1mInvalid format!\033[0m'
			continue
		else:
			print "\033[32;1mInsert Telephone: \'%s\' done!\033[0m" % tel
			break
	if quit == True:
		print "QUIT"
		return
	while True:
		comp = raw_input("Insert Company: ").strip().lower()
		pattern = re.compile(r'^\w{2,32}$')		# r.e. checking if comp format correct
		match = pattern.match(comp)
		if len(comp) == 0:
			# comp = ''			# comp can be empty, let it equal null if no input
			break
		elif comp == 'q':
			quit = True
			break
		elif not match:			# however, if format incorrect, need re-input
			print '\033[31;1mInvalid format!\033[0m'
			continue
		else:
			print "\033[32;1mInsert Company: \'%s\' done!\033[0m" % comp
			break
	if quit == True:
		print "QUIT"
		return
	while True:
		email = raw_input("Insert Email: ").strip().lower()
		pattern = re.compile(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')	# r.e. checking if email format correct
		match = pattern.match(email)
		if len(email) == 0:
			# email = ''			# email can be empty, let it equal null if no input
			break
		elif email == 'q':
			quit = True
			break
		elif not match:			# however, if format incorrect, need re-input
			print 'Invalid format!'
			continue
		else:
			print "\033[32;1mInsert Email: \'%s\' done!\033[0m" % email
			break
	if quit == True:
		print "QUIT"
		return

	x = PrettyTable(["Name", "TEL", "Company", "Email"])
	x.add_row([name, tel, comp, email])
	x.align = "l"
	x.padding_width = 2
	print x
	contacts[name] = [tel, comp, email]		# insert user into dictionary
	# print contacts.items()

