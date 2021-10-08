######
# Developed by:	David Astvatsatryan
# Date:		August 2021
# Version:	1.0
# 		STA Team
# Usage:	Fill in config.py and run loader.sh
# Example:	./loader.sh
######

import config, sys, os
from subprocess import Popen, PIPE, STDOUT
from string import Template
from time import time

sys.path.insert(1, '/u/davidas/nanotime/peer_review_referance/source')

import structure
#from pathcheck import Pathcheck
#from permission import Permission
#from pvtcheck import Pvtcheck
#from clkperiods import Clkperiods
#from libcompare import Libcompare
from monotonicity import Hyprelib
#from minmax import Minmax
#from libvslib import Libvslib
#from pinattr import Libattributes
#from tx_ana_data_en import Txanadata
#from shivini import Shivini

class Main():
	
#	sys.tracebacklimit = None


	def top(self):

		start = time()
		print('\nINFO:	Starting Peer Review automated flow')
# Create structure
		
		hierarchy_structure = structure.hierarchy()
		print('INFO:	Copying libs and /bin in to local sandbox')
		filecollect_structure = structure.filecollect()
		
		
# Path existence part		
#		pathcheck_out = Pathcheck()
#		pathcheck_start = pathcheck_out.start()
		
#		print('INFO:	Release area {} specified in config file exist'.format(config.path))
#		print('INFO:	Source project {} specified in config file exist'.format(config.reference))
		
		
# Permission checking part	
#		print('INFO:	Checking correctness of permission and node group')	

#		permission_out = Permission()
#		permission_collector = permission_out.collector()
#		if permission_collector != 0:
#			print('ERROR:	Permission and node group checking finished with violations')
#			print('INFO:	Writing data in permission.html')	
#		else:
#			print('INFO:	Permission and node group check is finished')
			
		

#		permission_html = permission_out.permission_html_writer()

# PVT consistency part	
#		print('INFO:	Checking PVT consistency with source release')
			
#		pvtcheck_out = Pvtcheck()
#		pvtcheck_collector = pvtcheck_out.corners()
#		pvtcheck_html = pvtcheck_out.pvtcheck_html_writer()
#		
#		print('INFO:	PVT consistency check is done')

# Clock periods check part
		
#		print('INFO:	Running setup/hold vs clock periods check')
#		clkperiods_out = Clkperiods()
#		clkperiods_collector = clkperiods_out.clockperiods()
#		if clkperiods_collector == 1:
#			print('ERROR:	timing_violations.csv does not appear to exist.')
#		clkperiods_html = clkperiods_out.clockperiods_html_writer()
#		print('INFO:	setup/hold vs clock periods check finished')
		
# libcompare check part
	
#		print('INFO:	Running MSIP Hypre libcompare check')
#		libcompare_out = Libcompare()
#		libcompare_collector = libcompare_out.structural()
#		if libcompare_collector == 1:
#			print('ERROR:	msip_hipreLibCompare_RESULTS.SUM does not appear to exist.')
#		libcompare_html = libcompare_out.structural_html_writer()
#		print('INFO:	MSIP Hypre libcompare check finished')


# Monotonicity check part
		
		print('INFO:	Running MSIP Hypre Liberty Check for monotonicity. This may take a while')
		monotonicity_out = Hyprelib()
		monotonicity_collector = monotonicity_out.monotonicity()
		monotonicity_html = monotonicity_out.monotonicity_html_writer()
		print('INFO:	MSIP Hypre Liberty Check for monotonicity completed')
		

# min/max arc check part
	
#		print('INFO:	Running Library Compiler to check timing arcs have both MIN/MAX timing')
#		minmax_out = Minmax()
#		minmax_collector = minmax_out.checkarcs()
#		if minmax_collector == 1:
#			print('ERROR:	min_dly.tcl does not appear to exist.')
#		minmax_html = minmax_out.checkarcs_html_writer()
#		print('INFO:	Lib verification with Library Compiler is finished')


# libvslib check part
#		print('INFO:	Running Hypre Lib Versus Lib')
#		libvslib_out = Libvslib()
#		libvslib_collector = libvslib_out.hiprelibvslib()
#		libvslib_html = libvslib_out.hiprelibvslib_html_writer()
#		print('INFO:	Hypre Lib Versus Lib check is finished')

# libattr check part
#		print('INFO:	Running Hypre Lib Pin Attributes Check')
#		libattr_out = Libattributes()
#		libattr_collector = libattr_out.hiprelibattr()
#		libattr_html = libattr_out.hiprelibattr_html_writer()
#		print('INFO:	Hypre Lib Pin Attributes Check is finished')


# tx_ana_data_en check part
#		print('INFO:	Checking if tx_ana_data_en pin is correctly defined in lane_ana lib')
#		txanafinder_out = Txanadata()
#		txanafinder_collector = txanafinder_out.txanafinder()
#		if txanafinder_collector == "NA":
#			print('INFO:	tx_ana_data_en pin existance is skipped since tere is no lana ana libs')
#		elif txanafinder_collector == "missing setup_rising":
#			print('ERROR:	tx_ana_data_en pin exist in lane_ana libs, but it is missing setup_rising arc')
#		elif txanafinder_collector == "missing hold_rising":
#			print('ERROR:	tx_ana_data_en pin exist in lane_ana libs, but it is missing hold_rising arc')
#		else:
#			print('INFO:	tx_ana_data_en correctly exists in lane_ana lib')
#		txanafinder_html = txanafinder_out.txanafinder_html_writer()
		


