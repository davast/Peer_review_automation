######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.0
# 		STA Team
# Comment:	This code is part of peer review flow and should check if paths specified in config file are correct, otherwise code will stop execution 	
######

import sys, config, os

abort = "\nINFO:\tAborting due to above error"

class Pathcheck:
	

	def start(self):
		
		if os.path.exists(config.path):
			correct_path = True
		else:
			raise NameError ( "Directory specified under \"path\" in config file does not exists" + abort)
			sys.exit(1)
		
		if os.path.exists(config.reference):
			correct_path = True
		else:
			raise NameError ( "Directory specified under \"source\" in config file does not exists" + abort)
			sys.exit(1)
		
		return correct_path
