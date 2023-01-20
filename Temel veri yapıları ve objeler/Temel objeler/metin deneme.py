s="The term originated in the early 17th century, simultaneously with opera and oratorio. [citation needed] Prior to that, all cultured music was vocal. With the rise of instrumental music the term appeared, while the instrumental art became sufficiently developed to be embodied in sonatas. From the beginning of the 17th century until late in the 18th, the cantata for one or two solo voices with accompaniment of basso continuo (and perhaps a few solo instruments) was a principal form of Italian vocal chamber music. A cantata consisted first of a declamatory narrative or scene in recitative, held together by a primitive aria repeated at intervals. Fine examples may be found in the church music of Giacomo Carissimi; and the English vocal solos of Henry Purcell (such as Mad Tom and Mad Bess) show the utmost that can be made of this archaic form. With the rise of the da capo aria, the cantata became a group of two or three arias joined by recitative. George Frideric Handel's numerous Italian duets and trios are examples on a rather large scale. His Latin motet Silete Venti, for soprano solo, shows the use of this form in church music."

kelimeler=s.split()
yalnız_kelimeler=list()

for i in kelimeler:
    i=i.strip("\n")
    i=i.strip(",")
    i=i.strip(".")
    i = i.strip(")")
    i = i.strip("(")
    i = i.strip("[")
    i = i.strip("]")
    i = i.strip(";")
    yalnız_kelimeler.append(i)
kelimeler2=set()
for i in yalnız_kelimeler:
    kelimeler2.add(i)
for i in kelimeler2:
    print(i)
    kelime_sozluk = dict()
    for i in yalnız_kelimeler:
        if (i in kelime_sozluk):
            kelime_sozluk[i] = kelime_sozluk[i] + 1
        else:
            kelime_sozluk[i] = 1
    for kelime, sayı in kelime_sozluk.items():
        print(" {} kelimesi {} defa geçiyor".format(kelime, sayı))