######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.2
# 		STA Team
# Comment:	This code is part of peer review flow and should check timing arcs to have both MIN/MAX timing	
######

import os
from subprocess import Popen, PIPE, STDOUT

class Minmax:

	def __init__(self, blocks):

		self.blocks = blocks

	def checkarcs(self):
		
		lib_path = "peer_review/"
		lib_name = ""
		report = {}
		
		for name in self.blocks:

			try:
				with open("peer_review/{}/min_dly.tcl".format(name), "r") as fr:
					mindly = fr.readlines()
			except:
				self.output_run = ""
				return 1
		
			block_path = "peer_review/" + name
						
			for lname in os.listdir(block_path):
				if lname.endswith(".lib"):
					lib_name = lname
					break

			lib_abs = os.getcwd() + "/peer_review/" + name +"/"+ lib_name
		
			with open("peer_review/{}/min_dly.tcl".format(name), "w") as fw:
				for line in mindly:
					if line.find("set in ") != -1:
						new_line = line.replace(line, "set in {}\n".format(lib_abs))
						fw.write(new_line)
					else:
						fw.write(line)
		
			process = Popen( "lc_shell", shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE, cwd = block_path )
		
			(self.output_run, self.error_run) = process.communicate(b'source min_dly.tcl')
		
			self.output_run = self.output_run.decode('ascii')

		
			for line in self.output_run.split("\n"):
				if "PASS" in line:
					report[name] = "pass"
				elif "FAIL" in line:
					report[name] = "fail"

		if "fail" in report.values():
			return "Fail"
		else:		
			return "Pass"


	def checkarcs_html_writer(self):
		
		with open("/u/davidas/nanotime/peer_review/source/html/minmax.html", "r") as fr:
			html_read = fr.read()
			
		self.output_run = self.output_run.replace("\n", "<br>")
		
		html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + self.output_run + "</p>\n"
		
		
		
		with open("peer_review/html_reports/minmax.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		

