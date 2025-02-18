
#This project was made with the contributions of Melisa Akkaş, Ceren Oksal and Muaz Alemdar, all of whom are Linguistics graduates from Boğaziçi University.

#STEMMER
pip install TurkishStemmer

from TurkishStemmer import TurkishStemmer
stemmer = TurkishStemmer()

import pandas as pd

#NORMALIZER
def txt_norm(string): 
  string = string.lower()
  pun_string = ""
  num_string = ""
  for i in string:
    punctuations = "!()[]{};’'\":\,<>./?@#$%^&*_~"
    if i not in punctuations:
      pun_string = pun_string + i
  for j in pun_string:
    numbers  = '''1234567890'''
    if j not in numbers:
      num_string = num_string + j
  num_string = num_string.split()


  num_string = list(pd.unique(pd.Series(num_string)))
  
  stemmed_string = []
  for i in num_string:
    i = stemmer.stem(i)
    stemmed_string.append(i)

  return stemmed_string

non_tr_exceptions = """Sarp elma anne dahi elma hangi hani inanmak kardeş şişman akşamki duvardaki karşıki onunki yarınki yoldaki açıkgöz bilgisayar çekyat hanımeli""".split()

import re
def arabic_regex(text):
  katibat_reg = [re.findall("^\w?a\wi?\wat$", word) for word in text]
  katib_e_t_reg = [re.findall("^\w?a\w[ıi]\w?e?t?$", word) for word in text]
  ketbi_reg =  [re.findall("^[\w]+i$", word) for word in text]
  kuttab_reg = [re.findall("^[\w][uü][\w]{2}a[\w]?$", word) for word in text] 
  kutteb_reg = [re.findall("^[\w][uü][\w]{2}e[\w]$", word) for word in text]
  ketebe_reg = [re.findall("^[\w]?[ae][\w]e[\w][ae]$", word) for word in text]
  kevatib_reg = [re.findall("^[\w]ava[\w]?i[\w]$", word) for word in text]
  mektub_e_reg = [re.findall("^m[ae]\w\w?[uü]\w?[ea]?$", word) for word in text]
  mektubat_reg = [re.findall("^m[ae]\w\w?[uü]\wat$", word) for word in text]
  mekatib_reg = [re.findall("^me[\w]a[\w][iı][\w]$", word) for word in text]
  kettab_reg = [re.findall("^\w[ae]\w{2}a\w$", word) for word in text]
  mekteb_e_t_reg = [re.findall("^m[ae][\w][\w]?[aei][\w][ae]?t?$", word) for word in text]
  ketbiyat_reg = [re.findall("^[\w]+yat$", word) for word in text]
  iktab_reg = [re.findall("^i[\w]?[\w]a[\w]?", word) for word in text]
  tektib_reg = [re.findall("^t[ae][\w][\w]?[ıi][\w]?$", word) for word in text]
  mukatebe_reg = [re.findall("^m[uü][\w]a[\w][ae][\w]?[ae]?", word) for word in text]
  inkitab_reg = [re.findall("^in[\w][ıi][\w]?a[\w]?", word) for word in text]
  iktitab_reg = [re.findall("^i\w?t[iı]\wa\w?$", word) for word in text]
  ihmilal_reg = [re.findall("^i[\w][\w]i[\w]a[\w]$", word) for word in text]
  tekettüb_reg = [re.findall("^t[ea]\w[ea]\w{2}[uü]\w$", word) for word in text]
  tekatüb_reg = [re.findall("^te[\w]a[\w][uü][\w]?", word) for word in text]
  istikbab_reg = [re.findall("^isti[\w][\w]?a[\w]?", word) for word in text]
  kitab_e_reg = [re.findall("^\wi\wa\w[ae]$", word) for word in text]
  tecelli_reg = [re.findall("^t[ea]\w[ae]\w{2}i$", word) for word in text]
  evvelen_reg = [re.findall("^\w+[ea]n$", word) for word in text]
  ekrem_reg = [re.findall("^e\w\w[ea]\w$", word) for word in text]
  edna_reg = [re.findall("^[ea]\w\w?a$", word) for word in text]   
  mensubin_reg = [re.findall("^\w+in$", word) for word in text]
  cihet_reg = [re.findall("^\wi\w[ae]t$", word) for word in text]
  millet_reg = [re.findall("^\w[ıi]\w{2}[ae]t$", word) for word in text]
  fikret_reg = [re.findall("^\w[ıi]\w\w[ae]t$", word) for word in text]
  sükna_reg = [re.findall("^\w[uü]\w\wa$", word) for word in text]   
  mündemic_reg = [re.findall("^m[uü]\w\w[ea]\w[ıi]\w", word) for word in text]  
  esrar_reg = [re.findall("^[ae][^aeıioöuü]\wa\w$", word) for word in text]
  mukaddime_reg = [re.findall("^m[uü]\w[ae]\w{2}[iı]\w?[ae]?",word) for word in text]
  gayri_reg = [re.findall("^gayr.+$", word) for word in text]
  mütefekkir_reg = [re.findall(r"^m[uü]t[ae]f[ae](\w)\1[iı]\w$", word) for word in text]
  mukaddes_e_reg = [re.findall(r"^m[uü]\w[ae]\w{2}[ae]\s[ae]?$", word) for word in text]
  kütüb_reg = [re.findall(r"^\w[uü]\w[uü]\w$", word) for word in text]
  sarahat_reg = [re.findall(r"^\w[ae]\wa\w[ae]t?$", word) for word in text]
  müphem_e_reg = [re.findall(r"^m[uü]\w\w[ae]\w[ae]?$", word) for word in text]
  iyet_reg = [re.findall(r"^\w+?iyy?et?$", word) for word in text]
  sıfat_kıta_reg = [re.findall(r"^\wı\wat?$", word) for word in text]
  fealet_reg = [re.findall(r"^\w[ae]\waat$", word) for word in text]
  mütekamil_reg = [re.findall(r"m[uü]t[ea]\wa\w[ıi]\w", word,) for word in text]
  delail_reg = [re.findall(r"^\we\wa\w?i\w$", word) for word in text ]
  munasip_reg = [re.findall(r"m[uü]\wa\w[ıi]\w?$", word) for word in text]
  hukema_reg = [re.findall(r"^\w?[uü]\we\wa$", word) for word in text]
  muntazam_reg = [re.findall(r"m[uü]\wt[ae]\w[ae]\w[ae]$", word) for word in text]
  mutesebbis_reb = [re.findall(r"m[uü]t[ae]\w[ae]\w{2}[ıi]\w[ae]?$", word) for word in text]
  
  all_words = katib_e_t_reg + katibat_reg + kuttab_reg + kutteb_reg + ketebe_reg + kevatib_reg + mektub_e_reg + mektubat_reg + mekatib_reg + kettab_reg + mekteb_e_t_reg + ketbiyat_reg + iktitab_reg + tektib_reg + mukatebe_reg + inkitab_reg + iktitab_reg + ihmilal_reg + tekettüb_reg + tekatüb_reg + istikbab_reg + kitab_e_reg + tecelli_reg + evvelen_reg  + ekrem_reg + edna_reg + mensubin_reg + cihet_reg + millet_reg + fikret_reg + sükna_reg + mündemic_reg + esrar_reg + mukaddime_reg + gayri_reg
  arabic_words = []
  for i in all_words:
    if i != []:
      arabic_words.append(i)
  arabic_words_test = arabic_words
  for item in arabic_words:
    if item in arabic_words_test:
      arabic_words.remove(item)
  print("The number of Arabic words in the text is", len(arabic_words))
  print("The ratio of Arabic words is", len(arabic_words)/len(text))
  if len(arabic_words) != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(arabic_words)
    else:
      print("Okay!")

