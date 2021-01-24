from django.shortcuts import render
from soz_analizi import *
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
# Create your views here.
from django.http import HttpResponse, JsonResponse
from .forms import NameForm, TextForm, SozForm, SignUpForm, UserLoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import gps_data, sayqac_data

from django.utils import timezone

from .forms import UserLoginForm
import json

# def index(request):
#     soz_class = NameForm
#     cumle_class = TextForm
#     morf_class = SozForm
#     if request.method == 'POST':

#         if request.POST['action'] == 'soz':
#             return soz_analiz(request)
#         if request.POST['action'] == 'metn':
#             return stem_metn(request)
#         if request.POST['action'] == 'morf':
#             return morf(request)

#     return render(request, 'index.html', {'form': soz_class, 'cumle': cumle_class, 'morf': morf_class})

# Create your views here.

from django.shortcuts import redirect

def handler404(request):
    return redirect('dilci.az')



def index(request):
    return render(request, 'index.html', {})

# done


def morf(request):

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    try:
        content = body['metn']
    except:
        return JsonResponse({"data": []}, status=400)

    # print(content)

    '''
    soz_class = NameForm
    cumle_class = TextForm
    morf_class = SozForm
    '''
    temp = content  # request.GET.get('soz', '')
    # print(request.GET)
    k = deqiq_olsun(duzelt(temp))
    txt = []
    if len(k) == 0:
        txt.append(temp+' sözü tapılmadı\n')

    txt.append(str(' '+temp+' sözünü '+str(len(k)) +
                   ' cür təhlil etmək mümkündür '))
    for i in range(0, len(k)):
        txt.append(' '+str(i+1)+' ci yol ')
        txt.append(
            ' '+str(k[i].kok)+' -sözün başlanğıc formasıdır. Nitqi hissəsi isə ' + str(k[i].nitq)+'dir.')
        for sh in k[i].shekilciler:
            if sh.stat == '-':
                txt.append(str(sh.adi)+' : '+str(sh.secilmis[-1:]))
            else:
                txt.append(str(sh.adi)+' : '+str(sh.secilmis))

        txt.append('Hecalara isə bu yol ilə ayırmaq olar : ' +
                   k[0].hecaya_bol()+' ')

    return JsonResponse({"data": txt}, status=200)

# done


def stem_metn(request):
    content_txt = ''
    body_unicode = request.body.decode('utf-8')
    print(body_unicode)
    try:
        print('1')
        body = json.loads(body_unicode)
        content_txt = body['metn']
        #content_nitq = body['nitq']
    except:
        print('3')
        return JsonResponse({"data": []}, status=400)
        print('2')

    #soz_class = NameForm
    #cumle_class = TextForm
    #morf_class = SozForm
    #porter = PorterStemmer()
    #lancaster = LancasterStemmer()
    #k = request.POST.get('metn', '')
    #alqo = request.POST.get('alqo', '')
    txt = content_txt
    '''
    if alqo == 'Bizim Alqoritm':
        txt = metn_oxu(k)
    elif alqo == 'Porter Alqoritmi':
        txt = porter.stem(txt)
    elif alqo == 'Lancaster Alqoritmi':
        txt = lancaster.stem(txt)
    elif alqo == 'WordNet Alqoritmi':
        wordnet_lemmatizer = WordNetLemmatizer()
        txt = metn_oxu(wordnet_lemmatizer.stem(k))
    '''
    #wordnet_lemmatizer = WordNetLemmatizer()
    txt = metn_oxu(txt)
    return JsonResponse({"data": txt}, status=200)

    # return render(request, 'metn.html', {'form': soz_class, 'cumle': cumle_class, 'morf': morf_class, 'txt': txt})

# done


