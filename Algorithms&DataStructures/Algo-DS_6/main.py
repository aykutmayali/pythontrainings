# This is a sample Python script.

memo= {}
def f(n):
    if n<1 :
        return 0
    elif n==1 or n==2:
        return n
    elif n==3:
        return 4
    elif n not in memo.keys():
        memo[n]= f(n-3)+f(n-2)+f(n-1)
        return memo[n]
    else:
        return memo[n]

def permutasyon_al(kelime):
    if(len(kelime) == 1):
        return kelime
    else:
        sonuc =[]
        for idx in range(len(kelime)):
            harf = kelime[idx]
            kalan = kelime[:idx]+kelime[idx+1:]

            kalan_permutasyonlari= permutasyon_al(kalan)

            for permutasyon in kalan_permutasyonlari:
                sonuc.append(harf+permutasyon)

        return sonuc


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f(35))
    print(f(1))
    print(f(2))
    print(f(3))
    print(f(4))
    print(f(5))

    print(permutasyon_al('lina'))