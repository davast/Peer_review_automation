######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	2.0
# 		STA Team
# Comment:	This code is part of peer review flow and should create run hierarchy	
######

import config, os, getpass, sys, random
from subprocess import Popen, PIPE, STDOUT
from pathlib import Path


class Structure:
	
	counter = 0
	
	def __init__(self, blocks):

		self.blocks = blocks
		
		Structure.counter += 1

	def hierarchy(self):

		(output_rm_flow, error_rm_flow)  = Popen(["rm", "-rf", "peer_review"], stdout=PIPE, stderr=PIPE).communicate()
		(output_mkdir_flow, error_mkdir_flow)  = Popen(["mkdir", "peer_review"], stdout=PIPE, stderr=PIPE).communicate()
	
		for name in self.blocks:
			(output_mkdir_lib, error_mkdir_lib)  = Popen(["mkdir", "peer_review/" + name], stdout=PIPE, stderr=PIPE).communicate()
			(output_mkdir_str, error_mkdir_str)  = Popen(["mkdir", "peer_review/" + name + "/str"], stdout=PIPE, stderr=PIPE).communicate()	

		(output_mkdir_reports, error_mkdir_reports)  = Popen(["mkdir", "peer_review/html_reports"], stdout=PIPE, stderr=PIPE).communicate()	
		(output_cp_bin, error_cp_bin)  = Popen(["cp", "-r", config.proj_bin, "./peer_review"], stdout=PIPE, stderr=PIPE).communicate()


	def filecollect(self):
		worst_this = []
		worst_ref = []
		worst_volts = []
	
		for name in self.blocks:	
			for lib in os.listdir(config.path):
			
				isCorrectLib = name in lib and not os.path.islink(config.path + "/" + lib) and not "repeat" in lib # returns TRUE or FALSE
		
				if ".lib" in lib and isCorrectLib:
					(output_cp_lib, error_cp_lib)  = Popen(["cp", "-r", config.path+"/"+lib, "./peer_review/" + name], stdout=PIPE, stderr=PIPE).communicate()
				
				if ("125c_rcworst_Ccworst" in lib or "125c_rcworst_CCworst" in lib or "125c_SigRCmax" in lib) and "ss" in lib and isCorrectLib:
					worst_this.append(lib)

# finding lowest voltage				
		for worst in worst_this:
			worst_splited = worst.split("_")
			for item in worst_splited:
				if "p" in item and "c" in item and "v" in item:
					volt = item.split("v")[0].split("0p")[1]
					volt = "0p" + volt
					volt = volt.replace("p", ".")
					for char in volt:	
						if char.isalpha():
							volt = volt.replace(char, "")
			worst_volts.append(float(volt))
					
		min_volt = min(worst_volts)
		min_volt_p = str(min_volt).replace(".", "p")

# copy of lowest voltage worst corner
		final_list = [lib for lib in worst_this if min_volt_p in lib]
		for name in self.blocks:
			(output_cp_mindly, error_cp_mindly)  = Popen(["cp", "./peer_review/bin/min_dly.tcl", "./peer_review/" + name], stdout=PIPE, stderr=PIPE).communicate()
			blockLibs = list(filter(lambda lib: name in lib, os.listdir(config.reference))) # filtering referance libs that only related to current block in "for cycle" 
			randomLib = blockLibs[random.randint(0,len(blockLibs)-1)]
			for lib in final_list:
				if name in lib:
					print("INFO:	{} lib is choosen as worst corner for structural comparison".format(lib))
					(output_cp_lib, error_cp_lib)  = Popen(["cp", "-r", config.path+"/"+lib, "peer_review/" + name + "/str"], stdout=PIPE, stderr=PIPE).communicate()  # Copy of exact block lib

# copy of worst corner from referance lib 				
					real_path = os.path.realpath(config.reference+"/"+lib)
					if  os.path.isfile(real_path) and name in lib:
						(output_cp_lib, error_cp_lib)  = Popen(["cp", "-r", real_path, "peer_review/" + name + "/str" + lib + "_ref"], stdout=PIPE, stderr=PIPE).communicate()
					else:
						print("WARNING:	{} does not exist in reference project. Copying random lib from reference project".format(lib))
						(output_cp_lib, error_cp_lib)  = Popen(["cp", "-r", os.path.realpath(config.reference+"/"+randomLib), "peer_review/" + name + "/str/" + randomLib + "_ref"], stdout=PIPE, stderr=PIPE).communicate()
		
		
		

	def countMe(self):
		
		username = getpass.getuser()	
		countMe = Structure.counter
		
		
		with open("/u/davidas/nanotime/countme.txt", "r") as fr:
			readCount = fr.read()
				
		with open("/u/davidas/nanotime/countme.txt", "w") as fw:
		
			newUser = True if username not in readCount else False
			
			for line in readCount.split("\n")[0:-1]: #Dont want to take unwanted newline at the end of file
				if username in line and not newUser: #Checking if username is in current line and it is not new user
					num = line.split(":")[1].strip() 
					newNum = int(num) + countMe
					new_line = line.replace(str(num),str(newNum)+"\n")
					fw.write(new_line)
				elif newUser: # if it is new user, In file I am appending username and count information
					readCount = readCount + "{}		:{}\n".format(username,countMe)
					fw.write(readCount)
				else:
					fw.write(line + "\n") # if it is not new user and not the line I am searching for just appending that line
				
	
	
