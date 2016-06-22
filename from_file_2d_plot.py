#!/usr/bin/env pytnon
# -*- coding: cp1251 -*-

# --------------------------
def from_file_plot(file_name):
	print 'in from_file_plot'
	
	import matplotlib.pyplot as plt
	from time import strftime
	import string
	import os
	import numpy as np

	# ----- Uncomment -----
	# dats_file_path = "/Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var)
	# os.chdir( os.getcwd()+ dats_file_path )
	# ---------------------

	# ----------------- making the data ------------------
	with open(file_name) as file_to_plot:
		data = file_to_plot.read()

	# data = data.replace('   ','\n') # uncomment if Bz_profile - in normal way
	data = data.replace('   ','')
	data = data.split('\n')
	data.pop()
	# print len(data)
	x=[]#['']*len(data)
	y=[]#['']*len(data)

	i = 1
	for string in data:
		string = string.strip()
		string = string.replace('  ',' ')
		x_val = string.split(' ')[0]
		x_val = float(x_val)
		x.append(x_val)
		y_val = string.split(' ')[1]
		y_val = float(y_val)
		y.append(y_val)
		print i, x_val, y_val, type(x_val)
		i +=1 

	print min(x), max(x)
	# ------------ graph building  ------------------
	x_min = min(x); x_max = max(x) 
	plt.xlim( x_min, x_max)
	plt.plot(x, y,label='Profile of magnetic field')
	# plt.plot(x, y)

	# plt.xlabel('X [cm]')
	# plt.xlabel(u'X [см]')
	# plt.ylabel('Magnet field (/bzt(80,1)) [Gs]')
	# plt.ylabel(u'Магнитное поле [Гс]')

	now_time = strftime("%d%b-%H.%M")
	# image_name = 'Bz_profile'+'_'+str(now_time)+'_'+variable_name+'_'+str(i)+'_'+str(var)+'.jpg'
	image_name = file_name+'_'+str(now_time)+'.jpg'
	
	print image_name
	print 'The gfaph ',image_name,' is builded.'
 	
	# plt.title(image_name)
	# plt.title('A profile of the magnetic fiels (when '+variable_name+' of the '+str(i+1)+' coil)'+' is '+str(var) +' (time: '+str(now_time)+')' )
	plt.title(file_name)
	plt.legend()
	plt.grid(True)
	plt.savefig(image_name)
	plt.show()

# --------------------------
from_file_plot("Bz_profile.dat")

# ------------------------------------------------------
# from os import listdir
# files = listdir(".")
# file_name_array = filter(lambda x: x.endswith('_2D.dat'), files)
# print "file_name_array:", file_name_array

# for file_name in file_name_array:
# 	from_file_plot(file_name)
# ------------------------------------------------------