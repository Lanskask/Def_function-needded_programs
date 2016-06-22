import os
from os import mkdir, path
from sys import platform
import subprocess
import shutil
from shutil import copy
# from several_variables_from_one import fromVariableToArray as sev_fr_one
def dats_file_path_func( var, variable_name, i):
    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        dats_file_path = "./Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var)
        print "dats_file_path: "+dats_file_path +'/field_c.out'
    elif platform == 'win32':
        dats_file_path = ".\Graphs\DATs_"+variable_name+'_'+str(i)+'_'+str(var)
        print "dats_file_path: "+dats_file_path +r'\field_c.exe'
    else: 
        print("undefined Operational System")
    return dats_file_path

def full_file_name_func(dats_file_path, file_name_to_full): # 'input.dat'
    print "    Dats f Path: "+dats_file_path
    full_file_name = dats_file_path+"/input.dat"
    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        full_file_name = dats_file_path+"/"+file_name_to_full
    elif platform == 'win32':
        full_file_name = dats_file_path+"\ ".strip()+file_name_to_full
    else: 
        print("undefined Operational System")
    return full_file_name

def making_folder_in_this_folder(variable): # 'Graphs'
    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        print "1 SubFolder to make: "+'/'+variable
        dir_name = './'+variable
    elif platform == 'win32':
        print "1 SubFolder to make: "+'.\ '.strip()+variable
        dir_name = '.\ '.strip()+variable
    else: 
        print("undefined Operational System")
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
        print "Directorie "+dir_name+" is created."

def making_folders(variable): # return ('.\Graphs'), (dats_file_path)
    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        dir_name = './'+variable
    elif platform == 'win32':
        print "Folder to make: "+variable # '.\ '.strip()+variable
        dir_name = variable # '\ '.strip()+variable
    else: 
        print("undefined Operational System")
    # if os.path.exists(variable) == False:
    #     os.mkdir(variable)
    if os.path.exists(dir_name) == False:
        os.mkdir(dir_name)
        print "Directorie "+dir_name+" is created."

def compile_fortr_field_c():
    if platform == 'linux' or platform == 'linux2':
        subprocess.call('prog_name=field_c \n gfortran $prog_name.f90 -o $prog_name.out') 
    elif platform == 'win32':
        subprocess.call('set prog_name=field_c gfortran %prog_name%.f90 -o %prog_name%.exe')
    return 

def copy_and_run_fortr_field_c( var, variable_name, i): # dats_file_path
# def copy_and_run_fortr_field_c(dats_file_path, var):
    # shutil.copy('./field_c.out', './Graphs/DATs_'+str(var)+'/field_c.out' )
    # dats_file_path = "/Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var)

    from sys import platform
    if platform == 'linux' or platform == 'linux2':
        dats_file_path = "/Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var)
        shutil.copy('./field_c.out', dats_file_path +'/field_c.out' )
        print dats_file_path +'/field_c.out'
    elif platform == 'win32':
        dats_file_path = ".\Graphs\DATs_"+variable_name+'_'+str(i)+'_'+str(var)
        print "    In func Copy_and_run_Fortr dats_file_path: \n\t",dats_file_path, type(dats_file_path)
        shutil.copy(r'.\field_c.exe', dats_file_path +r'\field_c.exe' )
        print dats_file_path +r'\field_c.exe'
    else: 
        print("undefined Operational System")

    # shutil.copy('./field_c.out', '.'+dats_file_path +'/field_c.out' )
    # print dats_file_path +'/field_c.out'
    cwd = os.getcwd()
    os.chdir( os.getcwd()+ dats_file_path )
    print '2: ',dats_file_path
    # os.chdir( os.getcwd()+ "/Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var) )
    if platform == 'linux' or platform == 'linux2':
       	command = './field_c.out'
    elif platform == 'win32':
        command = 'field_c.exe'
    subprocess.call(command) 
    os.chdir(cwd)
    print 'Command: '+command+' in folder: '+ dats_file_path+' - is evaluated'
    return 

def clean_str(file_str):
	# from sys import platform
	symbles = [',','\'','[',']','(',')']
	for x in symbles:
		file_str = file_str.replace(x,'')
	return file_str	

def fromVariableToArray(var_initial, number_of_percents = 10, step_number = 10):
	minus_part = var_initial/number_of_percents # this part we need to minus from the initial value of a variable to begin with
	var_changeble = var_initial - minus_part # initial value of variable from with we begin this colculating 
	step = var_initial/number_of_percents/step_number*2 # the value ofthe step 
	vars_array = [] 
	for i in range(1,step_number + 2):
		vars_array.append(round(var_changeble,4))
		var_changeble = var_changeble +step
	# print vars_array, type(vars_array[1])
	return vars_array

def file_removing_func(file_to_remove_name='field_c'):
    cwd1 = os.getcwd()
    os.chdir(cwd1+'\Graphs')
    cwd2 = os.getcwd()
    print "cwd2= " + cwd2
    folder_list = os.listdir(cwd2)
    # print folder_list
    # print '------- Begin removing loop ----------'

    if platform == 'linux' or platform == 'linux2':
            file_to_remove_name = './'+file_to_remove_name+'.out'
    elif platform == 'win32':
        file_to_remove_name = r'\ '.strip()+file_to_remove_name+'.exe'

    for folder in folder_list:
        # print " CWD: "+os.getcwd()
        filename = folder + file_to_remove_name #raw_input("Type file name to remove: ")
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print "File"+filename+" is removed."
            except OSError, e:
                print ("Error: %s - %s." % (e.filename,e.strerror))
            else:
                print("Sorry, I can not find %s file." % filename)
        os.chdir(cwd2)      

def prog_exit():
    import sys
    sys.exit()

def copy_jpg_files():
    import os 
    os.chdir("Graphs")
    cwd_Graph = os.getcwd()
    everthing_in_Graph = os.listdir(os.getcwd())[1:-1]
    # print "-- Cwd_Graph", cwd_Graph # Graph folder
    print everthing_in_Graph
    DATs_folders = filter( lambda x: x.startswith('DATs_'), os.listdir(os.getcwd()) )
    # print DATs_folders
    for folder_in_Gr in DATs_folders:
        # print "folder_in_Gr: ", folder_in_Gr
        os.chdir(folder_in_Gr)
        # print "os.getcwd(): ", os.getcwd()
        
        jpg_file_in_fold = filter( lambda y: y.endswith('.jpg'), os.listdir(os.getcwd()) )
        print "jpg_file_in_fold: ", jpg_file_in_fold
        for jpg_file in jpg_file_in_fold:
            if platform == 'linux' or platform == 'linux2':
                # shutil.copy(folder_with_jpg_cwd+'/'+file, '../All_Graphs'+file )
                shutil.copy(jpg_file, '../All_Graphs/'+jpg_file )
            elif platform == 'win32':
                shutil.copy('.\ '.strip()+jpg_file, '..\All_Graphs\\'+jpg_file )
        os.chdir("..")
    prog_exit()