def farsi_regex(text):
  farsi_regex_excep = """nane, spontane, elimsende, naaş, naat, nafi, naif, nail, naip, nara, naşi, nabız, nadas, nadim, hayvan, kovan, karavan""".split()
  ane_reg = [re.findall("[\w]+ane", word) for word in text]
  ende_reg = [re.findall("[\w]+ende", word) for word in text]
  na_reg = [re.findall("na[\w]+", word) for word in text]
  van_reg = [re.findall("[\w]+van[^e]", word) for word in text]
  hane_reg = [re.findall("[\w]*hane[\w]*", word) for word in text] 
  nüma_reg = [re.findall("[\w]+nüma", word) for word in text]
  yiş_reg = [re.findall("[\w]+yiş", word) for word in text]
  nim_reg = [re.findall("nim.+", word) for word in text]

  all_words = ane_reg + ende_reg + na_reg + van_reg + hane_reg+ nüma_reg + yiş_reg + nim_reg
  for item in all_words:
    if item in farsi_regex_excep or item in non_tr_exceptions:
      all_words.remove(item)
  persian_words = []
  for i in all_words:
    if i != []:
      persian_words.append(i)
  persian_words_test = persian_words
  for item in persian_words:
    if item in persian_words_test:
      persian_words.remove(item)
  print("The number of Persian words in the text is", len(persian_words))
  print("The ratio of Persian words is", len(persian_words)/len(text))
  if len(persian_words) != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(persian_words)
    else:
      print("Okay!")


def french_regex(text):
  fr_regex_excep = """Karaman, Yaman, Dalaman, sarman, mührüsüleyman, süleyman, asuman, başdanışman, danışman, kahraman, müruruzaman, araştırman, duman, darmaduman, kocaman, koskocaman, doğrultman, 
  morkaraman, muntazaman, akkaraman, zaman, gör, töre, dört, japon, heman, yazman, başyazman, roman, fotoroman, adıyaman, ayırtman, uzman, başuzman, çırakman, kilizman, müslüman, liman, sütliman, tercüman, brahman,
  filaman, harman, hanuman,  kodaman, okutman, toraman, ataman, batman, biaman, derman, dızman, düşman, elaman, ferman, ılıman, katman, mihman, narman, pişman, rahman, sayman, sokman, şişman, tekman, 
  yalman, yazman, akman, alman, azman, ceman, idman, kaman, keman, kuman, orman, saman, seman, şaman, tuman, uçman, umman, zaman, amman, aman, iman, nam,töre, tör, gör,kör, çello, balo, polo, filo, silo, çembalo, pati, 
  on, don, ton, horon, japon, hilye, bezelye, fasülye, sandalye, yer, eyer, siyer, kasiyer, muhayyer, nafile""".split()
 
  fr_regex_excep = list(fr_regex_excep)
  asyon_reg = [re.findall(r"^\w+asyon$", word) for word in text]
  izm_reg = [re.findall(r"^\w+izm$", word) for word in text]
  tör_reg = [re.findall(r"^\w+tör$", word) for word in text]
  aj_reg = [re.findall(r"^\w+aj$", word) for word in text]
  man_reg = [re.findall(r"^\w+man$", word) for word in text]
  ist_reg = [re.findall(r"^\w+ist$", word) for word in text]
  loji_reg = [re.findall(r"^\w+loji$", word) for word in text]
  log_reg = [re.findall(r"^\w+log$", word) for word in text]
  uar_reg = [re.findall(r"^\w+uv?ar$", word) for word in text]
  lye_reg = [re.findall(r"^\w+lye$", word) for word in text]
  on_reg = [re.findall(r"^\w+on$", word) for word in text]
  lo_reg = [re.findall(r"^\w+lo$", word) for word in text]
  arşi_reg = [re.findall(r"^\w+arşi$", word) for word in text]
  ör_reg = [re.findall(r"^\w+ör$", word) for word in text]
  pati_reg = [re.findall(r"^\w+pati$", word) for word in text]
  gram_reg = [re.findall(r"^\w+gram$", word) for word in text]
  tür_reg = [re.findall(r"^\w+tür$", word) for word in text]
  tezi_reg = [re.findall(r"^\w+tezi$", word) for word in text]
  siyel_reg = [re.findall(r"^\w+siyel$", word) for word in text]
  jan_reg = [re.findall(r"^\w+jan$", word) for word in text]
  jer_reg = [re.findall(r"^\w+jer$", word) for word in text]
  iyer_reg = [re.findall(r"^\w+iyer$", word) for word in text]
  atif_reg = [re.findall(r"^\w+atif$", word) for word in text]
  file_reg = [re.findall(r"^\w+file$", word) for word in text]
  sans_reg = [re.findall(r"^\w+sans$", word) for word in text]
  füm_reg = [re.findall(r"^\w+füm$", word) for word in text]

  all_words = asyon_reg + izm_reg + tör_reg + aj_reg + man_reg + ist_reg + loji_reg + log_reg + uar_reg + lye_reg + on_reg + lo_reg + arşi_reg + ist_reg + ör_reg + pati_reg + gram_reg +  tür_reg + tezi_reg + siyel_reg + jan_reg + iyer_reg + atif_reg +file_reg + füm_reg + sans_reg
  for item in all_words:
    if item in fr_regex_excep or item in non_tr_exceptions:
      all_words.remove(item)
  
  french_words = []
  for i in all_words:
    if i != []:
      french_words.append(i)
  
  french_words_test = french_words
  for item in french_words:
    if item in french_words_test:
      french_words.remove(item)

  print("The number of French words in the text is", len(french_words))
  if len(french_words) != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(french_words)
    else:
      print("Okay!")


def greek_regex(text):
  gr_regex_excep = """pancar, panik, panzehir, pankart, panama, pandül, panzer, panda, panel, pano, pantolon, pandispanya, pantürkizm, panslavizm,atik, seyreltik, antik, tik, yitik, bitik, tetik, batik, lastik""".split()
  pan_reg = [re.findall(r"^pan\w+", word) for word in text]
  koz_reg = [re.findall(r"^koz\w+", word) for word in text]
  gram_reg = [re.findall(r"^\w*gram$", word) for word in text]
  tik_reg = [re.findall(r"^\w+tik.+$", word) for word in text]
  aer_reg = [re.findall(r"^aer\w+", word) for word in text]
  graf_reg = [re.findall(r"^\w*[gğ]raf\w*", word) for word in text]

  all_words = pan_reg + koz_reg + gram_reg + tik_reg + aer_reg + graf_reg
  for item in all_words:
    if item in gr_regex_excep or item in non_tr_exceptions:
      all_words.remove(item)
  greek_words = []
  for i in all_words:
    if i != []:
      greek_words.append(i)
  greek_words_test = greek_words
  for item in greek_words:
    if item in greek_words_test:
      greek_words.remove(item)
  print("The number of Greek words in the text is", len(greek_words))
  if len(greek_words) != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(greek_words)
    else:
      print("Okay!")

not_turkish = []
def italian_regex(text):
  it_regex_excep = """alacakaranlık, ala, alaca, alay, alarak, alaz, alan, alaka, alarm, alacak, alacaklı, alabaş, aladağ, alamet, alaybozan, alacakarga, alabildiğine, alacamenekşe""".split()
  ala_reg = [re.findall(r"^ala\w+", word) for word in text]
  ando_reg = [re.findall(r"^\w+[ae]ndo$", word) for word in text]
  to_reg = [re.findall(r"\w+to$", word) for word in text]

  all_words = ala_reg + ando_reg + to_reg
  for item in all_words:
    if item in it_regex_excep or item in non_tr_exceptions:
      all_words.remove(item)
  italian_words = []

  for i in all_words:
    if i != []:
      italian_words.append(i)
  italian_words_test = italian_words
  for item in italian_words:
    if item in italian_words_test:
      italian_words.remove(item)
  for word in text:
    if word in italian_words:
      text.remove(word)
  print("The number of Italian words in the text is", len(italian_words))
  if len(italian_words) != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(italian_words)
    else:
      print("Okay!")

not_turkish = []
def not_turkish_list(words):
  for item in words:
    if item not in not_turkish:
      not_turkish.append(item)

  not_turkish_clean(not_turkish)

def not_turkish_clean(not_turkish):
  non_tr_exceptions = """Sarp elma anne dahi elma hangi hani inanmak kardeş şişman akşamki duvardaki karşıki onunki yarınki yoldaki açıkgöz bilgisayar çekyat hanımeli""".split()
  for item in not_turkish:
    if item in non_tr_exceptions:
      not_turkish.remove(item)

#VOWEL HARMONY
def vh_checker(phrase):
  results = []
  not_vh = []
  yes_vh = []
  no_vh_counter = 0
  for item in phrase:
    for letter in item:
      if letter in 'aıou':
        results.append('back')
      elif letter in 'eiöü':
        results.append('front')
      else:
        results.append('consonant')
    
    if 'back' in results and 'front' in results:
      not_vh.append(item)
      no_vh_counter += 1
    else:
      yes_vh.append(item)
    results = []
  print("The number of words that do not follow vowel harmony in the text:", no_vh_counter)
  for word in not_vh:
    if word in phrase:
      phrase.remove(word)
  if no_vh_counter != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(not_vh)
    else:
      print("Okay!")
  not_turkish_list(not_vh)

