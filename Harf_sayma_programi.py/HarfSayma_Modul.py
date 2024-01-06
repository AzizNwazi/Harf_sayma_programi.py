

def harf_sayilari(metin):

    harf_sayisi = {} # harflerin sayisini tutmak için 

    for harf in metin:
        if harf.isalpha(): # metindeki geçen harf olduğu sürece çalışsın
 
            harf = harf.lower() # büyük - küçük harfi eşitlesin

            if harf in harf_sayisi: # eğer harf yeniyse( ilk kes görüldüyse ) dizide tut
                harf_sayisi[harf] += 1
            else: 
                # daha önce geçtiğiyse bir şey yapma sabit tut 
                harf_sayisi[harf] = 1
    
    return harf_sayisi # son olarak harf sayisi dizisinde tutuğumuz harflerin sayısını maine döndur 