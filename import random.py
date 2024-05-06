import random

slova = []
with open("jmn.txt", encoding="utf-8") as f:
    slova = f.read().split()

def vyber_slovo():
    return random.choice(slova)

def inicializace_hry():
    slovo = vyber_slovo()
    hadane_pismeno = []
    for pismeno in slovo:
        if pismeno.isalpha():
            hadane_pismeno.append('_')
        else:
            hadane_pismeno.append(pismeno)
    return slovo, hadane_pismeno



def vykresli_sibenici(pokus):
    obrazek = [
        '  ________',
        '  |     | ',
        '  |     ' + ('O' if pokus > 0 else ''),
        '  |    ' + ('/|\\' if pokus > 2 else ('/' if pokus > 1 else '')),
        '  |    ' + ('/ \\' if pokus > 4 else ('/' if pokus > 3 else '')),
        '__|__'
    ]
    for line in obrazek:
        print(line)

def vypis_stav_hry(slovo, hadane_pismeno, spatna_pismena):
    print('Slovo:', ' '.join(hadane_pismeno))
    print('Špatně hádaná písmena:', ' '.join(spatna_pismena))
    vykresli_sibenici(len(spatna_pismena))


def nacti_hadane_pismeno():
    while True:
        hadani = input('Zadejte písmeno: ').lower()
        if len(hadani) == 1 and hadani.isalpha():
            return hadani
        else:
            print('Prosím, zadejte jedno platné písmeno.')


def zacni_hru():
    print('Vítejte na sibenici zlobišáci!')
    slovo, hadane_pismeno = inicializace_hry()
    spatna_pismena = []
    vykresli_sibenici(0)
    while True:
        vypis_stav_hry(slovo, hadane_pismeno, spatna_pismena)
        hadani = nacti_hadane_pismeno()
        if hadani in slovo:
            for i, pismeno in enumerate(slovo):
                if pismeno == hadani:
                    hadane_pismeno[i] = hadani
            if '_' not in hadane_pismeno:
                print('Gratulujeme, uhodli jste slovo:', slovo)
                break
        else:
            spatna_pismena.append(hadani)
            if len(spatna_pismena) == 6:
                vypis_stav_hry(slovo, hadane_pismeno, spatna_pismena)
                print('Bohužel, prohráli jste! Hledané slovo bylo:', slovo)
                break


if __name__ == '__main__':
    zacni_hru()