#o in second syllable
def o_checker(phrase):
  vowel_list = []
  not_turkisho = []
  o_counter = 0
  for item in phrase:
    for letter in item:
      if letter in 'aeıiuü':
        vowel_list.append('vowel_wo')
      elif letter in 'oö':
        vowel_list.append('vowel_o')
    vowel_list = vowel_list[1:]

    if 'vowel_o' in vowel_list:
      not_turkisho.append(item)
      o_counter += 1
    vowel_list = []

  print("The number of words that have unacceptable vowels in Turkish:", o_counter)
  for word in not_turkisho:
    if word in phrase:
      phrase.remove(word)
  if o_counter != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(not_turkisho)
    else:
      print("Okay!")
  not_turkish_list(not_turkisho)

#b-c-d-g ending
def ending_checker(phrase):
  ending_l = []
  not_turkishb = []
  ending_counter = 0
  for item in phrase:
    for letter in item:
      ending_l.append(letter)
    if ending_l[-1] in 'bcdg':
      not_turkishb.append(item)
      ending_counter += 1
    ending_l = []

  print("The number of words that have unacceptable endings in Turkish:", ending_counter)
  for word in not_turkishb:
    if word in phrase:
      phrase.remove(word)
  if ending_counter != 0:
    print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
    a = input()
    if a == '1':
      print(not_turkishb)
    else:
      print("Okay!")
  
  not_turkish_list(not_turkishb)

#CONSONANT AND VOWEL CLUSTER DETECTOR
alphabet = "b, c, ç, d, f, g, ğ, h, j, k, l, m, n, p, r, s, ş, t, v, y, z, a, e, ı, i , u, ü ,o , ö, A, B, C, Ç, D" \
           "E, F, G, Ğ, H , I, İ J, K, L, M, N, O, Ö, P, R, S, Ş, T, U, Ü, V, Y, Z"

consonants = "B,C,Ç,D,F,G,Ğ,H,J,K,L,M,N,P,R,S,Ş,T,V,Y,Z,b, c, ç, d, f, g, ğ, h, j, k, l, m, n, p, r, s, ş, t, v, y, z"

def is_cons(letter):
    for i in consonants:
        if i == letter:
             return 1
    return 0

def is_letter(x):
    for i in alphabet:
        if x == i:
            return 1
    return 0

def is_word_tr(word):
    for i in range(len(word)-1):
        if is_letter(word[i]) + is_letter(word[i+1]) != 2:
            continue
        if is_cons(word[0]) + is_cons(word[1]) == 2:
            return 0
        if is_cons(word[i]) + is_cons(word[i+1]) == 0:
            return 0
    return 1

b = list()
def test_clusters(text):
  for i in text:
    if is_word_tr(i) == 0:
      b.append(i)
  print("The number of words with unacceptable clusters are:", len(b))
  print("Do you want to see these words? Enter 1 for 'Yes', 0 for 'No'")
  x = input()
  if x == '1':
    print(b)
  else:
    print("Okay!")

def all_funcs(text):
  text = input()
  text = txt_norm(text)
  print("What do you want to do with this text? Options are:")
  print("1- Find Arabic borrowed words",'\n', "2- Find Persian borrowed words", '\n', "3- Find French borrowed words", '\n',"4- Find Italian borrowed words", '\n', "5- Find Greek borrowed words", '\n',"6- Find the words with non-Turkish phonotactics", '\n',"7- All of the above")
  print("Please enter the number of your choice:")
  a = input()
  if a == '1':
    arabic_regex(text)
  elif a == '2':
    farsi_regex(text)
  elif a == '3':
    french_regex(text)
  elif a == '4':
    italian_regex(text)
  elif a == '5':
    greek_regex(text)
  elif a == '6':
    vh_checker(text)
    o_checker(text)
    ending_checker(text)
    test_clusters(text)
  elif a == '7':
    arabic_regex(text)
    farsi_regex(text)
    french_regex(text)
    greek_regex(text)
    italian_regex(text)
    vh_checker(text)
    o_checker(text)
    ending_checker(text)
    test_clusters(text)

text = []
all_funcs(text)

#EVALUATION
#Since the stemmer we found online does not function properly (can not find the roots properly), our recall is lower than what it actually supposed to be

#akvam:
#ACCURACY
arabic_accuracy = 108/134
persian_accuracy = 5/9
french_accuracy = 2/5
greek_accuracy = 2/2
italian_accuracy = 0 #0/0
#RECALL
recall = 117/466
#PRECISION
precision = 117/150

print(arabic_accuracy, persian_accuracy, french_accuracy, greek_accuracy, italian_accuracy, recall, precision)

#FEEDBACK SYSTEM
n = input("Do you think any of the words are not from the stated language?\n Press 1 for 'Yes', 0 for 'No'. : ")
b = list()

if n == '1':
    a = list(input("\nIn which word(s) do you think there is an error? : ").strip().split())
    result = 0
    b.append(a)
elif n == '0':
    result = 1
if result == 0:
    print("\nThe words that you think are stated wrong - ",a)
    print('You think that', len(a), 'words are stated wrong.\nWe will work on making our program better. Thank you for your feedback!')
elif result == 1:
    print("Awesome. Thank you for your interest in our program!")

#print(b)

