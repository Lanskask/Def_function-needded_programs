#!/usr/bin/env pytnon
# -*- coding: cp1251 -*-

def from_file_plot(var, variable_name, i, data_to_graph_file):
	
	# import numpy as np
	import matplotlib.pyplot as plt
	import matplotlib.gridspec as gridspec
	from time import strftime
	# import string
	import os

	# ----- Uncomment -----
	cwd = os.getcwd()
	dats_file_path = "/Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var)
	os.chdir( os.getcwd()+ dats_file_path )
	# ---------------------

	# ----------------- making the data ------------------
	with open("Bz_profile.dat") as bz_profileDat:
		data = bz_profileDat.read()

	data = data.replace('   ','')
	data = data.split('\n')
	
	data.pop()
	# x = [row_pl.split('  ')[0] for row_pl in data]
	# y = [row_pl.split('  ')[1] for row_pl in data]
	x=[]#['']*len(data)
	y=[]#['']*len(data)

	# i = 1
	for string in data:
		string = string.strip()
		string = string.replace('  ',' ')
		x_val = string.split(' ')[0]
		x_val = float(x_val)
		x.append(x_val)
		y_val = string.split(' ')[1]
		y_val = float(y_val)
		y.append(y_val)
		# print i, x_val, y_val, type(x_val)
		# i +=1 
	
	y2 = [1]*len(y) # line: y = 1
	# print min(x), max(x)
	# ------------ graph building  ------------------
	x_min = min(x); x_max = max(x) 
	# x1= -0.04; x2 = 0.04
	# plt.xlim( x1, x2 )
	fig = plt.figure()
	# fig.subplots_adjust(top=0.85) # -------- ?
	egrid = (8,3)
	# ---------------
	# ax_1 = fig.add_subplot(211)
	ax_1 = plt.subplot2grid(egrid, (0, 0), colspan=3, rowspan=6)
	# ax_1 = ax_1.patch 
	# ax_1.xlim( x_min, x_max)
	ax_1.axis([x_min, x_max, min(y), max(y)])
	ax_1.plot(x, y,label='Profile of magnetic field')
	ax_1.plot(x, y2,label='y = 1')	

	# ax_1.xlabel('X [cm]') #	 ax_1.xlabel(u'X [см]')
	# ax_1.ylabel('Magnet field (/bzt(80,1)) [Gs]') 	# ax_1.ylabel(u'Магнитное поле [Гс]')
	ax_1.set_xlabel('X [cm]')
	ax_1.set_ylabel('Magnet field (/bzt(80,1)) [Gs]')

	now_time = strftime("%d.%m-%H.%M")
	image_name = 'Bz_profile'+'_'+str(now_time)+'_'+variable_name+'_'+str(i)+'_'+str(var)+'.jpg'
	
	# print 'image_name: ',image_name
	print 'The gfaph ',image_name,' is builded.'
	
	# ax_1.set_title('axes title') 	
	ax_1.set_title('A profile of the magnetic fiels (when '+variable_name+' of the '+str(i+1)+' coil) \n' 
		+' is '+str(var) +' (time: '+str(now_time)+').')
		 # \n' + 'When initial data is: \n'+data_to_graph_file)
	# ax_1.legend()
	ax_1.grid(True)
	# --------------------

	# ax_2 = fig.add_subplot(212)
	ax_2 = plt.subplot2grid(egrid, (7, 0), colspan=3, rowspan=1)
	ax_2.text(0.2, 0.4, 'Initial data:\n ' + data_to_graph_file)

	ax_2.set_frame_on(False)
	ax_2.axes.get_yaxis().set_visible(False)
	ax_2.axes.get_xaxis().set_visible(False)

	plt.tight_layout()
	plt.savefig('Testing_image.jpg')
	plt.savefig(image_name)
	plt.show()

	os.chdir(cwd)