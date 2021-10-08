######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	2.0
# 		STA Team
# Comment:	This code is part of peer review flow and should create run hierarchy	
######

import config, os, sys, random
from subprocess import Popen, PIPE, STDOUT
from pathlib import Path

	
		
# Since there can be variouse type of blocks in different projects
# I write logic to determine the block name from lib names
def blocks():

	blocks = []
	report = {}

	for lib in os.listdir(config.path):
		if ".lib" in lib and "ss" in lib:
			lib_split = lib.split("_")
			i = 0
			name = ""
			while "ss" not in lib_split[i]:
				name = name + lib_split[i] + "_"
				i+=1
			blocks.append(name.rstrip("_"))
			
	blocks = list(set(blocks))
		
	return sorted(blocks)
