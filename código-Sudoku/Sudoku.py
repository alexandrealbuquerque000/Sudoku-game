#Alexandre Maia Aquino de Albuquerque

from random import uniform, random, choice, sample, randint
from timeit import default_timer as timer
import time
import copy
import sys
import os
from termcolor import*
import colorama

#Função para tirar repetidos
def remove_repetidos(lista):
    l = []
    for i in lista:
        if str(i) not in l :
            l.append(str(i))
        else:
            l.append(' ')
    return l


#Funções copiadas da internet para estética:
def printsudoku(sudoku):
    print('\n')
    print(' '*4+'.'*25)
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print(' '*3, ':'+ " --------------------- "+':')
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(' '*4+':', line+':')
    print(' '*4+'.'*25)
    print()


def findNextCellToFill(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e):
    rowOk = all([e != sudoku[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != sudoku[x][j] for x in range(9)])
        if columnOk:
            secTopX, secTopY = 3*(i//3), 3*(j//3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if sudoku[x][y] == e:
                        return False
            return True
    return False


def solveSudoku(sudoku, i=0, j=0):
    i, j = findNextCellToFill(sudoku)
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
    return False


#Função para moldar matriz:
def moldmatriz():
    global quadrado
    global matriz
    global sudoku1
    global sudoku2
    global sudoku3
    matriz=[[]]
    sudoku1=[]
    sudoku2=[]
    sudoku3=[]
    for aux in range(1, quadrado+1):
        auxmatriz=str(0)
        matriz[0].append(str(auxmatriz))
        matriz[0]=copy.deepcopy(matriz[0])
        matriz=copy.deepcopy(matriz)
    auxmatriz=copy.deepcopy(matriz[0])
    for aux2 in range(quadrado-1):
        auxmatriz=copy.deepcopy(auxmatriz)
        matriz.append(list(auxmatriz))
        matriz=copy.deepcopy(matriz)
    for matrizsudoku in range(quadrado):
        matriz=copy.deepcopy(matriz)
        sudoku1.append(matriz)
        matriz=copy.deepcopy(matriz)
        sudoku2.append(matriz)
        matriz=copy.deepcopy(matriz)
        sudoku3.append(matriz)
        
    return sudoku1, sudoku2, sudoku3
        
#Função para adicionar função de remover números repetidos:
def noreplay(testematriz):
    for testerapido in range(len(testematriz)):
        testematriz[testerapido]=remove_repetidos(testematriz[testerapido])
    
    return testematriz
        
        
#Função para converter sudoku em linhas mais simples:
def convertsudokua():
    global sudoku
    global sudokuaparente
    sudokuaparente=[]
    sudokureserva=copy.deepcopy(sudoku)
    sudokureserva2=[]
    for num in range (3):
        for num2 in range (3):
            for num3 in range (3):
                sudokureserva2.extend(sudokureserva[num3][num][num2])
            sudokuaparente.append(sudokureserva2)
            sudokureserva2=[]
    for i in range(0,len(sudokuaparente)):
        for j in range(0,len(sudokuaparente[i])):
            if sudokuaparente[i][j] =='0':
                sudokuaparente[i][j] = ' '
    
    return sudokuaparente


#Função para converter sudoku em colunas mais simples:
def convertsudokub():
    global sudoku
    global sudokuaparente2
    sudokuaparente=[]
    sudokureserva=copy.deepcopy(sudoku)
    sudokureserva2=[]
    sudokuaparente2=[]
    for num in range (3):
        for num2 in range (3):
            for num3 in range (3):
                for num4 in range(3):
                    sudokureserva2.extend(sudokureserva[num][num3][num4][num2])
            sudokuaparente2.append(sudokureserva2)
            sudokureserva2=[]
    for i in range(0,len(sudokuaparente2)):
        for j in range(0,len(sudokuaparente2[i])):
            if sudokuaparente2[i][j] =='0':
                sudokuaparente2[i][j] = ' '
    
    return sudokuaparente2


#Função para converter sudoku em blocos mais simples:
def convertsudokuc():
    global sudoku
    sudokuaparente=[]
    sudokureserva=copy.deepcopy(sudoku)
    sudokureserva2=[]
    sudokuaparente3=[]
    for num in range (3):
        for num3 in range (3):
            for num4 in range(3):
                sudokureserva2.extend(sudokureserva[num3][num][num4])
            sudokuaparente3.append(sudokureserva2)
            sudokureserva2=[]
    for i in range(0,len(sudokuaparente3)):
        for j in range(0,len(sudokuaparente3[i])):
            if sudokuaparente3[i][j] =='0':
                sudokuaparente3[i][j] = ' '

    return sudokuaparente3


#Função de conversão inversa:
def invertconvertsudokua():
    global sudoku
    global sudokuaparente
    global sudokuaparente2
    global sudokureserva9
    sudokureserva5=copy.deepcopy(sudokuaparente)
    sudokureserva6=[]
    sudokureserva7=[]
    sudokureserva8=[]
    sudokureserva9=[]
    i=0
    j=3
    for montar in range(3):
        for testeinvert in range(1, 10):
            sudokureserva6.append(sudokureserva5[testeinvert-1][i: j])
            sudokureserva6=copy.deepcopy(sudokureserva6)
            if testeinvert%3==0:
                sudokureserva6=copy.deepcopy(sudokureserva6)
                sudokureserva7.append(sudokureserva6)
                sudokureserva7=copy.deepcopy(sudokureserva7)
                sudokureserva6=[]
                sudokureserva8.extend(sudokureserva7)
                sudokureserva8=copy.deepcopy(sudokureserva8)
                sudokureserva7=[]
        sudokureserva8=copy.deepcopy(sudokureserva8)
        sudokureserva9.append(sudokureserva8)
        sudokureserva9=copy.deepcopy(sudokureserva9)
        sudokureserva8=[]
        i=i+3
        j=j+3

    return (sudokureserva9)
 
 
 #Função de conversão inversa:
def invertconvertsudokub():
    global sudoku
    global sudokuaparente
    global sudokuaparente2
    global sudokureserva10
    sudokureserva5=copy.deepcopy(sudokuaparente2)
    sudokureserva6=[]
    sudokureserva7=[]
    sudokureserva8=[]
    sudokureserva10=[]
    sudokureserva11=[]
    i=0
    j=0
    for montar in range(3):
        for testeinvert in range(1, 10):
            testeinvert=testeinvert+i
            for testeinvert2 in range(1, 4):
                testeinvert2=testeinvert2+j
                sudokureserva6.extend(sudokureserva5[testeinvert2-1][testeinvert-1])
                sudokureserva6=copy.deepcopy(sudokureserva6)
            if testeinvert2%3==0:
                sudokureserva6=copy.deepcopy(sudokureserva6)
                sudokureserva7.append(sudokureserva6)
                sudokureserva7=copy.deepcopy(sudokureserva7)
                sudokureserva6=[]
            if len(sudokureserva7)%3==0:
                sudokureserva11.append(sudokureserva7)
                sudokureserva11=copy.deepcopy(sudokureserva11)
                sudokureserva7=[]
            if testeinvert==10:
                i=i+3
                sudokureserva8.extend(sudokureserva11)
                sudokureserva8=copy.deepcopy(sudokureserva8)
                sudokureserva11=[]
        sudokureserva8=copy.deepcopy(sudokureserva11)
        sudokureserva10.append(sudokureserva8)
        sudokureserva10=copy.deepcopy(sudokureserva10)
        sudokureserva6=[]
        sudokureserva7=[]
        sudokureserva8=[]
        sudokureserva11=[]
        j=j+3

    return (sudokureserva10)


#Função para printar com cor:
def sudokucomcor():
    global sudokuaparente
    global sudokucor
    convertsudokua()
    for cor in range(9):
        for cor2 in range(9):
            if sudokuaparente[cor][cor2]!= ' ' and sudokucor[cor][cor2]!=' ':
                sudokuaparente[cor][cor2]=colored(str(sudokuaparente[cor][cor2]), 'red')
                
    return sudokuaparente
                

#Segunda função para printar com cor:
def sudokucomcor2():
    global sudokuresolvido
    for cor in range(9):
        for cor2 in range(9):
            sudokuresolvido[cor][cor2]=colored(str(sudokuresolvido[cor][cor2]), 'green')
                
    return sudokuresolvido
                

#Função para ler apenas letras:
def leiastr(msg):
    while True:
        print()
        verif=str(input(msg).strip().replace(" ", ""))
        if verif.isalpha() == False:
            print()
            print("ERRO:""\nDigite apenas letras.")
            continue
        else:
            verif=verif.lower()
            return verif
        
        
#Função verificadora de números inteiros
def leiaint(msg):
    while True:
        try:
            print()
            N=int(input(msg).strip().replace(" ", ""))
        except (ValueError, TypeError, IndexError):
            print()
            print("ERRO:""\nDigite apenas números inteiros.")
            continue
        else:
            return N
    

def initshow():
        print("-"*12)
        print("   Sudoku")
        print("-"*12)


def initsudokunumbers():
    global nrepetperg
    global sudoku
    global quadrado
    global conferemagico
    global sudokupronto
    global sudokuresolvido

    if nrepetperg==0:
        sudokupronto=str("Deseja ver a resposta de um sudoku já existente ou jogar um novo? ")
        sudokupronto=leiastr(sudokupronto)
    #Obtendo a informação sobre o tamanho do quadrado
    quadrado=3
    conferemagico=[]
    sudoku1, sudoku2, sudoku3=moldmatriz()
    sudoku=[]
    sudoku1=copy.deepcopy(sudoku1)
    sudoku.append(sudoku1)
    sudoku2=copy.deepcopy(sudoku2)
    sudoku.append(sudoku2)
    sudoku3=copy.deepcopy(sudoku3)
    sudoku.append(sudoku3)
    sudoku= copy.deepcopy(sudoku)
    if 'nov' in sudokupronto:
        for aleatorio in range(3):
            for aleatorio2 in range(3):
                aleatorio5=('123456789')
                aleatorio6=('012')
                aleatorio8=choice('12345')
                for aleatorio7 in range(int(aleatorio8)):
                    while True:
                        aleatorio3=('012')
                        aleatorio6=('012')
                        a3=choice(aleatorio3)
                        a5=choice(aleatorio5)
                        a6=choice(aleatorio6)
                        sudoku[aleatorio][aleatorio2][int(a3)][int(a6)]=a5
                        aleatorio3=aleatorio3.replace(a3,"")
                        aleatorio5=aleatorio5.replace(a5,"")
                        aleatorio6=aleatorio6.replace(a6,"")
                        sudoku=noreplay(convertsudokua())
                        sudoku=invertconvertsudokua()
                        sudoku=noreplay(convertsudokub())
                        sudoku=invertconvertsudokub()
                        break
        convertsudokuc()
        sudokuresolvido=copy.deepcopy(convertsudokua())
        for resol in range(len(sudokuresolvido)):
            for resol2 in range(len(sudokuresolvido[resol])):
                if sudokuresolvido[resol][resol2] ==' ':
                    sudokuresolvido[resol][resol2] = '0'
                sudokuresolvido[resol][resol2]=int(sudokuresolvido[resol][resol2])
        solveSudoku(sudokuresolvido)
        for testeimpossivel in range(len(sudokuresolvido)):
            if any(testeimpossivel2==0 for testeimpossivel2 in sudokuresolvido[testeimpossivel]):
                os.system("cls")
                impossivel=1 
                break
            else:
                impossivel=0
        if impossivel==1:
            nrepetperg=1
            return -1
        else:
            nrepetperg=0
            pass
    else:
        pass


def configandverif():
    global sudokuresolvido

    testepos="true"
    confereverresolução=0
    while testepos=="true":
        confereverresolução=confereverresolução+1
        simbjg=str("Digite o número desejado: ")
        elemlin=str("Digite a linha desejada: ")
        elemlin=leiaint(elemlin)
        elemlin=int(elemlin)
        while elemlin==0:
            print()
            print("Esse é um quadrado 9x9.")
            print()
            print("Tente novamente")
            elemlin=str("Digite a linha desejada: ")
            elemlin=leiaint(elemlin)
            elemlin=int(elemlin)
        if elemlin<0:
            elemlin=-elemlin
        while elemlin>int(9):
            print()
            print("Esse é um quadrado 9x9.")
            print()
            print("Tente novamente")
            elemlin=str("Digite a linha desejada: ")
            elemlin=leiaint(elemlin)
        if elemlin >=1 and elemlin<=3:
            bloco=0
        elif elemlin >=4 and elemlin<=6:
            elemlin=elemlin-3
            bloco=1
        elif elemlin >=7 and elemlin<=9:
            elemlin=elemlin-6
            bloco=2
        elemcol=str("Digite a coluna desejada: ")
        elemcol=leiaint(elemcol)
        elemcol=int(elemcol)
        while elemcol==0:
            print()
            print("Esse é um quadrado 9x9.")
            print()
            print("Tente novamente")
            elemcol=str("Digite a coluna desejada: ")
            elemcol=leiaint(elemcol)
            elemcol=int(elemcol)
        if elemcol<0:
            elemcol=-elemcol
        while elemcol>int(9):
            print()
            print("Esse é um quadrado 9x9.")
            print()
            print("Tente novamente")
            elemcol=str("Digite a coluna desejada: ")
            elemcol=leiaint(elemcol)
        if elemcol >=1 and elemcol<=3:
            colunagrande=0
        elif elemcol >=4 and elemcol<=6:
            elemcol=elemcol-3
            colunagrande=1
        elif elemcol >=7 and elemcol<=9:
            elemcol=elemcol-6
            colunagrande=2
        if 'nov' in sudokupronto:
            if sudokuparametro[colunagrande][bloco][elemlin-1][elemcol-1]!=' ':
                print()
                print("Esse número não pode ser alterado.")
                continue
            else:
                pass
        else:
            pass
        simbjg=leiaint(simbjg)
        while simbjg<0 or simbjg>9:
            print()
            print("Por favor, digite apenas números naturais entre 0 e 10.")
            simbjg=str("Digite o número desejado: ")
            simbjg=leiaint(simbjg)
        sudoku[colunagrande][bloco][elemlin-1][elemcol-1]=str(simbjg)
        os.system("cls")
        printsudoku(sudokucomcor())
#Analizando a soma dos elementos das linhas
        conferenumreptest=[]
        conferenumrep=[]
        conferenumreplin=[]
        conferenumrepcol=[]
        for colunagrande in range(3):
            for bloco in range(3):          
                matriz=copy.deepcopy(sudoku[colunagrande])
                matriz=copy.deepcopy(matriz[bloco])
                magicototal=0
                conferenumiguais=[]
                for num in range(quadrado):
                    for num2 in range(quadrado):
                        conferenumrep.append(matriz[num][num2])
                        try:
                            magico=int(matriz[num][num2])
                        except (ValueError):
                            magico=0
                        conferenumiguais.append(magico)
                        magicototal=int(magicototal)+magico
                    conferemagico.append(magicototal)
                    magicototal=0
                teste=-1
                while teste <7:
                    for mg in (conferenumiguais):
                        teste=teste+1
                        testenumrepetido=0
                        for aux2 in range(9):
                            if mg == conferenumiguais[aux2] and mg!=0:
                                testenumrepetido=testenumrepetido+1
                            if testenumrepetido>1:
                                print()
                                print(colored(str(f"O bloco {bloco+1}x{colunagrande+1} possui números repetidos."), 'yellow'))
                                break
                        if testenumrepetido>1:
                            break
                    if testenumrepetido>1:
                        break
        j=-3
        j2=0
        for numtest in range(27):
            j=j+3
            j2=j2+3
            conferenumreptest.append(conferenumrep[j: j2 ])
        copiar=[]
        for num in range(3):
            for num2 in range(9):
                conferenumrepcol.extend(conferenumreptest[num2][num])
            copiar.append(copy.deepcopy(conferenumrepcol))
            conferenumrepcol=[]
        for num in range(3):
            for num2 in range(9, 18):
                conferenumrepcol.extend(conferenumreptest[num2][num])
            copiar.append(copy.deepcopy(conferenumrepcol))
            conferenumrepcol=[]
        for num in range(3):
            for num2 in range(18, 27):
                conferenumrepcol.extend(conferenumreptest[num2][num])
            copiar.append(copy.deepcopy(conferenumrepcol))
            conferenumrepcol=[]
        conferenumrepcol=copy.deepcopy(copiar)
        copiar=[]
        for num in range(9):
            for num2 in range(9):
                conferenumreplin.extend(conferenumrepcol[num2][num])
            copiar.append(copy.deepcopy(conferenumreplin))
            conferenumreplin=[]
        conferenumreplin=copy.deepcopy(copiar)
        copiar=[]   
        testenumrepetido=2
        teste=3
        while teste <11:
            for num in range(9):
                for mg in (conferenumrepcol[num]):
                    testenumrepetido=0
                    for aux2 in range(9):
                        teste=teste+1
                        try:
                            int(conferenumrepcol[num][aux2])
                        except(ValueError):
                            conferenumrepcol[num][aux2]=str(0)
                        try:
                            int(mg)
                        except(ValueError):
                            mg=0
                        if int(mg) == int(conferenumrepcol[num][aux2]) and int(mg)!=0:
                            testenumrepetido=testenumrepetido+1
                        if testenumrepetido>1:
                            print()
                            print(colored(str(f"A coluna {num+1} possui números repetidos."), 'yellow'))
                            break
                    if testenumrepetido>1:
                        break
        testenumrepetido=2
        teste=3
        while teste <11:
            for num in range(9):
                for mg in (conferenumreplin[num]):
                    testenumrepetido=0
                    for aux2 in range(9):
                        teste=teste+1
                        try:
                            int(conferenumreplin[num][aux2])
                        except(ValueError):
                            conferenumreplin[num][aux2]=str(0)
                        try:
                            int(mg)
                        except(ValueError):
                            mg=0
                        if int(mg) == int(conferenumreplin[num][aux2]) and int(mg)!=0:
                            testenumrepetido=testenumrepetido+1
                        if testenumrepetido>1:
                            print()
                            print(colored(str(f"A linha {num+1} possui números repetidos."), 'yellow'))
                            break
                    if testenumrepetido>1:
                        break
        copyconfere1=(convertsudokua())
        copyconfere2=(convertsudokub())
        copyconfere3=(convertsudokuc())
        if 'nov' in sudokupronto:
            WIN=0
            for vitoria in range(9):
                if all(vit!=' ' for vit in (copyconfere1[vitoria])) and all(vit2!=' ' for vit2 in (copyconfere2[vitoria])) and all(vit3!=' 'for vit3 in (copyconfere3[vitoria])) and (copyconfere1==noreplay(convertsudokua())) and (copyconfere2==noreplay(convertsudokub())):
                    WIN=WIN+1
            if WIN==9:
                end = timer()
                print()
                print("Parabéns!!!")
                print()
                print("Você conseguiu terminar o jogo em {:.2f} minutos.".format((float((end - start)/60))))
                reiniciar=str("Deseja reiniciar o programa? ")
                reiniciar=leiastr(reiniciar)
                if 's' in reiniciar:
                    os.system("cls")
                    return -1
                else:
                    input()
                    sys.exit()
            if confereverresolução%65==0:
                verresolução=str("Deseja ver a resolução? ")
                verresolução=leiastr(verresolução)
                if 's' in verresolução:
                    print()
                    printsudoku(sudokuresolvido)
                    input("Pressione 'Enter' para continuar.")
        else:
            addmaisnum=str("Deseja resolver o sudoku no estado atual ou precisa adicionar mais elementos? ")
            addmaisnum=leiastr(addmaisnum)
            if 'ad' in addmaisnum:
                continue
            else:
                for vitoria in range(9):
                    if  (copyconfere3!=noreplay(convertsudokuc())) or (copyconfere1!=noreplay(convertsudokua())) or (copyconfere2!=noreplay(convertsudokub())):
                        print()
                        print("Erro")
                        print()
                        print("Verifique os números desse sudoku.")
                        veriferro=1
                        break
                    else:
                        veriferro=0
                        break
            if veriferro==1:
                continue
            else:
                pass
            sudokuresolvido=copy.deepcopy(convertsudokua())
            for resol in range(len(sudokuresolvido)):
                for resol2 in range(len(sudokuresolvido[resol])):
                    if sudokuresolvido[resol][resol2] ==' ':
                        sudokuresolvido[resol][resol2] = '0'
                    sudokuresolvido[resol][resol2]=int(sudokuresolvido[resol][resol2])
            solveSudoku(sudokuresolvido)
            for testeimpossivel in range(len(sudokuresolvido)):
                if any(testeimpossivel2==0 for testeimpossivel2 in sudokuresolvido[testeimpossivel]):
                    print()
                    print("Esse sudoku não tem solução.")
                    break
                else:
                    print()
                    print("Essa é a resolução:")
                    printsudoku(sudokuresolvido)
                    break
            reiniciar=str("Deseja reiniciar o programa? ")
            reiniciar=leiastr(reiniciar)
            if 's' in reiniciar:
                os.system("cls")
                return -1
            else:
                input()
                sys.exit()


def run():
    global nrepetperg, sudokucor, sudokuparametro

    os.system('color')
    
    nrepetperg=0     
    reiniciar="s"
    while "s" in reiniciar:
        initshow()
        if initsudokunumbers()==-1:
            continue
        if 'nov' in sudoku:
            sudokucomcor2()
        sudokucor=copy.deepcopy(convertsudokua())
        #Mostrando a matriz formada
        printsudoku(sudokucomcor())
        start = timer()
        sudokuparametro=copy.deepcopy(sudoku)
        if configandverif()==-1:
            continue

                
run()            
        
