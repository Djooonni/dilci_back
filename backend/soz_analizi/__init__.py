from soz_analizi import *
from soz_analizi.soz import *
import nltk

def feildi(soz):
    for a in deqiq_olsun(soz):
        if a.nitq in ['Feil']:
            return True
    return False

def isimdi(soz):
    for a in deqiq_olsun(soz):
        if a.nitq in ['Isim']:
            return True
    return False

def sifetdi(soz):
    for a in deqiq_olsun(soz):
        if a.nitq in ['Sifet']:
            return True
    return False

def saydi(soz):
    for a in deqiq_olsun(soz):
        if a.nitq in ['Say']:
            return True
    return False

def evezlikdi(soz):
    for a in deqiq_olsun(soz):
        if a.nitq in ['Evezlik']:
            return True
    return False

def zerfdi(soz):
    for a in deqiq_olsun(soz):
        if a.nitq in ['Zerf']:
            return True
    return False


def az(a,b):
    if (len(a)>len(b)):
        return True
    else:
        return False

def cox(a,b):
    if (len(a)>len(b)):
        return False
    else:
        return True

def baslangic(soz, mode):
    cvb=''
    funksiya=cox
    yeke=False

    if soz[0]in 'QÜERTYUİOPÖĞASDFGHJKLIƏZXCVBNMÇŞ':
        yeke=True
    soz=duzelt(soz)

    if(mode=='q'):
        funksiya=az
    tcvb=deqiq_olsun(soz)
    if len(tcvb)==0:
        if yeke:
            return yuxari(soz)[0]+soz[1:]

        return yuxari(soz)

    for a in tcvb:
        if(len(cvb)==0):
            cvb=a.kok
            continue
        if(funksiya(cvb,a.kok)):
            cvb=a.kok
    return cvb

def nitqi(soz, mode):
    cvb=''
    fcvb=''
    funksiya=cox
    yeke=False

    if soz[0]in 'QÜERTYUİOPÖĞASDFGHJKLIƏZXCVBNMÇŞ':
        yeke=True
    soz=duzelt(soz)

    if(mode=='q'):
        funksiya=az
    tcvb=deqiq_olsun(soz)
    if len(tcvb)==0:
        return 'yyy'

    for a in tcvb:
        if(len(cvb)==0):
            cvb=a.kok
            fcvb=a.nitq
            continue
        if(funksiya(cvb,a.kok)):
            cvb=a.kok
            fcvb=a.nitq
    return fcvb

def bol(txt):
    words = nltk.word_tokenize(txt)
    return words

def metn_oxu(metn):

    luget=bol(metn)
    cv=''
    for ak in luget:
        if(ak=='\n'):
            continue
        cv+=baslangic(ak,'u')+' '
    return cv
def statistika(metn):
    total=0
    dict={}
    notfound=0
    luget=bol(metn)
    cv=''
    for ak in luget:
        if(ak=='\n'):
            continue

        total+=1
        tmp=nitqi(ak,'u')
        print(tmp+' ' + yuxari(ak))
        if(tmp=='yyy'):
            notfound+=1
            continue

        if(tmp not in dict.keys()):
            dict[tmp]=1
        else:
            dict[tmp]+=1

    perc=1-notfound/total

    return total,dict,perc

def statistika_soz(metn):
    total=0
    dict={}
    notfound=0
    luget=bol(metn)
    cv=''
    for ak in luget:
        if(ak=='\n'):
            continue

        total+=1
        tmp=baslangic(ak,'u')


        if(tmp in [yuxari(ak)]):
            notfound+=1
            continue
        if(tmp not in dict.keys()):
            dict[tmp]=1
        else:
            dict[tmp]+=1

    perc=1-notfound/total

    return total,dict,perc

def txt_oxu(addr):
    file = open(addr,'r',encoding='utf-8')
    sozder= file.readlines()
    luget=[]
    cvb=''
    for k in sozder:
        luget=k.split(' ')
        cv=''
        for ak in luget:

            if(ak=='\n'):
                continue
            ak=duzelt(ak)
			#Gədəbəy kartofun vətənidir.
        #    print(ak)
            cv+=baslangic(ak,'u')+' '
        #print(cv)
        cvb+=cv+'\n'
    return cvb
