"""
Código baseado no algorítmo "doomsday" onde encontra o dia da semana baseado na data colocada pelo usuário.

"""

#Início do código

def main():

    #Entrada do usuário.
    dia=input("Escreva aqui o dia do mês (exemplo: 1, 2, 3...): ")
    mes=input("Escreva aqui o mês (exemplo: janeiro -> 1 ; dezembro -> 12... ): ")
    ano=input("Escreva aqui o ano: ")

    #Lista contendo as datas correspondentes a cada dia.
    listadiareferencia=[3,28,14,4,9,6,11,8,5,10,7,12]
        #Correspondente respectivamente: 1-jan, 2-fev...

    #Alteração para código bissexto.
    if int(ano)%4==0 and int(ano)%100!=0:
        listadiareferencia[0]=4
        listadiareferencia[1]=29

    if int(ano)%4==0 and int(ano)%100==0 and int(ano)%400==0:
        listadiareferencia[0]=4
        listadiareferencia[1]=29

    #Código A:
    a=int(dia)-int(listadiareferencia[int(mes)-1])

    #Código B
    r=int(ano)
    while (r-400)>=0:
        r=r-400

    if 0<=r<100:
        b=3
    elif 100<=r<200:
        b=1
    elif 200<=r<300:
        b=6
    elif 300<=r<400:
        b=4

    #Código C
    m=int( int(ano)-((int(ano)//100)*100) )

        #Lista com os múltiplos de 12.
    listamultiplos=[12,24,36,48,60,72,84,96,108]

    for x in listamultiplos:
        if (m/x)<1:
            c=int(((x-12)/12))
            listamultiplos.append(x-12)
            break

    #Código D
    d=((m)-(int(listamultiplos[-1])))

    #Código E
    e=int(d//4)

    #Somatório geral.
    semana=(a+b+c+d+e)%7

    if semana==1:
        resultado=("domingo")
    elif semana==2:
        resultado=("segunda-feira")
    elif semana==3:
        resultado=("terça-feira")
    elif semana==4:
        resultado=("quarta-feira")
    elif semana==5:
        resultado=("quinta-feira")
    elif semana==6:
        resultado=("sexta-feira")
    elif semana==0:
        resultado=("sábado")
    else:
        resultado=("erro")

    print("Seus códigos Doomsday são: {}, {}, {}, {}, {}, {}".format(a,b,c,d,e,semana))

    print("O dia da semana correspondente a essa data é ---> {}".format(resultado))

main()