from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *

#isimden duzelen sifetler
"""
s_isim = [sekilci(['lı','li', 'lu', 'lü' ],3,'0',"İsimdən düzələn sifət 1 "), sekilci(['sız','siz', 'suz', 'süz' ],3,'0',"İsimdən düzələn sifət 2"),
           sekilci(['dakı','dəki' ],1,'0',"İsimdən düzələn sifət 3"), sekilci(['cıl','cil', 'cul', 'cül' ],3,'0',"İsimdən düzələn sifət 4"),
           sekilci(['ı','i', 'u', 'ü' ],3,'0',"İsimdən düzələn sifət 5"),sekilci(['i','li'],1,'0',"İsimdən düzələn sifət 6")]

#felden duzelen sifetler

s_fel = [sekilci(['ağan','əgən'],1,'0',"Feldən düzələn sifət 1"),
          sekilci(['ar','ər'],1,'0',"Feldən düzələn sifət 2"),
          sekilci(['qan','qən'],1,'0',"Feldən düzələn sifət 3"),
          sekilci(['ğın','ğin','ğun','ğün'],3,'0',"Feldən düzələn sifət 4"),
          sekilci(['qın','qin','qun','qün'],3,'0',"Feldən düzələn sifət 5"),
          sekilci(['ıq','ik','uq','ük'],3,'0',"Feldən düzələn sifət 6"),
          sekilci(['ıcı','ici','ucu','ücü'],3,'0',"Feldən düzələn sifət 7"),
          sekilci(['aq','ək'],1,'0',"Feldən düzələn sifət 8"),
          sekilci(['ma','mə'],1,'0',"Feldən düzələn sifət 9")]
"""


s_cem=[sekilci(['lar','lər'],1,'0',cem)]
s_hal=[sekilci(['nın','nin','nun','nün'],3,'-',hal2),sekilci(['ya','yə'],1,'-',hal3),sekilci(['nı','ni','nu','nü'],3,'-',hal4),
       sekilci(['da','də'],1,'0',hal5),sekilci(['dan','dən'],1,'0',hal6)]
s_men=[sekilci(['ım','im','um','üm'],3,'-',sex1),sekilci(['ın','in','un','ün'],3,'-',mens2),sekilci(['sı','si','su','sü'],3,'-',mens3),
       sekilci(['ımız','imiz','umuz','ümüz'],3,'-',mens4),sekilci(['ınız','iniz','unuz','ünüz'],3,'0',mens5)]
s_sex=[sekilci(['yam','yəm'],1,'-',sex1),sekilci(['san','sən'],1,'0',sex2),sekilci(['dır','dir','dur','dür'],3,'0',sex3),
       sekilci(['yıq','yik','yuq','yük'],3,'-',sex4),sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',sex5),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]


for pol in s_cem:
    pol.sonra=[s_men,s_hal,s_sex]
for pol in s_men:
    pol.sonra=[s_hal,s_sex]
for pol in s_hal:
    if pol.adi==hal3:
        pol.sonra=[[sekilci(['dır','dir','dur','dür'],3,'0',sex3),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]]
    else:
        pol.sonra=[s_sex]

"""
for pol in s_isim:
    pol.sonra = [i_sex]
for pol in s_fel:
    pol.sonra  = [i_sex]
"""
n_sifet = [s_cem, s_hal,s_men,s_sex] #isimden duzelen
#n_sifet1 = [s_fel, i_sex] #felden duzelen
