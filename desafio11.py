print('{} DESAFIO 11 {}'.format('='*10, '='*10))
larg = float(input('Informe a largura da parede (em metros): '))
alt = float(input('Informe a altura da parede (em metros): '))
area = larg * alt
tinta = area/2
print('Sta parede tem {}m² e são necessários {}L de tinta para pintá-la!'.format(area, tinta))
