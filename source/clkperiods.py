######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.0
# 		STA Team
# Comment:	This code is part of peer review flow and should check setup/hold vs clock periods 	
######

import os, sys
from subprocess import Popen, PIPE, STDOUT

class Clkperiods:

	def clockperiods(self):
	
		lib_path = "peer_review/"

		(output_cp, error_cp)  = Popen(["cp", "peer_review/bin/check_setup_hold_vs_clock_periods.pl", lib_path], stdout=PIPE, stderr=PIPE).communicate()
		
		(output_clk, error_clk)  = Popen("perl check_setup_hold_vs_clock_periods.pl *ana/*", stdout=PIPE, stderr=PIPE, cwd = lib_path, shell=True).communicate()
				
		try:
			with open("peer_review/timing_violations.csv", "r") as fr:
				csv_read = fr.read()
		except IOError:
			return 1
		
		self.warnings = []
		self.violation = []
		
		for line in csv_read.split("\n"):
			if "warning" in line:
				self.warnings.append(line + "\n")
			elif "violation" in line:
				self.violation.append(line + "\n")
		
		if len(self.warnings) == 0 and len(self.violation) == 0:
			return "Pass"
		elif len(self.warnings) != 0 and  len(self.violation) == 0:
			self.warnings = [name.replace("\n", "<br>") for name in self.warnings]
			return "Warnings"
		elif len(self.violation) != 0:
			self.warnings = [name.replace("\n", "<br>") for name in self.warnings]
			self.violation = [name.replace("\n", "<br>") for name in self.violation]
			return "Fail"

	def clockperiods_html_writer(self):
	
		with open("/u/davidas/nanotime/peer_review/source/html/clkperiods.html", "r") as fr:
			html_read = fr.read()
			
		if self.clockperiods() == "Warnings":
			for line in self.warnings:
				html_read = html_read + "<p><span style=\"color:blue;\"> WARNING: </span>" + line + "</p>\n"
		elif self.clockperiods() == "Fail":
			for line in self.warnings:
				html_read = html_read + "<p><span style=\"color:blue;\"> WARNING: </span>" + line + "</p>\n"
			for line in self.violation:
				html_read = html_read + "<p><span style=\"color:red;\"> ERROR: </span>" + line + "</p>\n"
			
		
		with open("peer_review/html_reports/clkperiods.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		
		
