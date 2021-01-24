
from soz_analizi.shekilci import *
from soz_analizi.shekilciler import *
from operator import itemgetter
#from soz_analizi.luget.rama_doldur import efsane
dey_isim=['is.']
dey_feil=['f.']
dey_evez=['ev.']
dey_sif=['sif.']
dey_say=['say.']
dey_zerf = ['z.','zer.']
hallanan=['Isim']
mensub=['Isim']

import os
cala={'isim':'Isim','feil':'Feil','sifet':'Sifet','say':'Say','evezlik':'Evezlik','zerf':'Zerf',
        'Isim':'Isim','Feil':'Feil','Sifet':'Sifet','Say':'Say','Evezlik':'Evezlik','Zerf':'Zerf'}


class sz:

    def __init__(self,kopya):
        if kopya.__class__.__name__=='sz':
            self.kok=kopya.kok
            self.ozu=kopya.ozu
            self.hecalar=kopya.hecalar
            self.saitler=kopya.saitler
            self.nitq=kopya.nitq
            self.shekilciler=kopya.shekilciler+[]
            self.sonra=[]

        else:
            if kopya[-3:] in ('maq', 'mək'):
                self.kok=kopya[:-3]
            else:
                self.kok=kopya
            self.ozu=self.kok
            self.shekilciler=[]
            self.hecalar=[]
            self.saitler=[]
            self=sz.istisnalar(self)

    def nitq(self,n):
        self.nitq=cala[n]
        self=self.istisnalar()

    def yaz(self,shekilci):
        if len(self.shekilciler)>0:
            if self.shekilciler[len(self.shekilciler)-1] in sait and shekilci[-1:] in sait:#burda sehf var diesen
                self.shekilciler[len(self.shekilciler)-1]=self.shekilciler[len(self.shekilciler)-1][:-1]
                self.shekilciler[len(self.shekilciler)-1].secilmis=self.shekilciler[len(self.shekilciler)-1].secilmis[:-1]
        self.ozu=shekilci.de(self)
        self.shekilciler.append(shekilci)
        return self


    def hecaya_bol(self):
        self.hecalar=[]
        self.saitler=[]
        if(self.ozu==''):
            self.hecalar=[]
            return
        heca=''
        for i in range(0,len(self.ozu)):
            if self.ozu[i] in sait:
                self.saitler.append(i)

        self.hecalar.append(self.ozu[:self.saitler[0]+1])
        for i in range(1,len(self.saitler)):
            self.hecalar.append(self.ozu[self.saitler[i-1]+1:self.saitler[i]+1] )
            if self.saitler[i]-self.saitler[i-1]>2:
                self.hecalar[i-1]+=self.ozu[self.saitler[i-1]+1]
                self.hecalar[i]=self.hecalar[i][1:]
        self.hecalar[len(self.hecalar)-1]+=self.ozu[self.saitler[len(self.saitler)-1]+1:]
        cvc=''
        for he in self.hecalar:
            cvc+=he+'-'
        return cvc[:-1]

    def istisnalar(self):
        if self.kok=='camaat' or self.kok=='əhali':
            self.sonra=[i_men,i_hal,i_sex]
            return self

        if(self.nitq=='Isim'):
            self.sonra=n_isim
            return self
        if(self.nitq=='Feil'):
            self.sonra=n_feil
            return self
        if(self.nitq=='Sifet'):
            self.sonra=n_sifet
            return self
        if(self.nitq=='Say'):
            self.sonra=n_say
            return self
        if(self.nitq=='Evezlik'):
            self.sonra=n_evezlik
            return self
        if(self.nitq=='Zerf'):
            self.sonra=n_zerf
            return self

        return self

    def yarat(self):
        cvb=[]
        #fazilando
        #ilk shekilcini elave edir
        for qrup in self.sonra:
            for she in qrup:
                y_soz=sz(self)
                cvb.append(y_soz.yaz(she))
        for sooz in cvb:
            #qru son wekilciye elave olunacag shekilci keteqoryasidi
            #meselem eger sonuncu sekilci mensubietdisa onda qru hal,sexs olur
            for qru in sooz.shekilciler[-1].sonra:
                #she qru qrupunda olan shekilcilerdi
                #cem ucun lar/ler
                #filtirleri bura qoyirsan,
                #y_soz.nitq,she.adi, ve y_soz.shekilcilerden istifade edeceksen cox gumanki
                for she in qru:
                    y_soz=sz(sooz)
                    #filtr buraligdi if(flanshey): continue
                    #qinama inet yoxdu bilmirem bawmi neynen qatim comment yaziram
                    cvb.append(y_soz.yaz(she))
        return cvb

    def adliq(self):
        if self.nitq not in hallanan:
            return False
        for s in self.shekilciler:
            if s.adi in (hal2,hal3,hal4,hal5,hal6):
                return False
        return True

    def yiyelik(self):
        if self.nitq not in hallanan:
            return False
        for s in self.shekilciler:
            if s.adi in (hal3,hal4,hal5,hal6):
                return False
        return True

    def yonluk(self):
        if self.nitq not in hallanan:
            return False
        for s in self.shekilciler:
            if s.adi in (hal3):
                return True
        return False

    def tesirlik(self):
        if self.nitq not in hallanan:
            return False
        for s in self.shekilciler:
            if s.adi in (hal4):
                return True
        return False

    def yerlik(self):
        if self.nitq not in hallanan:
            return False
        for s in self.shekilciler:
            if s.adi in (hal5):
                return True
        return False

    def cixisliq(self):
        if self.nitq not in hallanan:
            return False
        for s in self.shekilciler:
            if s.adi in (hal6):
                return True
        return False

    def mesubiyyeti(self,req):
        if self.nitq not in mensub:
            return False
        if req==0:
            for s in self.shekilciler:
                if s.adi in (mens1,mens2,mens3,mens4,mens5):
                    return True
        if req==1:
            for s in self.shekilciler:
                if s.adi in (mens1):
                    return True
        if req==2:
            for s in self.shekilciler:
                if s.adi in (mens2):
                    return True
        if req==3:
            for s in self.shekilciler:
                if s.adi in (mens3):
                    return True
        if req==4:
            for s in self.shekilciler:
                if s.adi in (mens4):
                    return True
        if req==5:
            for s in self.shekilciler:
                if s.adi in (mens5):
                    return True

        return False

