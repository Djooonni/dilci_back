from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *

zerf_cem=[sekilci(['lar','lər'],1,'0',cem)]
zerf_hal=[sekilci(['nın','nin','nun','nün'],3,'-',hal2),sekilci(['ya','yə'],1,'-',hal3),sekilci(['nı','ni','nu','nü'],3,'-',hal4),
       sekilci(['da','də'],1,'0',hal5),sekilci(['dan','dən'],1,'0',hal6)]
zerf_men=[sekilci(['ım','im','um','üm'],3,'-',mens1),sekilci(['ın','in','un','ün'],3,'-',mens2),sekilci(['sı','si','su','sü'],3,'-',mens3),
       sekilci(['ımız','imiz','umuz','ümüz'],3,'-',mens4),sekilci(['ınız','iniz','unuz','ünüz'],3,'0',mens5)]
zerf_sex=[sekilci(['yam','yəm'],1,'-',sex1),sekilci(['san','sən'],1,'0',sex2),sekilci(['dır','dir','dur','dür'],3,'0',sex3),
       sekilci(['yıq','yik','yuq','yük'],3,'-',sex4),sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',sex5),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]

for pol in zerf_cem:
    pol.sonra=[zerf_men,zerf_hal,zerf_sex]
for pol in zerf_men:
    pol.sonra=[zerf_hal,zerf_sex]
for pol in zerf_hal:
    if pol.adi==hal3:
        pol.sonra=[[sekilci(['dır','dir','dur','dür'],3,'0',sex3),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]]
    else:
        pol.sonra=[zerf_sex]

"""
for pol in s_isim:
    pol.sonra = [i_sex]
for pol in s_fel:
    pol.sonra  = [i_sex]
"""

n_zerf = [zerf_cem, zerf_hal,zerf_men,zerf_sex] #isimden duzelen
