######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.1
# 		STA Team
# Comment:	This code is part of peer review flow and should check if permissions in release area are correct	
######

import config, os, sys
from pathlib import Path

class Permission:
	

# The function is for yielding every file in lib directory to then check for permission and group	
	def dir_files(self):
		
		for name in os.listdir(config.path):
			if not os.path.islink(config.path + "/" + name):
				yield config.path + "/" + name

# Function is collecting information about each file mode and group
# and then checking if the permissions or groups are correct
	def collector(self):
		
		location = str(Path(config.path)).split("/")
		revision_area = "/".join(location[0:-2])
		
		self.node_types = ["tsmc6ff", "tsmc5ff", "tsmc7ff", "tsmc3ff"]

		self.lib_mode_status = []
		self.group_status = []
		
		for name in self.dir_files():
			fmode =  os.stat(name)
			files = Path(name)
			name = name.split("/")[-1]
			if not self.mode_check(fmode):
				self.lib_mode_status.append("\"{}\" permission is not correct. Should be \"750\"".format(name))
			
			if not self.group_check(files):
				self.group_status.append("Node group of \"{}\" is \"{}\" which is not correct. It should be \"{}\"".format(name, files.group(), config.node))
				
		if not self.group_check(Path(revision_area)):
			self.group_status.append("Below revision directory is under wrong group \"{}\". It should be \"{}\"</p>\n<p>\"{}\"".format(Path(revision_area).group(), config.node, revision_area))
		
		return len(self.lib_mode_status + self.group_status)
		
# mode checking function is separated to not use twice. For files in lib and for revision area
	def mode_check(self, name):
		
		if oct(name.st_mode)[-3:] != "750" and "ss" not in config.node:
			mode_status = False
		elif oct(name.st_mode)[-3:] != "755" and "ss" in config.node:
			mode_status = False
		else:
			mode_status = True
			
		return mode_status
		
# Group checking function is separated to not use twice. For files in lib and for revision area
	def group_check(self, name):
		if name.group() == config.node and config.node in self.node_types:
			gstatus = True
		elif name.group() != config.node and config.node in self.node_types:
			gstatus = False
		elif name.group() != config.node and name.group() == "synopsys":
			gstatus = True
		else:
			gstatus = False
		
		return gstatus

# The function is for writing html file for permission check
	def permission_html_writer(self):
				
		with open("/u/davidas/nanotime/peer_review/source/html/permission.html", "r") as fr:
			html_read = fr.read()
			
		for line in self.group_status:
			html_read = html_read + "<p><span style=\"color:red;\"> ERROR: </span>" + line + "</p>\n"

		for line in self.lib_mode_status:
			html_read = html_read + "<p><span style=\"color:red;\"> ERROR: </span>" + line + "</p>\n"
		
		
		with open("peer_review/html_reports/permissions.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
