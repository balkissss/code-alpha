# %%
import os
import shutil
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox

def organize(dir):
    for filename in os.listdir(dir):
        path = os.path.join(dir,filename)
        if os.path.isfile(path):
            try:
                extension=filename.split(".")[-1].lower()
                folder=os.path.join(dir,extension.upper()+" Files")
                if not os.path.exists(folder):
                    os.makedirs(folder)
                shutil.move(path,os.path.join(folder,filename))
                win.accomplished.setText("Files have been organized by their extensions.")
            except PermissionError:
                print(f"permission denied :'{path}',skipping...")
            except Exception as e :
                print(f"error moving'{path}':{e}")
def addpath():
    return win.lineEdit.text()
def clean(dir):
    for folder in os.listdir(dir):
        folderp= os.path.join(dir,folder)
        if os.path.isdir(folderp):
            seen=[]
            try:
                for file in os.listdir(folderp):
                    filep = os.path.join(folderp,file)
                    if os.path.isfile(filep):
                        if duplicated(filep,seen):
                            os.remove(filep)
                        else:
                            seen.append(filep)
            except PermissionError:
                print(f"permission denied :'{folderp}',skipping...")
            except Exception as e :
                print(f"error cleaning'{folderp}':{e}")
    win.accomplished.setText("Duplicated files removed")    
def duplicated(path,list):
    for file in list:
        if compare(file,path):
            return True
    return False
def compare(file1,file2):
    if os.path.getsize(file1)!= os.path.getsize(file2):
        return False
    with open(file1,'rb') as f1, open( file2,'rb') as f2:
        while True:
            chunk1=f1.read(4096)
            chunk2=f2.read(4096)
            if not chunk1 and not chunk2:
                return True
            if chunk1!=chunk2:
                return False

                  




app = QApplication([])
win = loadUi("organizer.ui")
win.organize.clicked.connect(lambda:organize(addpath()))
win.addpath.clicked.connect(addpath)
win.clean.clicked.connect(lambda:clean(addpath()))
win.show()



app.exec_()



# %%
