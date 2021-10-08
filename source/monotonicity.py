######
# Developed by:	David Astvatsatryan
# Date:		June 2021
# Version:	1.2
# 		STA Team
# Comment:	This code is part of peer review flow and should check monotonicity of libs 	
######
				
import os, re
from subprocess import Popen, PIPE, STDOUT
#from structure import blocks

class Hyprelib:

	def __init__(self, blocks):

		self.blocks = blocks

	def monotonicity(self):
									
		report = {}
		self.mono_report = []

		for name in self.blocks:
			
			block_path = "peer_review/" + name
			(self.output_hyp, self.error_hyp)  = Popen("msip_hipreLibertyCheck -checkTiming -grid", stdout=PIPE, stderr=PIPE, cwd = block_path, shell=True).communicate()
			self.output_hyp = self.output_hyp.decode('ascii')
			
			self.mono_report.append(self.output_hyp)

			max_timing = re.compile('(?ms)(Largest max.*?)(ps)')
			find_max_timing = re.findall(pattern=max_timing, string=self.output_hyp)
			
			largest_error = re.compile('(?ms)(Largest error for.*?)(ps)')
			find_largest_error = re.findall(pattern=largest_error, string=self.output_hyp)
			
			find_max_timing = "".join([str(elem) for elem in list(find_max_timing)])
			find_largest_error = "".join([str(elem) for elem in list(find_largest_error)])
			
						
			if find_max_timing:
				max_timing_num = find_max_timing[find_max_timing.find(": ") + 2:find_max_timing.find(" ps")]
				max_timing_num = max_timing_num.split("',")[0].strip()
				
			else:
				print("ERROR:	Faild to get \"Largest max timing arc error\" for {} block".format(name))
				max_timing_num = "777"

			if find_largest_error:
				arc_types_num = find_largest_error[find_largest_error.find(": ") + 2:find_largest_error.find(" ps")]
				arc_types_num = arc_types_num.split("',")[0].strip()
			else:
				print("ERROR:	Faild to get \"Largest error for all timing arc types\" for {} block".format(name))
				arc_types_num = "777"
			
			
			if float(max_timing_num) < 10 and float(arc_types_num) < 10:
				report[name] = "pass"
			else:
				report[name] = "fail"
			
		
			
		if "fail" in report.values():
			return "Fail"
		else:		
			return "Pass"
		
	
	def monotonicity_html_writer(self):
				
		with open("/u/davidas/nanotime/peer_review/source/html/monotonicity.html", "r") as fr:
			html_read = fr.read()
		
		for line in self.mono_report:
			line = line.replace("\n", "<br>")
		
			html_read = html_read + "<p><span style=\"color:blue;\"> INFO: </span>" + line + "</p>\n"
		
		
		
		with open("peer_review/html_reports/monotonicity.html", "w") as fw:
			fw.write(html_read + "</body>\n</html>")	
		


