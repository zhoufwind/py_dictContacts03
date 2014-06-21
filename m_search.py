import os,sys
from prettytable import PrettyTable
import itertools

def f_preSearch(contacts):
	#print "This is precise search!", contacts.keys()
	while True:
		Psearch = raw_input("Search Name: ").strip().lower()
		if len(Psearch) == 0: continue
		if Psearch == 'q': break
		if contacts.has_key(Psearch):		# output account information if contacts have search content
			x = PrettyTable(["Name", "TEL", "Company", "Email"])
			x.add_row(["\033[32;1m%s\033[0m" % Psearch, contacts[Psearch][0], contacts[Psearch][1], contacts[Psearch][2]])
			x.align = "l"
			x.padding_width = 2
			print x
		else:		# error message
			print "\033[31;1mNo valid record...\033[0m"

def f_fuzSearch(contacts):
	#print "This is fuzzy search!", contacts.keys()
	while True:
		x = PrettyTable(["Name", "TEL", "Company", "Email"])
		Fsearch = raw_input("Fuzzy keyword: ").strip().lower()
		if len(Fsearch) == 0: continue
		if Fsearch == 'q': break
		info_counter = 0                        # matching count
		if len(Fsearch) < 2:
			print "\033[31;1mSearching keyword must greater than 1 word!"
			continue
		for name, value in contacts.items():	# first layer loop
			if name.count(Fsearch) != 0:		# If name contains searching keyword, print user
				p = name.find(Fsearch)
				x.add_row([name[:p] + "\033[32;1m%s\033[0m" % Fsearch + name[p + len(Fsearch):], value[0], value[1], value[2]])
				info_counter += 1
				continue
			#print "start second loop"
			for i in value:						# second layer loop
				if i.count(Fsearch) != 0:
					x.add_row([name, value[0], value[1], value[2]])		# output raws without highlight
					# ---BUG02: Cannot using highlight function show output---
					# line = name + '\t' + '\t'.join(value)	# find 'value' contains Fsearch, generate origin output
					# lineSplit = line.split(Fsearch)			# we need highlight Fsearch, so we split the whole output
					# print lineSplit
					# lineMeger = []			# create temp sequence
					# for j in lineSplit:		# loop adding each part to the temp sequence
					# 	lineMeger.append(j)	# adding each part to temp sequence
					# 	lineMeger.append('\033[32;1m%s\033[0m' % Fsearch)	# adding highlight part
					# lineMeger.pop()			# removing the highlight at end of the temp sequence
					# print lineMeger
					# lineFin = "".join(itertools.chain(*lineMeger))
					# print lineFin
					info_counter += 1
					break
		if info_counter == 0:
			print "No valid record..."
		else:
			x.align = "l"
			x.padding_width = 2
			print x
			print "Found %s records..." % info_counter