#########################################################
class lug:
    dic={}
    def add(self,ad):
        if len(lug.dic.keys())<5:
            # pazz=os.path.join(os.getcwd(),'home')
            # pazz=os.path.join(pazz,'c')
            # pazz=os.path.join(pazz,'cu79127')
            
            # pazz=os.path.join(pazz,'Dilciaz')
            # pazz=os.path.join(pazz,'public_html')
            # pazz=os.path.join(pazz,'Dilci')            
            # pazz=os.path.join(pazz,'backend')

            pazz=os.path.join(os.getcwd(),'soz_analizi')

            # pazz=os.path.join(pazz,'soz_analizi')

            pazz=os.path.join(pazz,'luget')
            pazz=os.path.join(pazz,'luget.txt')
            file = open(pazz,'r',encoding='utf-8')
            sozder=file.readlines()
            for k in sozder:
                zaz=k.split('\t')[0]
                if zaz[:3] in lug.dic.keys():
                    lug.dic[zaz[:3]].append(k)
                else:
                    lug.dic[zaz[:3]]=[k]


            return self.de(ad)


        if ad in lug.dic.keys():
            return lug.dic[ad]
        else:
            lug.dic[ad]=[]
            return []



    def de(self,ad):
        if ad in lug.dic.keys():
            #print(len(lug.dic.keys()))
            return lug.dic[ad]
        return self.add(ad)
#########################################################
def soz_kokudu(kok,soz):
    if(kok==soz):

        return True

    if(kok[-3:]=="MƏK" or kok[-3:]=="MAQ"):
        kok=kok[:-3]

    if(len(kok)>len(soz)):
        return False

    if(len(kok)==len(soz)and kok!=soz):
        return False

    i=0
    err=0
    for her in kok:
        if(i>=len(kok)):
            break
        if (her!=soz[i]):
            if (her=='i'):
                i+=1
            else:
                err+=1
        if (err==2):
            return False
        i+=1
    return True

def firran(xam,soz,cvb):
    mumkundu=[]
    if(xam.ozu==soz.ozu):
        sj=''
        for sheki in xam.shekilciler:
            sj+=sheki.adi+","
        #print("-soz tapildi shekilciler: "+sj)
        cvb.append(xam)
        return cvb

    if(xam.nitq=='Isim'):
        soz=sz(soz)
        secilmisNitq=n_isim
    elif(xam.nitq=='Feil'):
        soz=sz(soz)
        secilmisNitq=n_feil
    elif(xam.nitq=='Sifet'):
        soz=sz(soz)
        secilmisNitq=n_sifet
    elif(xam.nitq=='Say'):
        soz=sz(soz)
        secilmisNitq=n_say
    elif(xam.nitq=='Evezlik'):
        soz=sz(soz)
        secilmisNitq=n_evezlik
    elif(xam.nitq=='Zerf'):
        soz=sz(soz)
        secilmisNitq=n_zerf

    else:
        secilmisNitq=[]
        print("alinmadi")
        return

    if(len(xam.shekilciler)==0):
        for qrup in secilmisNitq:
            for she in qrup:
                y_soz=sz(xam)
                y_soz.yaz(she)
                if(soz_kokudu(y_soz.ozu,soz.ozu)):
                    #print('alinir diesen : '+y_soz.ozu+"->"+soz.ozu)
                    cvb=[]+firran(y_soz,soz,cvb)

    else:
        for qru in xam.shekilciler[-1].sonra:
            for she in qru:
                y_soz=sz(xam)
                y_soz.yaz(she)
                if(soz_kokudu(y_soz.ozu,soz.ozu)):
                    #print('alinir diesen : '+y_soz.ozu+"->"+soz.ozu)
                    cvb=[]+firran(y_soz,soz,cvb)
    return cvb