#DATASETS
akvam = """ 
1329
Mukaddime 
Mütefekkir insanlar, çok endişe-âver iki muamma arasında yaşarlar: Mazi, istikbal. Kütüb-i  mukaddesede insanın ilk vatanı, menşei hakkında sarahat-ı kafiye yok. İnsan-ı iptidâî,  a’mak-ı mazide bir zıll-ı müphem gibi, bir hayalet gibi görünmektedir. İnsan hangi kıtada  zuhur etti? Mehd-i âdemiyet neresidir? Bu suallere, mâlûmat -ı hazıra-i beşeriye arasında,  tamamıyla kanaat verecekleri bulunmuyor. 
Bugün bir sûret-i müsbetede malum olan cihet, insanın mazisi, yüzbinlerle senelik olduğudur.  “Tasavvuf-ı İslami”nin mukaddimesinde dahi izah ettiğimiz gibi hübût-ı  Adem’in yedi bin  senelik bir şey oluşu, Musevilerin yanlış hesaplarından neş’et etmiş olup âleme bu meyanda  bize onlardan intişar eylemiştir. 
Mısır medeniyetinin takriben yetmiş asır evvel mevcut olduğu ve Mısır medeniyetinin malum  olan safahât-ı iptidâîyesinin şekl-i mütekâmili düşünürlerse, insanın bundan pek uzun bir  maziye mâlik olduğuna kat’i delail-i fenniye vardır. Arâzî-i salise ortalarında yaşamış bir  mahlûkun, taştan pek basit ve adi bir nevi balta yaptığı malum olup bu taş baltalardan  yüzlercesi müzehanelerde mahfuzdur. Zekâ ve iradeye delalet eden bu “Mebâdî-i sanat”  baltaları yapan mahlûkun insan olduğuna şüphe bırakmamaktadır. Bugün binlerle envâ-ı  hayvan içinde, bu suretle eser meydana getireni görülmüyor, lakin halen taştan balta imal ve  istimal eden vahşiler görülmüyor! 
Şu halde bu baltaları yapan mahlûkun insanın iptidâi olduğunu kabul etmek kadar makul ve  muvafık bir fikir olamaz. Eğer bu fikri kabul edecek olursak, mazîmiz için beş altı yüz bin  senelik bir zaman kabul etmiş oluruz! 
Ulema-i tabiiyyun ve hukemanın çoğu bu uzunluğu kabul etmiyor. Lakin arâzî-i saliseden  sonra tekevvün eden arâzî-i rabiada, evvelki baltalardan biraz daha muntazam taş baltalarla  beraber bunların sânii olan insanın da kadid-i mütehacciri bulunmaktadır. Bu arazinin  zaman-ı tekevvününden şimdiye kadar bazı tahmine göre lâ-akal üç yüz elli asır geçmiştir!  
Bu tarihi kabul etmekle beraber, insanın ilk vatanı meselesini halletmiş oluyor muyuz? Hayır,  evvela kıtaat-ı hamisenin muhtevi olduğu arâzî-i erbaanın, taharri edilebilen aksamında aynı  taş baltalar bulunmaktadır. Saniyen, Avrupa’da, bulunduğu mevkiye nispetle “Neandertal  insanı Kanstad cinsi” namı verilen insan cinsi kadidi, dünyanın muhtelif noktalarında  keşfedilmiştir. Demek ki şu kadidini bulduğumuz insan, dünyanın her tarafına yayılmış  kesirün-nüfus bir içtimaiyata mensup olup vatanı dünyanın birçok yerleridir. 
Asar-ı metrûke ve mütehaccirat ile iştigal eden tabiiyyunun bazıları, Cava(Java) Ada’sında  Hollandalı Eugene Dubois tarafından keşfedilen bir kadid-i mütehaccirin, Neandertal  insanlarından daha iptidâî halinde olduğunu nazar-ı itibara alarak mehbıt-ı  dem, Java adası  veyahut civarları olduğunu zannetmektedir. Hint’i, Serendip’i, Afrikadaki Bornu(Bernuh)yı  vatan-ı iptidâî-i beşer zannedenler de var. Alman ulemasından birisi de (Cümle-i nebatiye  ve hayvaniyesi, iklimi ve daha birçok şeraiti) itibariyle Avusturalya Adasını menşe-i beşer addetmektedir. Bunların hepsi şimdilik birer zandan ibaret ve menşe-i beşer meçhuldür.  
Akvam-ı iptidâîye yekdiğeriyle ziyade karışmışlardır. Mütemâdî hicretler, mütemâdî  muhalâta ve imtizaçlar, birçok melez cinsler meydana getirmiş ve getirmekte bulunmuştur.  Etnografya ve ensal-i kadime uleması âsar ve mütehaccirattan bu muhâceretlerin mebde ve sırlarını bir dereceye kadar tayin edebilmektedir. Bugün dahi akvam-ı meşhure-i cihanın muhitleri, akvamın sath-ı arza yayılması cihetleri, muhaceret ve mebdeler hakkındaki efkârı  teyit etmektedir.  
Bugün kürre-i arzımızda mevcut olan insanları ekser ulema, renkleri itibariyle, dört büyük  sınıfa taksim etmektedir ki bunların her birine “ırk” namı verilir. Bu dört ırk mensubunu  arasında derinin rengi “sima” kıhfın şekli, tenasüp-i vücut, zekâ, hadisat-ı içtimaiye,  istidat ve derece-i medeniyet cihetleriyle pek muhtelif ve mühim farklar bulunuyor.  
“Irk-ı Ebyaz” hepsinin güzeli ve mütenasipü’l-azası olup medeniyette pek ileri gitmekte,  şayan-ı hayret ve süratle terakki etmekte ve sanayi ve fünunu tekemmül ettirmektedir.  
Bugün kürre-i arzın hâkimi ve mukadderat-ı beşeriyenin sâiki bu ırka mensup olan Avrupa  Aryanlarıdır.  
En kadim medeniyetleri icat eden ve evvelen temeddün ettiğine şüphe edilemeyen “Irk-ı  Asfer” yakın zamanlara kadar mesai-i kadimesinin verdiği yorgunluk altında bîtap ve âtıl  kalmışa benziyordu. Irk-ı Asfer medid bir hâb-ı istirahate dalmıştı. 
Aryanların hakaret ve tecavüz tekmeleri Asfer’i uyandırdı. İptidâlarda yeni uyanan bu  ırkın, yorgunluğunu alıp almadığı ve yeniden cidal-i hayatta faaliyete başlayıp başlamayacağı  meçhul idi. Japonya intibahı, azîm bir inkılabı haber veriyordu. Çin’in şu günlerde  revnüma olan terakkiyat-ı serîası, bu inkılabın çok beklenilmeyeceğini ve umumiliğini  ispat etmektedir. 
“Irk-ı Ahmer” uful etmekte, nesli münkarız olmaktadır. Bu ırkın muhiti Amerika idi.  Amerika, Aryanların eline geçtikten sonra ahâlî-i aslisi olan kırmızılar bir inkıraz-ı serîa düşmüştür. Medeniyetle temas, kırmızıları mahvetmektedir. Bunların medeniyetten en büyük  tehâlükle aldıkları şey, sarhoşluk oluyor. Zaten hayat-ı medeniyenin şerait-i içtimaiyatı,  medeniyet bahçesi yaban güllerine mühlik bir tesir ika etmekte iken işin içine karışması  dâ'ül-küûl de bu ırkı imha etmektedir.  
“Irk-ı Esved” gayet kuvvetli ve mukavemetli olup beşeriyetin tabiata en yakın olan  efradını hâvidir. Bu ırkın mensubîni zekâca biraz dûn ise de beyazlara karşı  mevcudiyetini galibane müdafaa etmekte ve kuvvetlenmektedir. 
Seyahatin temadisi, keşfiyatın tekessürü, coğrafya ilminin tekemmülü sayesinde bugün  kürre-i arzımızın heman meçhul bir ciheti kalmamıştır. Ve tabiîdir ki artık akvam-ı meçhule de kalmamıştır. Lakin coğrafyanın âlem-i medeniyet hakkında bildiğiyle henüz nîm- 
medeni, bedevi ve vahşi akvam ve onların süknâ ve muhitleri hakkındaki mâlûmatı  arasında büyük farklar vardır. Denilebilir ki Asya, Afrika, Amerika ve Avustralya’da sâkin  ekser akvam hakkındaki mâlûmat -ı hazıramıza, henüz pek sathi ve alelacele toplanmış  şeylerdir. Kati ve kâfi mâlûmat istihsali için daha pek çok mesaiye ve uzun zamana lüzum  var. Bu sebebe mebni Merih’in kanallarını milyonlarla fersah baidlerdeki ecramı tetkik  eden ve a’mak-ı vücuda infaz-ı nazar etmek davasında olan fen, henüz kürre-i arzımızda  yaşayan ebnâ-yı insanın nüfus-ı hakikisini bilmiyor! 
Filvâki insaniyetin nüfus-ı hakikisi bilinmek için mükemmel tahrir-i nüfus icrası, vefiyat  ve tevellüdat cetvelleri ve daha birçok şeyler lazîmdır. Hakikate en yakın sayılan ve en son  tahmine göre kürre-i arzımızda: bir milyar yedi yüz milyon insan var. Onlar kıtat-ı hamseden  
dördü, Avrupa nispetinde ahaliye malik olsaydı, bugün sekene-i arzın beş buçuk milyar  olması icap ederdi. Her kıtada sâkin nüfus-ı insaniye ber-vech-i atidir.  
Avrupa’da: 430,000,000 
Asya’da: 873,000,000 
Afrika’da: 150,000,000 
Amerika’da: 163,000,000 
Okyanusya’da: 54,000,000 
Sekene-i arz: 1,670,000,000 
Bu aded-i takrîbînin akvama taksimi pek karışıktır. Uruka taksiminde dahi henüz kati ve  muttarit bir usûl kabul edilmemiştir. Bâlâdaki gösterdiğimiz dört ırk, pek sathi bir  taksimdir. Teşrih ve teşekkülat-ı vechiyesi itibariyle Irk-ı Ebyaz’a mensup nice kavimler  var ki renkleri itibariyle kırmızı veyahut siyah ve açık siyahtır. Somali, Habeşi, Tibous  vesaire gibi.  
Urukun ihtilâtıyla derecat-ı muhtelifede melezleşmiş ve ırk usulüyle bir taksim-i eşkâl  eden akvam da çok. Bir kısım Hindîler ve bazı Okyanusya Adalıları gibi. Binâberin yine bir  hesab-ı takribî olmak üzere, bâlâda gösterilen nüfus-ı beşeriyenin dört ırka taksimi ber vech-i atidir. 
Irk-ı Ebyaz: 768,000,000 
Irk-ı Asfer: 750,000,000 
Irk-ı Esved: 142,000,000 
Irk-ı Ahmer: 10,000,000 
Mecmuu İnsan: 1,670,000,000 
İnsanların tebeiyyet ettikleri edyan veyahut bir dine ittiba etmemek itibariyle taksim etmek  lazîm gelirse netice-i âtiye hâsıl olur: 
Muhammedi: 300,000,000 
İsevi: 450,000,000 
Musevi: 12,000,000 
Dinsiz: 100,000,000 
Brahmani: 100,000,000 
Buda Çini: 500,000,000 
Putperest: 158,000,000 
Toplam: 167,000,000 
Tekellüm etmekte oldukları elsine itibariyle dahi taksim-i âti husule gelir: Arap lisanını söyleyen: 50 milyon 
Türk ve şuubatı: 80 milyon 
Farisi: 10 milyon 
Hindistan ve şuubatı: 270 milyon 
Çin: 370 milyon 
Malayi: 50 milyon 
Japon: 50 milyon 
Berberi: 10 milyon 
İngiliz: 130 milyon 
Slav şuubatı: 120 milyon 
Alman: 80 milyon 
İspanyol: 70 milyon 
Fransız: 45 milyon 
İtalyan: 35 milyon 
Muhtelif: 300 milyon 
Toplam: 1670 milyon 
Levhalarımızın birisi efrad-ı beşeriye içinde ne bedia-nüma güzelleri ve mâmâfih ne kadar  da kerih-ül manzar ve ifrite benzerleri bulunduğunu gösteriyor. Diğer levhamızda dört  ırktan 
Bu üç resimden sağda olan Irk-ı Ahmer’e mensup bir kabile reisidir. Aşağıda Irk-ı Esved’den  bir zenci kadınıdır. Üçüncüsü Irk-ı Ebyaza mensup bir İngiliz kadını olup kitabın başındaki  resim de Irk-ı Asfer’e mensup zarif bir Çinli kadındır. Bu dört resmin tetkikinden şüphe  kalmaz ki uruk-ı beşer arasındaki zâhirî ve şekli farklara rağmen insan birkaç nev’ olmayıp cümlesi bir ailenin muhit ve tesirat-ı saire yüzünden tebeddülata dûçar olmuş evlatlarıdır.
Birer numune göstermektedir. Bu tefavütler mütefenninlerin iki kısma ayrılmasına sebep  olmuştur. Bir kısmı “ Vahîd’ül-Menşe” fikri taraftarlarıdır ki onlara göre bütün insanlar  kürre-i arzın bir noktasında peyda olmuş, bir aileden türemiş ve sonra tedricen dünyanın  
her tarafına yayılmıştır. Bugün uruk-ı beşer arasında müşahade olunan fark ise muhit,  tevarüs, tegaddi, ihtilat ve adem-i ihtilat vesaire gibi avamil-i tabiiye ve  içtimaiyenin âsar-ı tesiratıdır. Uruk arasındaki fark, onların ayrı ayrı cinslere taksimini icap  edecek mahiyette değildir. Akvam-ı beşeriye arasındaki fark ise, ya hiç ihtilat etmeyip uzun  müddetler avamil-i mahsusa-i muhitiye ile temeyyüz veyahut da melezleşme usulüyle  tenevvüden ibarettir.  
“Kesir’ül-Menşe” fikri taraftarlarına göre ise keyfiyet bunun aksinedir. İnsanlar, muhtelif  noktalarda peyda olmuştur. Her ırk ayrıca bir cinstir. Irklar arasındaki fark, ihtilat ve adem-i  ihtilat vesaire sebebiyle hasıl olmuş ârızî farklar değil, ayrı ve müstakil bir cinsiyeti irâe  eden farklardır. Melezler daima inkıraz ve istihaleye mahkûm olup ayrıca bir ırk  meydana getiremezler. 
Bu iki fikirden şu ikincisi, birinciye nispetle daha meşkûk ve ispatı müşkildir. Fazla  olarak da ne an’ane-i diniyeye ve ne de kavaid-i müspete-yi fenniyeye muvafık gelir.  Bugün insanla meskûn olan arazinin bir kısm-ı mühimmi edvar-ı kadime-i arziyede henüz sular altında idi. Nasıl ki nice meskûn arazi muahharan inhitat etmekle bugün  ka’r-ı deryada bulunmaktadır. 
"""