# shivini structural diff check part
#		print('INFO:	Running Shivini structural diff between current and source libs')
#		structural_out = Shivini()
#		structural_collector = structural_out.structural()
#		if structural_collector == 1:
#			print('ERROR:	Summary report for structural diff does not exist')
#			print('ERROR:	Can not finish structural diff check for peer review')
#		else:
#			structural_html = structural_out.structural_html_writer()
#			print('INFO:	Shivini structural diff check is finished')
		



# Writing PASS/FAIL status and all top level information in main HTML
		with open("/u/davidas/nanotime/peer_review/source/html/top_report.html", "r") as fr:
			top_read = fr.read()
			
# pathcheck html writer
#		pathcheck_top_html = Template(top_read)
		
#		if pathcheck_start:
#			top_read = pathcheck_top_html.safe_substitute(pathcheck = "Directory exists")


# permission html writer
#		permission_top_html = Template(top_read)
		
#		if permission_collector == 0:
#			top_read = permission_top_html.safe_substitute(permission = "PASS")
#		else:
#			top_read = permission_top_html.safe_substitute(permission = "<span style=\"color:red;\"> FAIL </span>")

		
# pvtcheck html writer
#		pvtcheck_top_html = Template(top_read)

#		if pvtcheck_collector == 0:
#			top_read = pvtcheck_top_html.safe_substitute(pvtcheck = "PASS")
#		else:
#			top_read = pvtcheck_top_html.safe_substitute(pvtcheck = "<span style=\"color:blue;\"> Check Report </span>")


# Clock periods html writer

#		clkperiods_top_html = Template(top_read)
		
#		if clkperiods_collector == "Pass":
#			top_read = clkperiods_top_html.safe_substitute(clkperiods = "PASS")
#		elif clkperiods_collector == "Warnings":
#			top_read = clkperiods_top_html.safe_substitute(clkperiods = "Warnings")
#		else:
#			top_read = clkperiods_top_html.safe_substitute(clkperiods = "<span style=\"color:red;\"> FAIL </span>")


# libcompare html writer

#		libcompare_top_html = Template(top_read)
#		
#		if libcompare_collector == "Pass":
#			top_read = libcompare_top_html.safe_substitute(libcompare = "PASS")
#		else:
#			top_read = libcompare_top_html.safe_substitute(libcompare = "<span style=\"color:red;\"> FAIL </span>")



# monotonicity html writer
		
		monotonicity_top_html = Template(top_read)
		
		if monotonicity_collector == "Pass":
			top_read = monotonicity_top_html.safe_substitute(monotonicity = "PASS|Check Report")
		else:
			top_read = monotonicity_top_html.safe_substitute(monotonicity = "<span style=\"color:red;\"> FAIL </span>")


# min/max arc html writer

#		minmax_top_html = Template(top_read)
#		
#		if minmax_collector == "Pass":
#			top_read = minmax_top_html.safe_substitute(minmax = "PASS")
#		else:
#			top_read = minmax_top_html.safe_substitute(minmax = "<span style=\"color:blue;\"> WARNING </span>")


# libvslib html writer

#		libvslib_top_html = Template(top_read)
		
#		if libvslib_collector == "Pass":
#			top_read = libvslib_top_html.safe_substitute(libvslib = "PASS")
#		else:
#			top_read = libvslib_top_html.safe_substitute(libvslib = "<span style=\"color:red;\"> FAIL </span>")


# libattr html writer

#		libattr_top_html = Template(top_read)
#		
#		if libattr_collector == "Pass":
#			top_read = libattr_top_html.safe_substitute(libattr = "PASS")
#		else:
#			top_read = libattr_top_html.safe_substitute(libattr = "<span style=\"color:red;\"> FAIL </span>")


# tx_ana_data_en html writer

#		txanafinder_top_html = Template(top_read)
		
#		if txanafinder_collector == "Pass":
#			top_read = txanafinder_top_html.safe_substitute(txanafinder = "PASS")
#		elif txanafinder_collector == "NA":
#			top_read = txanafinder_top_html.safe_substitute(txanafinder = "Not Checked")
#		else:
#			top_read = txanafinder_top_html.safe_substitute(txanafinder = "<span style=\"color:red;\"> FAIL </span>")


# shivini structural diff check html writer

#		structural_top_html = Template(top_read)
#		
#		if structural_collector == "1":
#			top_read = structural_top_html.safe_substitute(structural = "FAIL")
#		else:
#			top_read = structural_top_html.safe_substitute(structural = "<span style=\"color:blue;\"> REPORT </span>")


					
		with open("peer_review/peer_review_report.html", "w") as fw:
			fw.write(top_read)
		
		(output_rm_cache, error_rm_cache)  = Popen(["rm", "-rf", "__pycache__"], stdout=PIPE, stderr=PIPE).communicate()
		end = time()
		print("INFO:	Complete peer review generation took {} sec".format(round(end - start)))
		print("INFO:	Thanks for useing this flow for peer review!")
		
		
if __name__ == '__main__':
	object = Main()

	top_func = object.top()
	
	
