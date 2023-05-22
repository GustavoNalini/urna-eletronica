prefeito = [
    # nome, numero, partido, votos
    ["Marcelo", 20, "P2", 19],
    ["Grazi", 30, "P3", 19],
    ["Andre", 10, "P1", 20]
]

# ordenar por quem recebeu mais votos. voto esta na
# posicao 3 da minha lista
prefeito.sort(reverse=True, key= lambda x : x[3])

def imprime_tabela(lista, cargo, totalVotos=58, v1=200) :
    print(f'{"":-^80}')
    print('|'+f'{"RANKING DO RESULTADO PARA "+cargo:^78}'+'|')
    print(f'{"":-^80}')
    print('|'+f'{"Candidato":^32}'+
          '|'+f'{"Partido":^10}'+
          '|'+f'{"Total de votos":^16}'+
          '|'+f'{"% votos validos":^17}'+'|')
    print(f'{"":-^80}')

    for i in range(len(lista)) :
        votosPorcentagem = f'{100*lista[i][3]/totalVotos:.1f}'+'%'
        print('|' + f'{i+1:02}. '
              + f'{lista[i][0]:<28}' + '|'
              + f'{lista[i][2]:^10}' + '|'
              + f'{lista[i][3]:^16}' + '|'
              + f'{votosPorcentagem:^17}' + '|'

              )

    print(f'{"":-^80}')
    print('|'+f'{"Total de votos = "+str(v1):<78}'+'|')
    print('|'+f'{"Total de votos válidos e % = "+str(v1):<78}'+'|')
    print('|'+f'{"Total de brancos e % = "+str(v1):<78}'+'|')
    print('|'+f'{"Total de nulos e % = "+str(v1):<78}'+'|')
    print(f'{"":-^80}')

imprime_tabela(prefeito, "PRESIDENTE")
imprime_tabela(prefeito, "GOVERNADOR")
imprime_tabela(prefeito, "prefeITO")