aborda = """
Aborda Olmak
   YANAŞIRKEN:

1.Motoru çalıştırın. Yelkenli bir teknenin yanaşma ve ayrılma manevraları, aksi bir durum yoksa motorla yapılır.
2.Yelkeni ancak motoru çalıştırdıktan sonra indirin.
3.Planınızı yapın ve bunu mürettebatla paylaşın.
4.Rüzgarüstüne aborda olmak en kolay yanaşma manevralarından birisidir.  Bu şekilde aynı zamanda ayrılırken de çok rahat edilir.
5.Yanaşırken rüzgarın yönü ve şiddetini, varsa akıntı durumunu, yanaşılacak yeri ve kendi teknenizin özelliklerini değerlendirin.
6.Olası aksilikleri değerlendirin ve B planı oluşturun. “Eğer yanaşamazsak çıkıp alargada demirleyeceğiz” gibi

 

7.Dingiyi, eğer kıçtan çekiyorsanız diğer taraf bordasına sabitleyin.
8.Eğer bir tekneye bordalayacaksanız, tekne sahibi veya kaptanını haberdar etmek gerekir.
9.Eğer bir yelkenli tekneye bordalıyorsanız, tekne direklerinin ve gurcatalarının olası bir dalga ya da yalpada birbirine çarpmaması için uygun şekilde ayarlayın. 

10.Bordalanacak yerin tekne ile aynı yükseklikte olması tercih edilir. Koltuk halatının 30º’den dik bir açıyla gelmesi, diğer bir deyişle küpeşteye paralel olmaması yüzünden koç boynuzu veya kurt ağzını güverteye tespit eden cıvata ve benzeri bağlantıları zorlaması, ileri durumlarda tamamen kopartması söz konusu olabilir. Yüksek bordalı tekneler veya pontonlara yanaşırken, özellikle de rüzgarlı ve dalgalı sularda çok dikkat etmek, mümkün mertebe bağlanmaktan kaçınmak gerekir

11.Özellikle sert rüzgar ve dalgalı deniz sözkonusuysa, elde bir balon usturmaçalı güvertede serbest bir veya birkaç ekip üyesinin çarpışma anında, tekne ile çarpılan aralığa sokarak önlem almaları gerekebilir.

Teknenin çarpışma anında el ayak yoktur, usturmaça vardır!

12.Örneğin iskele ayakları gibi düz olmayan bir zemine bordalanıyorsa, pasarella ile usturmaçaların görevini yapması sağlanır.Önce rüzgarüstü koltuk halatı sahile verilir.

 



13.Sahilde kimse yoksa, birisinin önceden atlayıp halatı alması ve uygun şekilde bağlaması gerekebilir.
14.Sahile verilen halatlar, sahilde anele, baba veya koç boynuzlarına izbarço ile bağlanabilecekleri gibi doblin yapılarak geri alınabilirler 
Ucu tekne tarafında sabit, sahilde veya iskelede anele veya babadan geçtikten sonra tekrar tekneye alınır ve diğer ucu yine teknede sabitlenir. Bu şekilde ayrılırken sahile çıkıp, o tarafı çözmeye gerek kalmayacaktır.
15.Tekne yanaştıktan sonra, açmazlarla tekne uzun hattının iskele ya da pontona paralel olması sağlanır.
Yelkenli teknelerin, motorlu teknelerden farklı olarak yelkenlerini indirmiş dahi olsalar; direk, arma ve bordaları sebebiyle rüzgarla temas eden yüzeyi fazladır, bu yüzden rüzgaraltına kolaylıkla sürüklenirler. Yapılacak manevrada bunu hesaba katmak önemlidir. 
Tüm tekneler kural itibarıyla rüzgarı kafadan aldıklarında daha stabildirler. 
Pervane kanatlarının şekli dolayısıyla birçok tekne tornistanda iskeleye veya sancağa çeker. Alışıldığında, motorla yanaşırken, özellikle dar yerlerde avantaj olarak kullanılabilecek bir özelliktir. 
"""

inönü = """
Reis-i cumhur sıfatiyle cumhuriyetin kanunlarına ve hakimiyet-i milliye esaslarına riyaet ve bunları müdafaa, Türk milletinin saadetine sâdıkane ve bütün kuvvetimle sarf-ı mesai,
Türk devletine teveccüh edecek her tehlikeyi kemal-i şiddetle men, Türkya'nın şan-ı şerefini vikaye ve ilaya, ve deruhte ettiğim vazifenin icabatına ... etmekten ayrılmayacağıma 
namusum üzerine söz veririm.
"""

