import os,sys,re
from prettytable import PrettyTable

def f_update(contacts):
	# print "This is update function!", contacts.keys()
	while True:		# find user first
		x = PrettyTable(["Name", "TEL", "Company", "Email"])
		print contacts.keys()	# show all the keys/names FYI
		search = raw_input("Which account do you want to update?\nUser name: ").strip().lower()
		if len(search) == 0: continue
		elif search == 'q':
			break
		# print 'start searching'		# begin real searching
		elif contacts.has_key(search):
			# print 'found user'		# found user!
			print search +'\t' + '\t'.join(contacts[search])	# show user info briefly
			flag = False	# check if user have been updated, if not, don't show update result agian
			tel = contacts[search][0]	# init user's tel
			comp = contacts[search][1]	# init user's comp
			email = contacts[search][2]	# init user's email
			while True:
				cmd = raw_input("Which property do you want to update?\nTel(T), Company(C), Email(E): ").strip().lower()
				if len(cmd) == 0: continue
				elif cmd == 'q':
					break			# cancel this user's updating, return user select page
				elif cmd == 't':
					while True:
						flag = True		# table updated
						tel = raw_input("Update Telephone: ").strip().lower()	# update tel
						pattern = re.compile(r'^\d{11}$|^(0\d{2,3})\d{7,8}$')	# r.e. checking if tel format correct
						match = pattern.match(tel)
						if len(tel) == 0:
							tel = ''		# tel can be empty, let it equal null if no input
						elif not match:		# however, if format incorrect, need re-input
							print "\033[31;1mInvalid Tel Number!\033[0m"
							continue
						print "\033[32;1mUpdate Telephone: \'%s\' done!\033[0m" % tel
						break
					# print 'Tel: ', tel
				elif cmd == 'c':
					while True:
						flag = True		# table updated
						comp = raw_input("Update Company: ").strip().lower()
						pattern = re.compile(r'^\w{2,32}$')
						match = pattern.match(comp)
						if len(comp) == 0:
							comp = ''		# comp can be empty, let it equal null if no input
						elif not match:
							print "\033[31;1mInvalid Company Name!\033[0m"
							continue
						print "\033[32;1mUpdate Company: \'%s\' done!\033[0m" % comp
						break
					# print 'Company'
				elif cmd == 'e':
					while True:
						flag = True		# table updated
						email = raw_input("Update Email: ").strip().lower()
						pattern = re.compile(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$')
						match = pattern.match(email)
						if len(email) == 0:
							email = ''
						elif not match:
							print "\033[31;1mInvalid Email!!\033[0m"
							continue
						print "\033[32;1mUpdate Email: \'%s\' done!\033[0m" % email
						break
					# print 'Email'
			if flag:	# if any part of user info have been update, show the updated table
				print "\033[33;1mUser: \'%s\' have been updated!\033[0m" % search
				x = PrettyTable(["Name", "TEL", "Company", "Email"])
				x.add_row([search, tel, comp, email])
				x.align = "l"
				x.padding_width = 2
				print x
				contacts[search] = [tel, comp, email]		# insert user into dictionary
			else:
				print "\033[33;1mNo item have been updated!\033[0m"
		else:
			print "\033[31;1mUser isn't exist!\033[0m"

