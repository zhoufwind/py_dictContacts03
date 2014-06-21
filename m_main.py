#!/usr/bin/env python

import os, sys, pickle
import m_print, m_search, m_insert, m_update, m_delete

print '''\033[34;1m
***Welcome to contact list***
	P   : Print users
	S   : Search user
	I   : Insert user
	U   : Update user
	D   : Delete user
	Q   : Quit/ Exit
***Enjoy it!***
\033[0m'''

_contacts = {}
_contacts_file = 'contacts.txt'
_contacts_binary = 'contacts.pickle'

with open (_contacts_file) as f:
	# f.readline()	# Ingore first line
	for i in f.readlines():
		line = i.strip().split()
		_contacts[line[0]] = line[1:]
with open (_contacts_binary, 'wb') as f:
	pickle.dump(_contacts, f)
with open (_contacts_binary, 'rb') as f:
	_entry = pickle.load(f)

def writeContact(contact):		# output mem to disk
	with open (_contacts_file, 'w') as f:
		f.writelines("")
		for k, v in contact.items():
			# print k, v[0], v[1], v[2]
			f = open(_contacts_file, 'a')
			f.writelines(k + '\t' + v[0] + '\t' + v[1] + '\t' + v[2] + '\n')

def main():
	while True:
		cmd = raw_input("Enter Command(\033[34;1mP\033[0m/\033[34;1mS\033[0m/\033[34;1mI\033[0m/\033[34;1mU\033[0m/\033[34;1mD\033[0m/\033[34;1mQ\033[0m): ").strip().lower()
		if len(cmd) == 0: continue
		elif cmd == 'p':
			m_print.f_print(_entry)
		elif cmd == 's':
			while True:
				searchMode = raw_input("\033[36;1mPrecise(P)\033[0m Search or \033[36;1mFuzzy(F)\033[0m Search or \033[36;1mQuit(Q)\033[0m?").strip().lower()
				if len(searchMode) == 0: continue
				elif searchMode == 'p':
					m_search.f_preSearch(_entry)
				elif searchMode == 'f':
					m_search.f_fuzSearch(_entry)
				elif searchMode == 'q':
					break
		elif cmd == 'i':
			m_insert.f_insert(_entry)
		elif cmd == 'u':
			m_update.f_update(_entry)
		elif cmd == 'd':
			m_delete.f_delete(_entry)
		elif cmd == 'q' or 'e':
			with open (_contacts_binary, 'wb') as f:
				pickle.dump(_entry, f)
			_contacts = _entry
			writeContact(_contacts)
			print '\033[33;1mHave a nice day! Goodbye!\033[0m'
			sys.exit()	# BUG01- If enter none of above, it also quit...

main()