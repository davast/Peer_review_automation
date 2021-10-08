######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.1
# 		STA Team
# Comment:	This code is part of peer review flow and should check PVT consistency between current and source releases 	
######

import config, os, sys

class Pvtcheck:

	def corners(self):
		
		
		self.current = [name for name in os.listdir(config.path) if ".lib" in name]
		
		self.source = [name for name in os.listdir(config.reference) if ".lib" in name]
				
		self.difference_with_source = list(set(self.current) - set(self.source))
		self.difference_with_current = list(set(self.source) - set(self.current))
		
		for i, diff in enumerate(self.difference_with_source):
			diff = diff.split(".")[0]
			self.difference_with_source[i] = "\"{}\" PVT is missing in source release. Please check".format(diff)
			
		for i, diff in enumerate(self.difference_with_current):
			diff = diff.split(".")[0]
			self.difference_with_current[i] = "\"{}\" PVT is missing in current release. Please check".format(diff)
					
		return len(self.current) - len(self.source)

	def pvtcheck_html_writer(self):
		
		
		with open("/u/davidas/nanotime/peer_review/source/html/pvtcheck.html", "r") as fr:
			html_read = fr.read()
		
		if len(self.current) - len(self.source) != 0:
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span> In current release there is \"" + str(len(self.current)) + "\" PVTs, which is not matching with source PVTs \"" + str(len(self.source)) +  "\"</p>\n"
			
		for line in self.difference_with_source:
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + line + "</p>\n"
		
		for line in self.difference_with_current:
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + line + "</p>\n"
		
		with open("peer_review/html_reports/pvtcheck.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
				
		
