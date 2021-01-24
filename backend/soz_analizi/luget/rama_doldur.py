import xlwt
import xlrd
import os

def yuxari(soz):
    for k in range(0,len(soz)):
        if soz[k]=='ı':
            soz=soz[0:k]+'I'+soz[k+1:]
        if soz[k]=='i':
            soz=soz[0:k]+'İ'+soz[k+1:]
        if soz[k]=='ə':
            soz=soz[0:k]+'Ə'+soz[k+1:]
    soz=soz.upper()
    return (soz)

class efsane:
    xemse={}
    def __init__(self):
        self.xemse=self.oxu_tar()

    def oxu_tar(self):
        pazz=os.path.join(os.getcwd(),'luget')
        pazz=os.path.join(pazz,'final.xlsx')
        rbook= xlrd.open_workbook(pazz)
        rsh=rbook.sheet_by_index(0)
        for k in range(1,rsh.nrows):
            soz =rsh.cell_value(k,1)
            nitq=rsh.cell_value(k,10)
            if(len(nitq)==0):
                nitq='namelum;'
            try:
                if(len(soz)==1):
                    if((soz[0],-1,-1) in self.xemse.keys()):                
                        self.xemse[soz[0],-1,-1].append(soz+'\t'+nitq)
                    else:
                        self.xemse[soz[0],-1,-1]=[]
                elif(len(soz)==2):
                    if((soz[0],soz[1],-1) in self.xemse.keys()):                
                        self.xemse[soz[0],soz[1],-1].append(soz+'\t'+nitq)
                    else:
                        self.xemse[soz[0],soz[1],-1]=[]
                elif(len(soz)>2):
                    if((soz[0],soz[1],soz[2]) in self.xemse.keys()):                
                        self.xemse[soz[0],soz[1],soz[2]].append(soz+'\t'+nitq)
                    else:
                        self.xemse[soz[0],soz[1],soz[2]]=[]
            except:
                print(soz)
                print('-----')
    

        print("50%")

        pazz=os.path.join(os.getcwd(),'luget')
        pazz=os.path.join(pazz,'diff_final.xlsx')
        rbook= xlrd.open_workbook(pazz)
        rsh=rbook.sheet_by_index(0)
        for k in range(1,rsh.nrows):
            
            soz =rsh.cell_value(k,0)
            nitq=rsh.cell_value(k,1)
            soz=yuxari(soz)

            if(len(nitq)==0):
                nitq='namelum;'
            
            if(len(soz)==1):
                if((soz[0],-1,-1) in self.xemse.keys()):                
                    self.xemse[soz[0],-1,-1].append(soz+'\t'+nitq)
                else:
                    self.xemse[soz[0],-1,-1]=[]
            elif(len(soz)==2):
                if((soz[0],soz[1],-1) in self.xemse.keys()):                
                    self.xemse[soz[0],soz[1],-1].append(soz+'\t'+nitq)
                else:
                    self.xemse[soz[0],soz[1],-1]=[]
            elif(len(soz)>2):
                if((soz[0],soz[1],soz[2]) in self.xemse.keys()):                
                    self.xemse[soz[0],soz[1],soz[2]].append(soz+'\t'+nitq)
                else:
                    self.xemse[soz[0],soz[1],soz[2]]=[]
        
        print("loading done")
        return self.xemse

    def de_yaver(self,soz):
        cvb=[]
        soz=yuxari(soz)
        if(len(self.xemse)==0):
            oxu_tar()
        if(len(soz)==1):
            if((soz[0],-1,-1) in self.xemse.keys()):
                for k in self.xemse[soz[0],-1,-1]:
                    cvb.append(k)
        elif(len(soz)==2):
            if((soz[0],soz[1],-1) in self.xemse.keys()):
                for k in self.xemse[soz[0],soz[1],-1]:
                    cvb.append(k)
        elif(len(soz)>2):
            if((soz[0],soz[1],soz[2]) in self.xemse.keys()):
                for k in self.xemse[soz[0],soz[1],soz[2]]:
                    cvb.append(k)
        return cvb

