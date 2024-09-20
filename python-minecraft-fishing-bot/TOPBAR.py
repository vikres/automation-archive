import PySimpleGUI as sg      
import subprocess      
import os      
import sys      
var1 = 0
"""      
    Demo_Toolbar - A floating toolbar with quick launcher     One cool PySimpleGUI demo. Shows borderless windows, grab_anywhere, tight button layout      
    You can setup a specific program to launch when a button is clicked, or use the Combobox to select a .py file found in the root folder, and run that file.  """      

ROOT_PATH = './'      

def Launcher():      

    def print(line):      
        window['output'].update(line)      

    sg.ChangeLookAndFeel('Dark')      

    namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py') ]      

    sg.SetOptions(element_padding=(0,0), button_element_size=(14,2), auto_size_buttons=False)      
    layout =  [[sg.Combo(values=namesonly, size=(35,30), key='demofile'),      
                sg.Button('Run', button_color=('white', '#00168B')),     
                sg.Button('Program 1'),      
                sg.Button('Program 2'),      
                sg.Button('Program 3', button_color=('white', '#35008B')),      
                sg.Button('EXIT', button_color=('white','firebrick3'))],      
                [sg.Text('', text_color='white', size=(20,1), key='output')]]      

    window = sg.Window('Floating Toolbar', layout, no_titlebar=True, keep_on_top=True, location=(200, 0), size=(1200,40))

    # ---===--- Loop taking in user input (events) --- #      
    while True:      
        (event, value) = window.read()      
        if event ==  'EXIT'  or event == sg.WIN_CLOSED:      
            break # exit button clicked      
        if event ==  'Program 1':      
            os.system('test.py')      
        elif event ==  'Program 2':      
            print('Run your program 2 here!')      
        elif event ==  'Run':      
            file = value['demofile']      
            print('Launching %s'%file)   
            global var1
            var1 = file   
            ExecuteCommandSubprocess('python', os.path.join(ROOT_PATH, file))      
        else:      
            print(event)      

def ExecuteCommandSubprocess(command, *args, wait=False): 
    print(var1)    
    os.system(var1)       
    #try:      
    #    if sys.platwindow == 'linux':      
    #        arg_string = ''      
    #        for arg in args:      
    #        sp = subprocess.Popen(['python3'  + arg_string, ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)              
    #    else:      
    #        sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
    #    if wait:      
    #        out, err = sp.communicate()      
    #        if out:      
    #            print(out.decode("utf-8"))      
    #        if err:      
    #            print(err.decode("utf-8"))      
    #except: pass      



if __name__ == '__main__':      
    Launcher()      
