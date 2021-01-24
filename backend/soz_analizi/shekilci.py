sait=['a', 'ı', 'o', 'u','e', 'ə' , 'i', 'ö', 'ü']
istisna=['tale', 'mənbə', 'mövqe', 'mənşə', 'nə', 'mənafe']
istisna1=['isim', 'qisim', 'nəsil', 'fikir', 'ətir', 'səbir', 'qəbir','heyif','sətir','qədir','ömür', 'sinif',
 'eyib', 'şəkil', 'meyil', 'əsil', 'fəsil', 'xeyir', 'zehin']
istisna2=['beyin','ağıl','alın','burun','ağız','boyun','qoyun','çiyin','oğul','qarın','əyin','qayın']   #qoyun is omonim both versions should work but do not know how

class sekilci:
    req=0
    def __init__(self,fm,qa,st,ad):
        self.sonra=[]
        self.forma=fm
        self.qn=qa
        self.stat=st
        self.adi=ad
    def d_et(self,n):
        self.req=n

    def check(self, soz, shekilci):
        #Nicat burani qurdala
        
        if(soz.ozu[-1]=='t' and shekilci[0] in sait and soz.nitq=='Feil'):
            soz=soz.ozu[:-1]+'d'
        else:
            soz=soz.ozu
        #burdan asagi hecne eleme
        m=0
        self.secilmis=shekilci
        if soz in ('biz', 'mən') and shekilci=='in' and False:#wpage==2
            self.secilmis='im'
            return soz +'im'

        if soz in ('o') :#and wpage==2:
            return soz+shekilci

        for i in range (0, len(soz)):
            if soz[i] in sait:
                m+=1

        if soz[len(soz)-1]==soz[len(soz)-2] and shekilci[0] not in sait:
            return soz[:-1]+shekilci

        if soz in istisna1 and shekilci[0] in sait and shekilci not in ('əm', 'ik'):
            return soz[:-2]+soz[len(soz)-1]+shekilci

        if soz in istisna2 and shekilci[0] in sait and shekilci not in ('əm', 'ik', 'in', 'ə'):
            return soz[:-2]+soz[len(soz)-1]+shekilci

        if soz in istisna:
            if shekilci in ('m', 'n', 'miz', 'niz'):
                self.secilmis='yi'+shekilci
                return soz[:]+'yi'+shekilci
            if shekilci in ('si'):
                self.secilmis='yi'
                return soz[:]+'yi'
            return soz[:]+shekilci

        if soz in ('su'):
            if shekilci in ('m', 'n', 'muz', 'nuz'):
                self.secilmis='yu'+shekilci
                return soz[:]+'yu'+shekilci
            if shekilci in ('su'):
                self.secilmis='yu'
                return soz[:]+'yu'
            return soz[:]+shekilci

        if shekilci[0] not in sait:
            return soz+shekilci

        if m>1:
            if soz[len(soz)-1]=='q':
                return soz[:-1]+'ğ'+shekilci
            if soz[len(soz)-1]=='k':
                return soz[:-1]+'y'+shekilci
            return soz+shekilci

        if m==1:
            return soz+shekilci
        self.secilmis=shekilci
        return soz+shekilci

    def shert(self,soz,req):
            if self.stat=='-' and not((soz.ozu[(len(soz.ozu)-1)]in sait) ^ (self.forma[req][0] in sait)):
                self.secilmis=self.forma[req][1:]
                return self.check(soz,self.forma[req][1:])
            if self.stat=='+' and ((soz.ozu[(len(soz.ozu)-1)] in sait) ^ (self.forma[req][0] in sait)):
                self.secilmis=self.forma[req][2:]
                return self.check(soz, self.forma[req][2:])
            self.secilmis=self.forma[req]
            return self.check(soz,self.forma[req])


    def de(self,soz):
        it=(len(soz.ozu)-1)
        if self.qn==1:
            while it>-1:
                if soz.ozu[it] in ('a', 'ı', 'o', 'u'):
                    return self.shert(soz,0)
                if soz.ozu[it] in ('e', 'ə' , 'i', 'ö', 'ü'):
                    return self.shert(soz,1)
                it-=1

        if self.qn==3:
            while it>-1:
                if soz.ozu[it] in ('a', 'ı'):
                    return self.shert(soz,0)
                if soz.ozu[it] in ('e', 'ə' , 'i'):
                    return self.shert(soz,1)
                if soz.ozu[it] in ('o', 'u'):
                    return self.shert(soz,2)
                if soz.ozu[it] in ('ö', 'ü'):
                    return self.shert(soz,3)
                it-=1
        self.secilmis=self.forma[0]
        return soz.ozu+self.forma[0]
