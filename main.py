import sys,os
sys.path.insert(0, os.getcwd() + "/src/") #assuming you are running the script from inside the BIOS_PW_SCANNER folder


from Application import Application



app = Application()
app.run()