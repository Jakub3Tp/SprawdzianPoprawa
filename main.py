parzyste = 0
tylesamo = 0
iloscZer = 0
iloscJedynek = 0
koniecJeden = 0
palindromy = 0

with open('napisy.txt', 'r') as pliczek:
    for linia in pliczek:
        linia = linia.strip()
        ciag = len(linia)

    if ciag % 2 == 0:
        parzyste += 1
        print('Jest tyle parzystych napisów: ', parzyste, '\n')

    if linia.count('0') == linia.count('1'):
        tylesamo += 1
        print('Jest tyle wyrazów mających tyle samo jedynek i zer:', tylesamo, '\n')

    if ciag == linia.count('0'):
        iloscZer = 1
        print('Jest tyle wyrazów mających zera:', iloscZer, '\n')
    elif ciag == linia.count('1'):
        iloscJedynek += 1
        print('Jest tyle wyrazów mających jedynki', iloscJedynek, '\n')

    if linia.endswith('1'):
        koniecJeden += 1
        print('Jest tyle wyrazów kończączych się na jeden:', koniecJeden, '\n')

    if linia == linia[::-1]:
        palindromy += 1
        print('Jest tyle palindromów:', palindromy)
