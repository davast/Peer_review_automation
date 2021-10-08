######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.2
# 		STA Team
# Comment:	This code is part of peer review flow and should check structural diff with shivini script 	
######

import os, sys
from subprocess import Popen, PIPE, STDOUT

class Shivini:

	def __init__(self, blocks):

		self.blocks = blocks
	
	def structural(self):
		
		try:
			with open("peer_review/bin/Shivini_lib_vs_lib/Shivini.pl", "r") as fr:
				file_read = fr.read()
		except IOError:
			print("ERROR	\"Shivini_lib_vs_lib/Shivini.pl\" does not exist. Please check bin directory")
			return 1


		try:
			with open("peer_review/bin/get_summary_struct_diffs.pl", "r") as fr:
				file_read = fr.read()
		except IOError:
			print("ERROR	\"get_summary_struct_diffs.pl\" does not exist. Please check bin directory")
			return 1
		
		
		self.report = []
					

		for name in self.blocks:
			str_path = "peer_review/{}/str/".format(name)
			
			libs = os.listdir(str_path)
			for item in libs:
				if "ref" not in item:
					new_lib = item
				else:
					old_lib = item
			
			corner = new_lib.split(".")[0]
		
			print("INFO:   For {} block Shivini structural diff is running on {}".format(name, corner))
			(output_str, error_str)  = Popen("perl  ../../bin/Shivini_lib_vs_lib/Shivini.pl {} {}".format(new_lib, old_lib), stdout=PIPE, stderr=PIPE, cwd = str_path, shell=True).communicate()
			
			output_str = output_str.decode('ascii')

			for line in output_str.split("\n"):
				if "txt" in line:
					struct_file = str(line).split(":")[-1].strip()
					
			
			print("INFO:   Creating summary report for structural check")					
			(output_sum, error_sum)  = Popen("perl  ../../bin/get_summary_struct_diffs.pl {}".format(struct_file), stdout=PIPE, stderr=PIPE, cwd = str_path, shell=True).communicate()
			
			try:
				with open("peer_review/{}/str/{}.diff.txt.summary.txt".format(name, new_lib), "r") as fr:
					lib_read = fr.read()
					self.report.append(lib_read)
			except IOError:
				print("ERROR	Output file from shivini run does not exist. Please check run directory or run it manually")
				self.report = []
				return 1
			
			if "Missing timing arcs" in lib_read:
				print("WARNING:   There are missing timing arcs in summary report of Shivini structural check for {}".format(name))
				print("WARNING:   Please check report in peer_review/peer_review_report.html")
			
			
			
	def structural_html_writer(self):
	
		with open("/u/davidas/nanotime/peer_review/source/html/shivini.html", "r") as fr:
			html_read = fr.read()
		
		for i, block in enumerate(self.blocks):
			html_read = html_read + "<p><b>" + block + "</b></p>\n"
			block_message = self.report[i].replace("\n", "<br>")
			html_read = html_read + block_message
		
		with open("peer_review/html_reports/shivini.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
		
