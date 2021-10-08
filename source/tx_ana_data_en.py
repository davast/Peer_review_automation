######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.1
# 		STA Team
# Comment:	This code is part of peer review flow and should check tx_ana_data_en is correctly defined in lane_ana libs	
######

import re, os

class Txanadata:

	def txanafinder(self):
		
		if os.path.isdir("peer_review/lane_ana/"):
			lib_path = "peer_review/lane_ana/"
		else:
			self.tx_ana = ""
			return "NA"
		
		files = ""

		self.missing_setup_rising = 0
		self.missing_hold_rising = 0
				
		for name in os.listdir(lib_path):
			if "lane_ana" in name:
				lib_name = name
				break
		
		lane_ana_abs = os.getcwd() + "/peer_review/lane_ana/" + lib_name
		
		with open(lane_ana_abs, "r") as fr:
			laneana_read = fr.read()
		
		tx_ana_reg = re.compile('(?ms)(    pin \(\"tx_ana_data_en\"\).*?)(    \}  \/\* End pin\(tx_ana_data_en\))')
		find_tx_ana = re.findall(pattern=tx_ana_reg, string=laneana_read)
		
		self.tx_ana = find_tx_ana[0][0]
		
		counter = 0
		
		if self.tx_ana.find("setup_rising"):
			counter = counter + 1
		if self.tx_ana.find("hold_rising"):
			counter = counter + 1
		
		
		setup_rising_reg = re.compile('(?ms)(        timing_type \: setup_rising \;.*?)(        \}  \/\* End rise_constraint)')
		find_setup_rising = re.findall(pattern=setup_rising_reg, string=self.tx_ana)
		
		
		try:
			setup_rising = find_setup_rising[0][0]
		except IndexError:
			self.missing_setup_rising = 1
			return "missing setup_rising"
		
		if len(setup_rising.split("\\")) > 3:
			counter = counter + 1
		
		hold_rising_reg = re.compile('(?ms)(        timing_type \: hold_rising \;.*?)(        \}  \/\* End rise_constraint)')
		find_hold_rising = re.findall(pattern=hold_rising_reg, string=self.tx_ana)
		
		
		try:
			hold_rising = find_hold_rising[0][0]
		except IndexError:
			self.missing_hold_rising = 1
			return "missing hold_rising"
		
		if len(hold_rising.split("\\")) > 3:
			counter = counter + 1
		
		
		if counter == 4:
			return "Pass"
		else:
			return "Fail" 
		
		
			
	def txanafinder_html_writer(self):
	
		with open("/u/davidas/nanotime/peer_review/source/html/tx_ana_data_en.html", "r") as fr:
			html_read = fr.read()
		
		if self.missing_setup_rising == 1:
			html_read = html_read + "<p><span style=\"color:red;\"> ERROR: </span>tx_ana_data_en pin exist in lane_ana libs, but it is missing setup_rising arc</p>\n"

		if self.missing_hold_rising == 1:
			html_read = html_read + "<p><span style=\"color:red;\"> ERROR: </span>tx_ana_data_en pin exist in lane_ana libs, but it is missing hold_rising arc</p>\n"
			
		self.tx_ana = self.tx_ana.replace("\n", "<br>")
		
		html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + self.tx_ana + "</p>\n"
			
		
		with open("peer_review/html_reports/tx_ana_data_en.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
		