otkütür = """Haute Couture


Chanel tarafından 1965 yılında üretilmiş haute couture etek-ceket takım.
Haute couture (Türkçe okunuşu: otkutür) kişinin özel siparişi üzerine hazırlanmış, özel dikim giysi anlamına gelen ve Fransızca'dan gelen bir moda terimidir. Tam karşılığı ise "yüksek dikiş"dir. Buna karşın, her özgün ya da kişiye özel dikilen tasarım haute couture olarak sınıflandırılmaz Genellikle üst gelir seviyesinde elit müşterilerin ölçülerine ve beğenisine göre hazırlanan giyim türüdür. Yani kişinin kendi tercihlerine göre tasarımcının tasarımında değişiklikler yapılmasına olanak sağlar. Gelinlik buna bir örnek olabilir fakat haute couture sadece abiye değil müşterilerin günlük giyim ihtiyaçlarını da karşılar. Bir moda evinin Haute Couture Sendikası'na (Chambre Syndicale de la Haute Couture) üye olabilmesi için hem abiye hem de günlük giyim üretiyor olması gerekir.

Günümüzde tüm dünyada yaklaşık 4,000 haute couture müşterisi kaldığı tahmin edilmektedir. Yanlış bilinenin aksine haute couture müşterinin çoğunluğunu ünlüler değil, adını dahi bilmediğimiz çok zengin ailelerin mensupları oluşturmaktadır. Haute couture dikilen sade bir etek-ceket takım 20,000 Euro gibi bir fiyattan başladığı gibi işlemeli parçalar ve gece elbiseleri altı rakamlı fiyatları bulmaktadır. Fransa ve Avrupa'daki üretim maliyetlerinin çok artmasından dolayı günümüzde yüksek satış fiyatlarına rağmen moda evlerinin haute couture bölümü şirketlere kar getirmemektedir. Buna rağmen, moda evlerinin parfüm ve çanta gibi daha uygun fiyatlı ürünlerinin satışına yardımcı olduğundan dolayı bir reklam gideri olarak, haute couture atölyeleri yaşamını sürdürmeye devam etmektedir. Balmain, Balenciaga gibi bazı markalar haute couture atölyelerini kapatmış ve günümüzde sadece hazır giyim (pret-a-porter) ürütmektedir.

1700'lerde ilk adımları atılan Haute Couture akımı, Fransa'da 19. yüzyıl sonlarında günümüzdeki anlamını kazanmıştır. Bir "haute couture" atölyesi olabilmek için, Haute Couture Sendikası'na (Chambre Syndicale de la Haute Couture) üye olmak gerekmektedir. Bu sendikaya üye olabilmek için ise atölyede çalışacak insan sayısından çalışanların saat ücretine, dekorasyonundan üretim adetlerine kadar her konuda belli kurallar bulunmaktadır. Atölyeler her yıl defile başına en az 35-40 parçadan oluşan 2 koleksiyon hazırlamakla yükümlüdür. Tüm kıyafetler yüzlerce saatlik uğraşlar sonucu yalnızca elle dikilmektedir. Tamamen insan emeğine ve becerisine dayalı bu akım, yalnızca çok özel bir kesime hitap etmektedir.

Haute Couture Sendikası'nın (Chambre Syndicale de la Haute Couture) üyeleri: (Günümüzdeki ve geçmişteki üyeler)

Armani Prive
Atelier Versace
Balenciaga (eski üye)
Balmain (eski üye)
Chanel
Christian Dior
Christian Lacroix (eski üye)
Christophe Josse
Dice Kayek (konuk üye)
Elie Saab
Emanuel Ungaro (eski üye)
Escada (eski üye)
Louis Féraud (eski üye)
Franck Sorbier
Giambattista Valli
Givenchy
Guy Laroche (eski üye)
Jean Paul Gaultier
Jeanne Lanvin (eski üye)
Ted Lapidus (eski üye)
Mak Shoe (eski üye)
Maison Martin Margiela
Nina Ricci (eski üye)
Paco Rabanne (eski üye)
Pierre Cardin (eski üye)
Rochas (eski üye)
Schiaparelli
Stéphane Rolland
Thierry Mugler (eski üye)
Valentino
Victor & Rolf
Yves Saint Laurent (eski üye)
Uluslararası olarak haute couture sayılmasa da, Yıldırım Mayruk, Vural Gökçaylı, Dilek Hanif gibi tasarımcılar Türkiye'deki haute couture standartlarında üretim yapan moda evlerine örnek gösterilebilir.

moda = """
Christian Dior’dan Chanel'e, Iris Van Herpen'den Schiaparelli'ye, lüks moda evlerinin Paris Haute Couture Haftası'nda tanıttığı İlkbahar-Yaz 2021 koleksiyonlarını keşfedin.

Christian Dior
Christian Dior’un doğayla ilgili inançlarına ve kaderin işaretlerine olan tutkusuna adanan bu koleksiyon için Maria Grazia Chiuri, 15. yüzyılda İtalya’da ortaya çıkan Tarot kartlarından ve Rönesans dönemi tablolarından ilham alıyor. Romalı sanatçı Pietro Ruffo tarafından yeniden yorumlanan Tarot desenleri ve Maison atölyelerinde çalışılan benzersiz işçilik, olağanüstü gece elbiselerinde buluşuyor.


Tıpkı bir önceki Haute Couture koleksiyonunda olduğu gibi, bu koleksiyonun sunumu için hazırlanan filmin yönetmenlik koltuğunda Matteo Garrone oturuyor. Floransa’daki Sammezzano Kalesi’nde çekilen ve “Le Château du Tarot” (Tarot Şatosu) adını taşıyan film ile, Haute Couture’ün bir ihtimaller ve deneyimler dünyası olduğu gözler önüne seriliyor.

Chanel

 

Chanel’in İlkbahar-Yaz 2021 Couture koleksiyonu, tüm görkemi ile görücüye çıktı. U2 ve Depeche Mode gibi müzik grupları ve Hollandalı yönetmen Anton Corbijn tarafından çekilen klipte, arka plan olarak Paris’teki 31 Rue Cambon’daki Chanel atölyesini gördük. Couture atölyesinde terzilerin çalışmaları ve model provaları renkli ve siyah beyaz karelerle sunuldu, geçişler oldukça etkileyiciydi!

Valentino

Valentino’nun 2021 İlkbahar/Yaz Haute Couture koleksiyonundaki parçalar, doku ve formlarıyla göz kamaştırıyor. Markanın kreatif direktörü Pierpaolo Piccioli’nin imzasını taşıyan koleksiyonun gösterimi, Massive Attack üyelerinden İngiliz sanatçı Robert Del Naja'nın katkılarıyla Roma'daki Galleria Colonna'da gerçekleştirdi.

Giambattista Valli

Giambattista Valli, 2021 İlkbahar/Yaz Haute Couture koleksiyonunda "Abartıdan korkma ve evde kal" mesajını verirken, Haute Couture'ün sadece büyük hacimler ile gösterişli olabileceğine inandığının altını çiziyor.

Fendi

Fendi’nin 2021 İlkbahar/Yaz Haute Couture koleksiyonu, VirginiaWolf'un Orlando romanından ilham alarak hazırlandı. Kim Jones’un hazırladığı koleksiyon; Naomi Campbell, Christy Turlington ve Bella Hadid gibi yıldız modellerin boy gösterdiği bir defile ile tanıtıldı.

Schiaparelli

Schiaparelli 2021 İlkbahar/Yaz Haute Couture koleksiyonunu yaklaşık dört dakikalık bir filmle tanıttı. "Bedeninizin gerçeğinin farkına varmanızı sağlayan, dünyada nasıl hareket ettiğinizi düşünmenizi sağlayan kıyafetler.” olarak koleksiyonu tanıtan markanın kreatif direktörü Daniel Roseberry; göz alıcı tasarımlar sunuyor.

Iris Van Herpen

