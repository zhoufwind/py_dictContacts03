import os,sys

def f_delete(contacts):
	# print "This is delete function!", contacts.keys()
	while True:
		delete = raw_input("Enter the name you want to delete: ").strip().lower()
		if len(delete) == 0: continue
		elif delete == 'q':
			print "QUIT"
			break
		elif not contacts.has_key(delete):
			print "\033[31;1mUser isn't exist!\033[0m"
		else:
			confirm = raw_input("\033[31;1mDo you really want to delete \'%s\'? (Y/N): \033[0m" % delete).strip().lower()
			if confirm == 'n':
				continue
			else:
				contacts.pop(delete)
				print "\033[33;1mUser: \'%s\' have been deleted!\033[0m" % delete
				continue