def asaqi(soz):
    for k in range(0,len(soz)):
        if soz[k]=='I':
            soz=soz[0:k]+'ı'+soz[k+1:]
        if soz[k]=='İ':
            soz=soz[0:k]+'i'+soz[k+1:]
        if soz[k]=='Ə':
            soz=soz[0:k]+'ə'+soz[k+1:]
    soz=soz.lower()
    return (soz)

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

def duzelt(soz):
    cvb=''
    soz=asaqi(soz)
    for i in range(0,len(soz)):
        if soz[i] in ('0','1','2','3','4','5','6','7','8','9','q','ü','e','r','t','y','u','i','o','p','ö','ğ','a','s','d','f','g','h','j','k','l','ı','ə','z','x','c','v','b','n','m','ç','ş'):
            cvb=cvb+soz[i]

    return cvb

lll=''
def cehd_ele(ad,soz):
    suret=0
    '''
    '''
    cvb=[]
    #try:
    if(suret==0):
        koko=lug()
        sozder=koko.de(ad)

        for s in sozder:
            k=s.split('\t')
            if(soz_kokudu(k[0],soz) and len(k[1])>1):
                if(k[1][:-2] in dey_feil):
                    if(k[0][-2:] not in ['MA','MƏ']):
                        cvb.append([k[0],k[1][:-1].split(';')[:-1]])#cvb.append([k[0],k[1][:-1].split(';')]) kohne versiya
                else:
                        cvb.append([k[0],k[1][:-1].split(';')[:-1]])
    else:
        global lll
        if(lll==''):
            lll=efsane()
        sozder=lll.de_yaver(ad)
        for s in sozder:
            k=s.split('\t')
            #print(k)
            if(soz_kokudu(k[0],soz)):
                cvb.append([k[0],k[1][:-1].split(';')])

    return cvb

    #except:
    #    return []

def sirala(sira):
    for i in range(0,len(sira)):
        for j in range(0,len(sira)-i-1):
            if(len(sira[j][0])<len(sira[j+1][0])):
                temp=sira[j]
                sira[j]=sira[j+1]
                sira[j+1]=temp

    return sira

def nitqi_tap(soz):
    soz=yuxari(soz)
    cvb=[]
    for h in soz:
        if(h in ('0','1','2','3','4','5','6','7','8','9')):
            return []
    if(len(soz)>1):
        a=cehd_ele(soz[:2],soz)
        cvb+=a

        if(len(soz)>2):
            a=cehd_ele(soz[:3],soz)
            cvb+=a

            if(soz[2]!='M'):
                a=cehd_ele(soz[:2]+'M',soz)
                cvb+=a

    a=cehd_ele(soz[:1],soz)
    cvb+=a

    cvb=sirala(cvb)
    return cvb[:]


def deqiq_olsun(soz):
    for h in soz:
        if(h in ('0','1','2','3','4','5','6','7','8','9')):
            return []
    cvb=[]
    mumkun=nitqi_tap(soz)
    for cut in mumkun:
        #print(cut)
        s=''
        for n in cut[1]:
            s=sz(asaqi(cut[0]))
            if(n in dey_isim):
                s.nitq('Isim')
                kk=sz(soz)
                kk.nitq('Isim')
                cvb=firran(s,kk,cvb)


            elif(n in dey_feil):
                s.nitq('Feil')
                kk=sz(soz)
                kk.nitq('Feil')
                cvb=firran(s,kk,cvb)
            elif(n in dey_sif):
                s.nitq('Sifet')
                kk=sz(soz)
                kk.nitq('Sifet')
                cvb=firran(s,kk,cvb)
            elif(n in dey_say):
                s.nitq('Say')
                kk=sz(soz)
                kk.nitq('Say')
                cvb=firran(s,kk,cvb)

            elif(n in dey_evez):
                    s.nitq('Evezlik')
                    kk=sz(soz)
                    kk.nitq('Evezlik')
                    cvb=firran(s,kk,cvb)
            elif(n in dey_zerf):
                    s.nitq('Zerf')
                    kk=sz(soz)
                    kk.nitq('Zerf')
                    cvb=firran(s,kk,cvb)
                #print(296)
                #for ca in cvb:
                #    print(ca.kok)
                #    print(ca.nitq)

            else:
                #bu hisse muveqqetidir yeni nitq hisseleri elave olana kimi
                s.nitq('Isim')
                kk=sz(soz)
                kk.nitq('Isim')
                cvb=firran(s,kk,cvb)

                #bura kimi sil ve continue leri yigisdir


    return cvb
