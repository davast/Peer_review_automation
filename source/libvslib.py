######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.2
# 		STA Team
# Comment:	This code is part of peer review flow and should check msip_hyprelibvslib	
######

import os
from subprocess import Popen, PIPE, STDOUT

class Libvslib:

	def __init__(self, blocks):

		self.blocks = blocks

	def hiprelibvslib(self):
	
		report = {}
		
		self.lvl_report = []
		
		for name in self.blocks:
			
			block_path = "peer_review/" + name
			(self.output_lvl, self.error_lvl)  = Popen(["msip_hipreLibVsLib"], stdout=PIPE, stderr=PIPE, cwd = block_path).communicate()
		
			self.output_lvl = self.output_lvl.decode('ascii')
			self.lvl_report.append(self.output_lvl)


			if self.output_lvl.count("PASSED") == 2:
				report[name] = "pass"
			else:
				report[name] = "fail"
			
		if "fail" in report.values():
			return "Fail"
		else:		
			return "Pass"
			
	def hiprelibvslib_html_writer(self):
	
		with open("/u/davidas/nanotime/peer_review/source/html/hiprelibvslib.html", "r") as fr:
			html_read = fr.read()
		
		for report in self.lvl_report:	
			report = report.replace("\n", "<br>")
		
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + report + "</p>\n"
			
		
		with open("peer_review/html_reports/hiprelibvslib.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
		