Iris Van Herpen’ın Merlin Sheldrake'in Entagled Life kitabından ilham alınarak tasarladığı koleksiyon için "Root of Rebith" adını verdi. Markanın 2021 İlkbahar/Yaz Haute Couture koleksiyonu yaklaşık 9 dakikalık bir video ile tanıtıldı. 3D baskıların ön planda olduğu koleksiyonda, moda ve teknolojinin etkileyici bir harmanı gözler önüne serildi. 
"""

erdogan = """
Cumhurbaşkanı Recep Tayyip Erdoğan, "Geçtiğimiz yıl Ayasofya'yı yeniden ibadete açarak, önceki yıl Büyük Çamlıca Camii'ni hizmete vererek, dün de Taksim Camii'nde ilk cumayı eda ederek ecdadın mirasına sahip çıktığımızı gösteriyoruz." dedi.
Cumhurbaşkanı Erdoğan, Okçular Vakfı 9. Uluslararası Fetih Kupası programına video mesaj gönderdi.


Erdoğan, "Aziz milletim, sevgili İstanbullular, Uluslararası Fetih Kupası'nın 9'uncusu vesilesiyle Okmeydanı'nda bir araya gelen kıymetli sporcularımız, değerli misafirler, hepinizi en kalbi duygularımla, muhabbetle selamlıyorum." diyerek başladığı konuşmasında, İstanbul'un fethinin 568. yıl dönümünün hayırlı olmasını diledi.

Fatih Sultan Mehmet Han başta olmak üzere İstanbul'u fethedip milletin ebedi şehri haline getiren kutlu ordunun her bir ferdine şükranlarını ileten Erdoğan, "Bin yıldır bu toprakların vatanımız olması için gözlerini kırpmadan canlarını feda eden tüm şehitlerimizi, gazilerimizi, kahramanlarımızı rahmetle şükranla yad ediyorum. Fetih Kupası Okçuluk Yarışmalarına Türkiye ile özellikle 30'dan fazla ülkeden gelerek iştirak eden 200 sporcumuza başarılar diliyorum. 'Ya Hak' diyerek attıkları oklarıyla fetih ruhunu günümüze taşıyan okçularımıza özellikle teşekkürlerimi sunuyorum." diye konuştu.

"İstanbul'umuzu geliştirip güzelleştirerek emaneti koruyoruz"

Yarışmanın bir spor müsabakası olmanın ötesinde çağlar açıp çağlar kapatan o büyük dönüm noktasının manasının nesilden nesile aktarıldığı bir kültür festivali olduğunu aktaran Erdoğan, şöyle devam etti:

"Salgın şartları sebebiyle arzu ettiğimiz coşkuyla gerçekleştiremiyor olsak da Fetih Kupası'nda somutlaşan fetih heyecanının tüm gençlerimizin yüreklerini dalga dalga sardığına inanıyorum. Biz geçtiğimiz yıl Ayasofya'yı yeniden ibadete açarak, önceki yıl Büyük Çamlıca Camii'ni hizmete vererek, dün de Taksim Camii'nde ilk cumayı eda ederek ecdadın mirasına sahip çıktığımızı gösteriyoruz.

Yollarıyla köprüleriyle Marmaray'la Avrasya Tüneli'yle metrolarıyla parklarıyla hepsinden önemlisi doğrudan insanımıza sunduğumuz nice hizmetlerimizle İstanbul'umuzu geliştirip güzelleştirerek emaneti koruyoruz. Fatih'in İstanbul'daki ilk vakfiyesi olan Okçular Vakfı bünyesinde yürütülen faaliyetleri hem ecdadın hatırasını ve kadim geleneklerimizi yaşatma hem de gençlerimizi sporla buluşturma işlevleriyle bu çerçevede takdirle takip ediyoruz."

"Gençlerimizle adım adım, büyük ve güçlü Türkiye'yi inşa ediyoruz"

Vakfın bünyesindeki gençlerin Malazgirt'ten İstanbul'a, oradan yurt dışındaki etkinliklere kadar uzanan başarılı çalışmalarıyla gurur duyduklarını kaydeden Cumhurbaşkanı Erdoğan, "Biz gençlerimizle birlikte Malazgirt'te Alparslan'ın cesaretini, Söğüt'te Osman Gazi'nin rüyasını, İstanbul'da Fatih'in devrimini, Ankara'da Gazi Mustafa Kemal'in dirayetini, 15 Temmuz'da istiklaline sahip çıkma iradesini yaşatarak adım adım, büyük ve güçlü Türkiye'yi inşa ediyoruz.

Kanlarımızla ve terlerimizle sulayarak vatan yaptığımız bu topraklara mührünü vurduğumuz medeniyetimizi yeniden yükseltecek ve zirveye çıkartacak olan işte bu gençlerimizdir. Dün okçularımızla yazdığımız destanı bugün insansız hava araçlarımızla yazılımlarımızla üretimimizle ihracatımızla tekrarlıyoruz."

Cumhurbaşkanı Erdoğan, bütün bunları da tıpkı ecdadın okçuluğa verdiği ehemmiyetin, ona yüklediği misyonun hassasiyetiyle yürüttüklerini belirterek, konuşmasını şöyle tamamladı:

"Okmeydanı'na abdestsiz girilemeyişi, müsabakalara mutlaka besmeleyle başlanması, sınavlarda ok kullanma kabiliyeti yanında; ahlakın ve karakterin de dikkate alınması bize bugün takip etmemiz gereken yolu da gösteriyor. Kökleriyle bağı kopmuş bir ağacın ayakta kalamayacağı gibi inanç ve kültür kökleriyle bağı kopmuş bir toplum da varlığını uzun süre devam ettiremez.

Gençlerimizden okçuluk, binicilik, kılıç, hat, tezhip gibi geleneksel spor ve sanat dalları ile günümüze ait her türlü sosyal ve kültürel faaliyeti işte bu anlayışla yürütmelerini bekliyoruz. Aklıselim ile düşünen, kalbiselim ile hisseden, zevkiselim ile inşa eden gençlerimizi gördükçe geleceğimize daha bir güvenle bakıyoruz.

Bu duygularla Uluslararası Fetih Kupası'nın 9'uncusunun başarılı geçmesini diliyorum. Sizlerin nezdinde geleneksel spor dallarımıza sahip çıkan gençlerimizin her birine teşekkürlerimi iletiyorum. Dünyanın farklı ülkelerinden gelerek Fetih Kupası'na iştirak eden tüm sporcularımızı canı gönülden tebrik ediyorum. Hepinizi bir kez daha sevgiyle saygıyla selamlıyorum. Kalın sağlıcakla."
"""

dil_beyti ="""
Açıldı çün bezm-i elest
Devr eyledi peymânesi
Andan içenler oldu mest
Ayılmadı mestânesi

Ol bâdeden kim nûş ider
İçdiği dem serhôş ider
Deryâ gibi ol cûş ider
Esrük olur dîvânesi

Savm-ı sivâyı kim tutar
Iyd-i visâle ol yeter
Bülbül gibi dâim öter
Gülşen olur kâşânesi

Bayrâma ol âşık irer
Kim Hak cemâlini görer
Dost bezminin zevkin sürer
Pür-nûr olur dil-hânesi

Aç gözünü Hak ile bak
Oku Hüdâyî'den sebak
Kâmil olurmuş ehli-i Hak
Doğmazdan evvel ânesi
"""

bardakçı = """Münir Nureddin
Geçen hafta, Münir Nureddin Selçuk’un vefatının 40. yıldönümü idi...

Çocukluk ve gençlik senelerinde alaturka musikinin birinci sınıf icralarını dinlemiş ve kulakları o nağmelerle dolu olanların gönlünde Münir Nureddin, Safiye Ayla, yahut Necmi Rıza gibi büyük sanatçıların yerleri bambaşkadır.

Hiç unutmam, 1981’in 29 Nisan’ında Münir Bey’in cenazesine iştirak edip büyük sanatkârın Âşiyan’a defninden sonra 1965’de vefat etmiş olan bestekâr Refik Fersan’ın hanımı kemençe icracısı Fahire Fersan’ın Mecidiyeköy’deki evine uğramıştım. Fahire Hanım “İki fatiha okudum” demişti. “Biri 70 senelik arkadaşım Münir’e, öteki de musikiye... Bu iş artık bitti!”.

