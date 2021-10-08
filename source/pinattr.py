######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.1.
# 		STA Team
# Comment:	This code is part of peer review flow and should check msip_hipreLibPinAttributesCheck	
######

from subprocess import Popen, PIPE, STDOUT

class Libattributes:

	def __init__(self, blocks):

		self.blocks = blocks

	def hiprelibattr(self):
		
		report = {}
		
		for name in self.blocks:
			lib_path = "peer_review/" + name
		
		
			(self.output_attr, self.error_attr)  = Popen(["msip_hipreLibPinAttributesCheck"], stdout=PIPE, stderr=PIPE, cwd = lib_path).communicate()
		
			self.output_attr = self.output_attr.decode('ascii')


			if "FAILED" in self.output_attr:
				report[name] = "fail"
			elif "Error" in self.output_attr:
				report[name] = "fail"
			elif "ERROR" in self.output_attr:
				report[name] = "fail"
			else:
				report[name] = "pass"
		
		if "fail" in report.values():
			return "Fail"
		else:		
			return "Pass"
			
			
	def hiprelibattr_html_writer(self):
	
		with open("/u/davidas/nanotime/peer_review/source/html/pinattr.html", "r") as fr:
			html_read = fr.read()
			
		self.output_attr = self.output_attr.replace("\n", "<br>")
		
		html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + self.output_attr + "</p>\n"
			
		
		with open("peer_review/html_reports/pinattr.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
		
