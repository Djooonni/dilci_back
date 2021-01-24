from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *


istisnalar = ['bildirmək', 'döyündü', 'yuyundu', 'daranmaq']
f_zaman = [sekilci(['yır','yir','yur','yür'],3,'-',in_zaman),
	sekilci(['dı','di','du','dü'],3,'0',s_k_zaman),
	sekilci(['mış','miş','muş','müş'],3,'0',n_k_zaman1),
	sekilci(['yıb','yib','yub','yüb'],3,'-',n_k_zaman),
	sekilci(['yacaq','yəcək'],1,'-',q_q_zaman),
	sekilci(['yar','yər'],1,'-',qq_q_zaman)]

f_qeyriqeticase = [sekilci(['z','z'],1,'0',qq_q_zaman)]

f_inkar = [sekilci(['ma','mə'],1,'0',inkar)] #indiki ve qeyri qeti gelecek zamanda sait dushur

f_tli_tsiz = [sekilci(['dır','dir','dur','dür'],3,'0',t_eden),
	sekilci(['yış','yiş','yuş','yüş'],3,'-',t_eden1),
	sekilci(['yın','yin','yun','yün'],3,'-',t_eden2),
	sekilci(['yıl','yil','yul','yül'],3,'-',t_eden3)
]

f_mena = [sekilci(['yıl','yil','yul','yül'],3,'-',qaydis),
	sekilci(['yın','yin','yun','yün'],3,'-',qaydis1),
	#sekilci(['n'],0,'0',"qayidish3"),
	sekilci(['yıl','yil','yul','yül'],3,'-',mechul),
	sekilci(['yın','yin','yun','yün'],3,'-',mechul1),
	#sekilci(['n'],0,'0',"mechul3"),
	sekilci(['yış','yiş','yuş','yüş'],3,'-',qar_birge),
	sekilci(['dır','dir','dur','dür'],3,'0',icbar)]
	#sekilci(['t'],3,'0',"icbar2")]

f_dimish = [sekilci(['dı','di','du','dü'],3,'0',idi_h),
            sekilci(['mış','miş','muş','müş'],3, '0', imis_h)]
f_idi = [sekilci(['dı','di','du','dü'],3,'0',idi_h)]
f_imish = [sekilci(['mış','miş','muş','müş'],3, '0', imis_h)]

f_sual = [sekilci(['mı','mi'],1,'0',sual_h)]
f_ise = [sekilci(['sa','sə'],1,'0',ise_h)]

f_sex=[sekilci(['yam','yəm'],1,'-',sex1),
       sekilci(['san','sən'],1,'0',sex2),
       sekilci(['dı','di','du','dü'],3,'0',sex3),
       sekilci(['yıq','yik','yuq','yük'],3,'-',sex4),
       sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',sex5),
       sekilci(['lar','lər'],1,'0',sex6)]

f_sexcase =[sekilci(['m','m'],1,'0',sex1),
           sekilci(['n','n'],1,'0',sex2),
           sekilci(['dı','di','du','dü'],3,'0',sex3),
           sekilci(['q','k','q','k'],3,'0',sex4),
           sekilci(['ınız','iniz','unuz','ünüz'],3,'-',sex5),
           sekilci(['lar','lər'],1,'0',sex6)]


f_emr = [sekilci(['yım','yim','yum','yüm'],3,'-',e_s_1t),
         sekilci(['sın','sin','sun','sün'],3,'0',e_s_3t),
         sekilci(['yaq','yək'],1,'-',e_s_1c),
         sekilci(['yın','yin'],1,'-',e_s_2c),
         sekilci(['sınlar','sinlər','sunlar','sünlər'],3,'0',e_s_3c)]

f_arzu =[sekilci(['ya','yə'],1,'-',a_s)]
f_vacib = [sekilci(['malı','məli'],1,'0',v_s)]
f_lazim = [sekilci(['yası','yəsi'],1,'-',l_s)]
f_sert = [sekilci(['sa','sə'],1,'0',s_s)]
f_davam = [sekilci(['maqda','məkdə'],1,'0',d_s)]

for fel in f_tli_tsiz:
    fel.sonra = [f_zaman, f_dimish, f_sex,f_sual]

for fel in f_inkar:
    '''
    if fel.adi == 'inkar' and fel.adi == 'qeyri-qeti gelecek zaman':
        fel.sonra = [f_qeyriqeticase,f_sual]
        continue
    if fel.adi == 'inkar' and fel.adi == "shuhudi kecmish zaman":
        fel.sonra = [f_zaman, f_sexcase]
    '''
    fel.sonra = [f_ise,f_emr, f_arzu, f_vacib, f_lazim, f_sert, f_davam,f_zaman, f_dimish, f_sual,f_qeyriqeticase]

for fel in f_tli_tsiz:
    fel.sonra = [f_zaman, f_sex, f_sual]
for fel in f_zaman:
    if fel.adi == s_k_zaman or fel.adi == idi_h:
        fel.sonra = [f_sexcase, f_sual]
        continue
    if fel.adi == n_k_zaman or fel.adi == idi_h:
        fel.sonra = [f_sex, f_sual]
        continue
    if fel.adi == s_k_zaman and fel.adi == sex1:
        fel.sonra = [f_sexcase, f_sual]

    fel.sonra = [f_dimish, f_sex,f_sual]

for fel in f_mena:
    if fel.adi == qaydis1 and fel.adi == sex1:
        fel.sonra = [f_zaman, f_sexcase, f_sual]
        continue
    if fel.adi == icbar: # and fel.adi == '1Tek':
        fel.sonra = [f_zaman, f_sexcase, f_sual]

    fel.sonra = [f_zaman, f_sex, f_sual]
for fel in f_dimish:
    fel.sonra = [f_sex,f_sual]



n_feil=[f_inkar, f_mena,f_zaman, f_ise,f_emr, f_arzu, f_vacib, f_lazim, f_sert, f_davam]