Fahire Hanım’ın söyledikleri maalesef doğru çıktı! Bir zamanların haşmetli, gümbür gümbür ve dinamik musikisi artık yoktur! İmparatorluk mirası olan tantanalı musikinin yerini şimdi ağlamalarla ve inlemelerle dolu vıcık vıcık nağmeler almıştır. “Millî musikimiz”, “ilâhî nağmeler”, “ruh pınarlarının bilmemnesi” veya “gönül damlaları” gibisinden tuhaf ve ucuz sıfatlar verilen ama geleneksel müziğimiz ile hiç alâkası olmayan zamane müziğini icra eden hanım solistler kalın perdelerden haykırmakta, erkek okuyucular kendi seslerinden mest olmuş vaziyette fakat ıztırap çeken bir çehre ile güya icrâ-yı sanat etmektedirler.


Velhasıl alaturka musiki artık yerlerdedir, bugün icra edilen müziğin hakiki Türk Musikisi ile hiçbir alâkası kalmamıştır. Çöküş sebeplerinin başında sanatkârların çalışmamaları, eski kayıtları dinlememeleri, neticede zevksizleşme, bir anda “Ben oldum!” havalarına girme ve dinleyiciyi salgın gibi etkisi altına alan zevk ve kulak kirlenmesi gelir.

BİZ YAZAMADIK, BİR İRLANDALI YAZDI!

Münir Nureddin’in musikimizdeki önemini ve yerini burada anlatmam gereksizdir, musikiye getirdikleri ve vefatı ile beraber götürdükleri bilenlerin zaten malûmudur...

Geçen hafta, Münir Bey’in vefatının 40. yıldönümü münasebeti ile tek-tük yazılar yazıldı, hakkında birkaç konuşma yapıldı ama bunların hepsi senelerdir yazılıp söylenenlerin tekrarı idi, yeni hiçbirşey yoktu...

Münir Bey hakkında bilinmeyenleri de maalesef biz yazamadık, bu işi İngiltere’deki Cardiff Üniversitesi’nin profesörlerinden İrlandalı müzikolog John Morgan O’Connell yaptı. O’Connell’in Münir Nureddin’i anlattığı “Alaturka: Style in Turkish Music”, yani “Alaturka: Türk Müziği’nde Üslûp” isimli kitabı 2013’te Londra Üniversitesi’ne bağlı çok önemli bir okul olan SOAS tarafından yayınlandı ama Türkçe’ye çevrilmedi.

O’Connell kitabını aslında 2000’lerin başında yazmış, öncelikli kaynak olarak Münir Bey’in geçenlerde vefat eden kızı Meral Selçuk’ta bulunan evrakını kullanmıştı...

Kitabı okuduğunuzda, Münir Nureddin’i tanımamış olanların bugün Münir Bey hakkında bildikleri birçok şeyin yanlış olduğunu, meselâ “gençliğinde Paris’e giderek konservatuvara devam ettiği” söylentisinin gerçekle alâkasının bulunmadığını, Münir Bey’in Paris’teki musiki eğitiminin birkaç özel ders ile bazı konserleri dinlemekten ibaret kaldığını görür ve Türk Müziği’ne getirdiği yeni icra tavrının yüksek zevkinin neticesi olduğunu görürsünüz...


ÇÖPÇÜ MAAŞINI BİLİR MİSİNİZ?

Sırası gelmişken, üstad hakkında sadece yakın çevresine malûm olan birkaç acı hâdiseyi de nakledeyim:

Münir Bey’in emekliliği yoktu! Musikiyi 60 küsur sene boyunca ve en üst seviyede icra etmiş, Cumhuriyet’in ilk senelerinde Ankara’da Riyaset-i Cumhur Fasıl Heyeti’nde, yani Mustafa Kemal’in alaturka musiki grubunda çalışmış ama emeklilik hakkına sahip olamamıştı.

Yaşlılığında bazı sıkıntılar başgösterince, yanlış hatırlamıyorsam, zamanın İstanbul Belediye Başkanı Ahmet İsvan üstad için belediyede bir kadro ayarlayıp cüz’î de olsa aylık almasını sağladı.

Ama öyle danışman, sanatçı vesaire değil, “çöpçü” kadrosu! Belediye Başkanı’nın elinden ancak bu kadarı gelebilmiş, Ankara’nın “devlet sanatçılığı” dağıttığı o günlerde Münir Nureddin’i kimseler hatırlamamış ve musikinin büyük üstadı İstanbul Belediyesi’nden “çöpçü” aylığı almaya devam etmişti.

Derken aradan birkaç sene geçti, İstanbul’da “Türk Musikisi Devlet Konservatuvarı” kuruldu ve konservatuvarın kurucu başkanı Ercümend Berker, Münir Bey’i belediye çöpçülüğünden okulun hoca kadrosuna nakletti. Ama üstad artık yaşlı ve hasta idi, okula gidip ders vermesi mümkün değildi, bu yüzden sembolik mahiyette tek bir defa ders verdirildi ve aylığı vefatına kadar ödendi.

Ama memlekette karaktersiz herif mi ararsınız?

Münir Bey’in vakti zamanında musiki bakımından zayıf bulduğu için korosuna almadığı ve sonraları konservatuvarda hocalık kapabilmiş bir adam aklı sıra intikam peşine düştü Maliye’ye bir ihbar mektubu gönderip “Münir Nureddin Selçuk okulda ders falan vermeden boş yere aylık alıyor” dedi!


Maliye ne yapsın? Mecburen soruşturma açtı, prosedür işledi, ifadeler alındı, bu arada Münir Bey’in dostları Ankara’yı devreye soktular ve üstadın son günlerinde sefalet çekmesinin önüne bu sayede geçilebildi...

LİSANSÜSTÜ CEHALET!

Bilgi görgü ve sanat bahislerinde vaziyetin nasıl vahim hâle geldiğini şahsen yaşadığım bir hadiseyi naklederek anlatayım:

Konservatuvarı bitirip lisansüstü bilmemne yapan gençlerden biri, bir dostumun tavassutuyla, tezi hakkında birşeyler sormak için beş-altı sene önce evime gelmişti...

“Genç” diyorum ama öyle yeni mezun delikanlı falan değil, otuzunu geçmiş koskoca adam...

Geldi, kütüphaneme geçtik... O gün evrak, fotoğraf, vesaire tasnifi ile meşguldüm; ortalık biraz karışıktı ve yerde yerleştirilmeyi bekleyen fotoğrafların üzerinde Münir Bey’in büyük boy ve gayet bilinen bir resmi duruyordu...

Konservatuvar mezunu herif fotoğrafa baktı, sonra birşey söylemek ihtiyacını hissetti ve “Dedeniz mi?” diye sordu!

Sadece “Yallah, yürü git, beni günaha sokma!” deyip herifi kapıdışarı ettiğimi hatırlıyorum!

Burada, 40 sene önce kaybettiğimiz Münir Nureddin’in bilinmeyen bir ses kaydını, son bestelerinden olan ve “Sesin bir ışık bana her hicran gecesinde” mısraı ile başlayan Nihavend eserinin bir bölümünü yayınlıyorum...

Kayıt, 1970’lerin sonlarına doğru Münir Bey’in en yakın dostlarından rahmetli Orhan Telmen’in evindeki bir akşam yemeğinde, sofrada yapılmıştır. Münir Nureddin “Sesin bir ışık bana”yı bir hanım talebesi ile saz refakati olamadan okumakta ve şarkının bazı kısımlarını da iki sesli icra etmektedirler.

Kaydı dinlerken Münir Nureddin’in nerede ise seksen yaşında olduğunu gözönüne alırsanız, sanatının gücünü daha mükemmel şekilde farkedersiniz...

John Morgan O’Connell’in Münir Nureddin Selçuk hakkında 2013’te yayınladığı kitap. O’Connell’in eseri Türkçe’ye hâlâ çevrilmedi.

Cumhuriyet’in ilk senelerinde Ankara’da, Riyase-i Cumhur, yani Cumhurbaşkanlığı İncesaz Heyeti’nde görevli olan Burhaneddin (Ökte), Refik (Fersan), Hafız Yaşar (Okur) ve Münir (Münir Nureddin Selçuk) Beyler’in, 23 Eylül 1925’te Mustafa Kemal Paşa’nın emri ile ve onunla beraber Bursa’ya gitmeleri konusunda verilen talimat (Cumhurbaşkanlığı Arşivi, 1015048-37)

Münir Nureddin, “Sesin bir ışık bana her hicran gecesinde” mısraı ile başlayan eserini 1970’lerin sonlarında bir dostunun evindeki akşam yemeğinde bir öğrencisi ile beraber okuyor.
"""
