######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.2
# 		STA Team
# Comment:	This code is part of peer review flow and should check libcompare 	
######

import re, os
from subprocess import Popen, PIPE, STDOUT

class Libcompare:

	def __init__(self, blocks):

		self.blocks = blocks

	def structural(self):
			
		report = {}
		self.sum_report = []
		
		self.matches = []
		self.lib_count = []
		
		for name in self.blocks:
			block_path = "peer_review/" + name

			(output_comp, error_comp)  = Popen("msip_hipreLibCompare -g", stdout=PIPE, stderr=PIPE, cwd = block_path, shell=True).communicate()
			output_comp = output_comp.decode('ascii')
			try:
				with open("peer_review/{}/msip_hipreLibCompare_RESULTS.SUM".format(name), "r") as fr:
					sum_read = fr.read()
					self.sum_report.append(sum_read)
			except IOError:
				return 1

			
			count_matches = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("matches"), sum_read))	
			self.matches.append(count_matches)

			lib_num = [name for name in os.listdir(block_path) if "lib" in name]
			count_libs = len(lib_num)
			self.lib_count.append(count_libs)
		
			if count_matches == count_libs - 1:
				report[name] = "pass"
			else:
				report[name] = "fail"
				
				
		if "fail" in report.values():
			return "Fail"
		else:		
			return "Pass"

	def structural_html_writer(self):
	
		with open("/u/davidas/nanotime/peer_review/source/html/structural.html", "r") as fr:
			html_read = fr.read()
		
		for i, rep in enumerate(self.sum_report):
			rep = rep.replace("\n", "<br>")
			
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: There are {} libs present in run directory and comparison done for {} libs</span></p>\n".format(self.lib_count[i] - 1, self.matches[i])
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + rep + "</p>\n"
			
		
		with open("peer_review/html_reports/structural.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
		
