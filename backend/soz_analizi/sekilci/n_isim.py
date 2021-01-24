from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *

i_cem=[sekilci(['lar','lər'],1,'0',cem)]
i_hal=[sekilci(['nın','nin','nun','nün'],3,'-',hal2),sekilci(['ya','yə'],1,'-',hal3),sekilci(['nı','ni','nu','nü'],3,'-',hal4),
       sekilci(['da','də'],1,'0',hal5),sekilci(['dan','dən'],1,'0',hal6)]
i_men=[sekilci(['ım','im','um','üm'],3,'-',mens1),sekilci(['ın','in','un','ün'],3,'-',mens2),sekilci(['sı','si','su','sü'],3,'-',mens3),
       sekilci(['ımız','imiz','umuz','ümüz'],3,'-',mens4),sekilci(['ınız','iniz','unuz','ünüz'],3,'-',mens5)]
i_sex=[sekilci(['yam','yəm'],1,'-',sex1),sekilci(['san','sən'],1,'0',sex2),sekilci(['dır','dir','dur','dür'],3,'0',sex3),
       sekilci(['yıq','yik','yuq','yük'],3,'-',sex4),sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',sex5),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]
i_la=[sekilci(['la','lə'],1,'0',i_la)]
i_daki=[sekilci(['dakı','dəki'],1,'0',i_daki)]
for pol in i_cem:
    pol.sonra=[i_men,i_hal,i_sex[3:],i_la,i_daki]
for pol in i_men:
    if pol.adi == mens1 or pol.adi == mens4:
        pol.sonra=[i_hal,i_sex[1:3]+i_sex[4:],i_la,i_daki]
        continue
    if pol.adi == mens2 or pol.adi == mens5:
        pol.sonra=[i_hal,i_sex[0:1]+i_sex[2:4]+i_sex[5:],i_la,i_daki]
        continue

    if pol.adi == mens3:
        pol.sonra=[i_hal,i_sex,i_la,i_daki]
        pol.sonra[0][1].forma=['na','nə']#bitişdirici samir dəyişir
    else:
        pol.sonra=[i_hal,i_sex,i_la,i_daki]

for pol in i_hal:
    if pol.adi==hal3 or pol.adi==hal2 or pol.adi==hal4:
        pol.sonra=[[sekilci(['dır','dir','dur','dür'],3,'0',sex3),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',sex6)]]
    else:
        pol.sonra=[i_sex]

n_isim=[i_cem,i_men,i_hal,i_sex,i_la,i_daki]
