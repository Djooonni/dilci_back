from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *




ev_cem=[sekilci(['lar','lər'],1,'0',cem)]
ev_hal=[sekilci(['nın','nin','nun','nün'],3,'-',hal2),sekilci(['ya','yə'],1,'-',hal3),sekilci(['nı','ni','nu','nü'],3,'-',hal4),
       sekilci(['da','də'],1,'0',hal5),sekilci(['dan','dən'],1,'0',hal6)]
ev_men=[sekilci(['ım','im','um','üm'],3,'-',mens1),sekilci(['ın','in','un','ün'],3,'-',mens2),sekilci(['sı','si','su','sü'],3,'-',mens3),
       sekilci(['ımız','imiz','umuz','ümüz'],3,'-',mens4),sekilci(['ınız','iniz','unuz','ünüz'],3,'0',mens5)]
ev_sex=[sekilci(['yam','yəm'],1,'-',sex1),sekilci(['san','sən'],1,'0',sex2),sekilci(['dır','dir','dur','dür'],3,'0',sex3),
       sekilci(['yıq','yik','yuq','yük'],3,'-',sex4),sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',sex5),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]


for pol in ev_cem:
    pol.sonra=[ev_men,ev_hal,ev_sex]
for pol in ev_men:
    pol.sonra=[ev_hal,ev_sex]
for pol in ev_hal:
    if pol.adi==hal3:
        pol.sonra=[[sekilci(['dır','dir','dur','dür'],3,'0',sex3),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]]
    else:
        pol.sonra=[ev_sex]

"""
for pol in s_isim:
    pol.sonra = [i_sex]
for pol in s_fel:
    pol.sonra  = [i_sex]
"""
n_evezlik = [ev_cem, ev_hal,ev_men,ev_sex] #isimden duzelen
