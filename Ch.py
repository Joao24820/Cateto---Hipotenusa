import math


co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))

hi = (co**2 + ca**2)
hip = hi**(1/2)

print('O cateto oposto vale {} e o cateto adjacente vale {} sua hipotenusa vai valer {:.2f} '
      .format(co, ca, hip))
