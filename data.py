import os
import numpy as np
import pandas as pd
import processing

class DataUtils:
    def __init__(self):
        self.signalRoot="D:/AI/Projects/VedicFY/BP 3.0/PPG-BP/PPGBPDatabase/Data File/0_subject"
        self.DataRoot="D:/AI/Projects/VedicFY/BP 3.0/PPG-BP/PPGBPDatabase/Data File/PPG-BP dataset csv.csv"
    
    def signalMat(self,filter):
        # print(os.listdir(self.root)[0][:-4])
        files=os.listdir(self.signalRoot)

        processor=processing.Preprocesing()
        self.rawSignalsDict={}
        self.filteredSignalDict={}
        self.fileList=[]
        for i in files:
            data=np.loadtxt(os.path.join(self.signalRoot,i), dtype=float)
            self.fileList.append(i)
            # self.signalsDict[i[:-4]]=data
            self.rawSignalsDict[i]=data
            if(filter==True):
                self.filteredSignalDict[i]=processor.process(data)
           
        
        return self.fileList,self.rawSignalsDict,self.filteredSignalDict

    
    def BPMat(self):
        data=pd.read_csv(self.DataRoot)
        self.SBPDict=dict(zip(data["subject_ID"],data["Systolic Blood Pressure(mmHg)"]))
        self.DBPDict=dict(zip(data["subject_ID"],data["Diastolic Blood Pressure(mmHg)"]))
       
        return self.SBPDict,self.DBPDict

        

    
    def getFilenameWithIndex(self,filename):
        return filename[:-4]
    
    def getIdFromFilename(self,filename):
        return filename[:-6]