def soz_analiz(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    #print(body)
    try:
        content_soz = body['metn']
        content_nitq = body['nitq']
    except:
        return JsonResponse({"data": []}, status=400)

    '''
    soz_class = NameForm
    cumle_class = TextForm
    morf_class = SozForm
    '''

    k = sz(content_soz)  # request.POST.get('soz', ''))
    k.nitq(content_nitq)  # request.POST.get('nitq', ''))
    z = []
    res = {'original_word': k.ozu}
    for a in k.yarat():
        for aa in a.shekilciler:
            if(a.ozu in res.keys()):
                # res[a.ozu].append([aa.secilmis, aa.adi])
                res[a.ozu].append( aa.adi)

            else:
                res[a.ozu] = []
                # res[a.ozu].append([aa.secilmis, aa.adi])
                res[a.ozu].append( aa.adi)

        # z.append(a.ozu)
        # print(a)
        #form = soz_class(data=request.POST)

    data = z

    # , 'form': soz_class, 'morf': morf_class, 'cumle': cumle_class
    return JsonResponse(res, status=200)
    # return render(request, 'yarat.html', {'data': data, 'pho': pho, 'form': soz_class, 'morf': morf_class, 'cumle': cumle_class})

# sil


def about(request):
    return render(request, 'team.html', {})

# sil


def contact(request):
    return render(request, 'contact.html', {})

# sil


def work(request):
    return render(request, 'work.html', {})

# ????


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, "login.html", {"form": form, "title": title})


# done
def morf_view(request):
    #soz_class = NameForm
    #cumle_class = TextForm
    #morf_class = SozForm

    if True:  # request.method == 'GET':
        # if request.POST['action'] == 'morf':
        return morf(request)

    # return render(request, 'morf.html', {'form': soz_class, 'cumle': cumle_class, 'morf': morf_class})

# don


def yarat_view(request):

    return soz_analiz(request)
    '''
    soz_class = NameForm
    cumle_class = TextForm
    morf_class = SozForm
    if request.method == 'POST':

        if request.POST['action'] == 'soz':
            return soz_analiz(request)

    return render(request, 'yarat.html', {'form': soz_class, 'cumle': cumle_class, 'morf': morf_class})
    '''

# don


def metn_view(request):
    # if request.method == 'POST':
    #    return JsonResponse({"data":'ali'}, status = 200)
    return stem_metn(request)

    soz_class = NameForm
    cumle_class = TextForm
    morf_class = SozForm
    if request.method == 'POST':
        if request.POST['action'] == 'metn':
            return stem_metn(request)
    return render(request, 'metn.html', {'form': soz_class, 'cumle': cumle_class, 'morf': morf_class})


def cnv(n):
    if(n in dey_isim):
        return 'Isim'
    if(n in dey_feil):
        return 'Feil'
    if(n in dey_evez):
        return 'Əvəzlik'
    if(n in dey_sif):
        return 'Sifət'
    if(n in dey_say):
        return 'Say'
    if(n in dey_zerf):
        return 'Zərf'
    return n


def l_v(request):
    morf_class = SozForm
    temp = request.POST.get('soz', '')
    koko = lug()
    za = yuxari(temp)
    sozder = koko.de(za[:3])
    cv = []
    for kl in sozder:
        if kl.startswith(za) == True:
            soz = kl.split('\t')[0]
            nitqler = kl.split('\t')[1].split(';')[:-1]
            for ni in nitqler:
                cv.append([soz, cnv(ni)])

    if(len(za) < 3):
        for zaaz in koko.dic.keys():
            if zaaz.startswith(za) == True:
                for kl in koko.de(zaaz):
                    soz = kl.split('\t')[0]
                    # print(kl)
                    nitqler = kl.split('\t')[1].split(';')[:-1]
                    for ni in nitqler:
                        cv.append([soz, cnv(ni)])

    return render(request, 'luget.html', {'morf': morf_class, 'morf_t': cv})


def luget_view(request):
    morf_class = SozForm
    if request.method == 'POST':
        if request.POST['action'] == 'morf':
            return l_v(request)
    return render(request, 'luget.html', {'morf': morf_class})
