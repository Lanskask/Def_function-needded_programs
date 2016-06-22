#!/usr/bin/python
# -*- coding: utf-8 -*-

### TODO
#   Interface - 1 and seccond
#   Use the old Input.dat file
#   C++ - QCustomPlot ?
#   import needed functions from sys, os, shutil
#   using from_file_plot the right one
#   
#   building a lot of graphs
#   +++ copy all graphs from folders to one folder +++
#   
#   dats_file_path for all functions
#   
### 
# ---------defs ------------------------------------------------
# from os import listdir
import shutil
from shutil import copy
import os

# import needed_functions
# from needed_functions import making_folders, copy_and_run_fortr_field_c, clean_str
from needed_functions import *
from from_file_plot import from_file_plot
from needed_functions import fromVariableToArray as sev_fr_one
# -----------------------------------------------

# ---------- opening and parsing file -----------
# def opening_and_parsing_input_file():
with open("input.dat") as inputDat:
    inpData = inputDat.read()
inputDat.close()

inpData = inpData.split('\n')
firstRow = inpData[0]
numOfCoils = firstRow.lstrip().split('  ')[0]
lastRow = inpData[4]
inpData = inpData[1:4]

data_to_graph_file = ''
for item in inpData:
    data_to_graph_file += item + '\n'
# print data_to_graph_file

for i in range( int(numOfCoils) ):
    inpData[i] = inpData[i].lstrip()
    # print inpData[i]

# ------ parsing data To variables --------
inRad           = [row.split('  ') [0] for row in inpData]
eternRad        = [row.split('   ')[1] for row in inpData]
coilHigh        = [row.split('   ')[2] for row in inpData]
currentDensity  = [row.split('   ')[3] for row in inpData]
coilCenter      = [row.split('   ')[4] for row in inpData]

inRad          = [float(i) for i in inRad]
eternRad       = [float(i) for i in eternRad]
coilHigh       = [float(i) for i in coilHigh]
currentDensity = [float(i) for i in currentDensity]
coilCenter     = [float(i) for i in coilCenter]
# # -------------- Interface for user to choose a variable -------
# print 'Choose a coil, which you want to study'
# coil_number = input('Print the number of coil you want to change (1, 2 or 3): ')
# # print 'There should be input of number of coil (default 1)'; coil_number = 1; # --- to commen to release
# if coil_number == 1 :
#     i = 0
# elif coil_number == 2 :
#     i = 1
# elif coil_number == 3 :
#     i = 2

# print 'Choose a variable of coil, which you want to study'
# print "inRad - 1, eternRad - 2, coilHigh - 3, currentDensity - 4, coilCenter - 5"
# variable_char_list = [ 'inRad', 'eternRad', 'coilHigh', 'currentDensity', 'coilCenter' ] 
# variable_list = [ inRad, eternRad, coilHigh, currentDensity, coilCenter ]
# choosen_variable_number = input('Print the number of variable you whant to change: ') 
# # print 'There should be input of choosen_variable_number (default 1)'; choosen_variable_number = 1; # --- to commen to release
# choosen_variable_number -= 1
# # ----
# choosen_variable = variable_list[choosen_variable_number][i]
# variable_name = variable_char_list[choosen_variable_number]
# print 'choosen_variable: ',variable_name,"[",i,"] = ", choosen_variable 

# # --------- Interface to input number_of_percents and step_number -------------
# number_of_percents = input('Input the range of changes of choosen variable in persents \n (default 10 %) : ')
# # number_of_percents = 10
# step_number = input('Input the quality of steps in whith you want tochange the variable (default 10) : ')
# # step_number = 3
# # -----------------------------------------------------------------------------

variable_char_list = [ 'inRad', 'eternRad', 'coilHigh', 'currentDensity', 'coilCenter' ] 
print "Variable_char_list: ", variable_char_list  # !!!!!!!!!!!!!!!!!!!!!!!!!!!
# choosen_variable_number = input('Print choosen_variable_number (1 -5): ') - 1 # !!!!!!!!!!!!!!!!!!!! for releasing
choosen_variable_number = 4 # !!!!!!!! for debuging
variable_name = variable_char_list[choosen_variable_number]
variable_list = [ inRad, eternRad, coilHigh, currentDensity, coilCenter ]

# print "Colomn of choosen_variable ("+variable_char_list[choosen_variable_number] +"): ", variable_list[choosen_variable_number] # !!!!!!!!!!!!!!!!!!!!!!!!!!!

# coil_number = input('Print coil_number (1 - 3): ') - 1 # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
coil_number = 2
choosen_variable = variable_list[choosen_variable_number][coil_number]
# print "The choosen_variable is - "+variable_char_list[choosen_variable_number]+" of coil ("+str(coil_number+1)+") is equel ", choosen_variable # !!!!!!!!!!!!!!!!!!!!!!!!!!!
print "Variable_list: ", variable_list
print "Choosen variable: ",variable_list[choosen_variable_number][coil_number] # !!!!!!!!!!!!!!!!!!!!!!!!!!!

number_of_percents = 90
step_number = 4
# print "Default now: Coil center of 3 coil. Num of %'s = 90. Step numper = 4"
# -----------------------------------------------------------------------------
for i in range( int(numOfCoils) ): # while i<3:
    inRad[i]          = '{:>8}'.format('%.3g' % inRad[i])       
    eternRad[i]       = '{:>7}'.format('%.3g' % eternRad[i])   
    coilHigh[i]       = '{:>7}'.format('%.3g' % coilHigh[i])     
    currentDensity[i] = '{:>12}'.format('%.3e' % currentDensity[i])         
    coilCenter[i]     = '{:>7}'.format('%.3g' % coilCenter[i])
# -------------------
 
j = 0
# print "making_folders('Graphs')" # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
making_folder_in_this_folder('Graphs')
for var in sev_fr_one(choosen_variable, number_of_percents, step_number):
    print "-------------Begin of Iteration j = "+str(j+1)+" --------------------"
    
    dats_file_path = dats_file_path_func( var, variable_name, i) 
    # print dats_file_path
    print "    Making_folders("+dats_file_path+"): "#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    making_folders(dats_file_path) 
    # -------- making file to write -----
    full_file_name = full_file_name_func(dats_file_path, "input.dat") 
    input_file = open(full_file_name, 'w') 

    input_file.write(firstRow+'\n') 

    variable_list[choosen_variable_number][coil_number] = var
    
    string=['']*int(numOfCoils) # 3
    for i in range( int(numOfCoils) ):
        string[i] = '   '
        for j in range( len(variable_list) ): # (5)
            string[i]+='  '+str(variable_list[j][i])
        # print string[i]
        input_file.write(string[i]+'\n')

    input_file.write(lastRow)
    input_file.close()
    # -------- End of making file to write -----

    # ---- Ploting --------
    # cwd = os.getcwd()
    copy_and_run_fortr_field_c( var, variable_name, i) # !!!!!!!!!!!!!!!!!!!!

    print 'should be ploting ' # !!!!!!!!!!!!!!!!!!!!!!!!!!!
    from_file_plot(var, variable_name, i, data_to_graph_file)
    prog_exit()
    # shutil.copy('field_c.out', dats_file_path + '\field_c.out' )    
    # ---- End of ploting --------
    # print "CWD: ", os.getcwd()

    print "-------------End of Iteration j = "+str(j+1)+" is done --------------------"
    j +=1

# copy_jpg_files()
# file_removing_func('field_c')