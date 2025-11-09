# ALUNOS: GABRIEL DE CAMPOS GONSALVES e RUAN SARTÓRIO THOMAZ

import math

#============================
def o_que_eh_trigonometria():
    print("================================= EXPLICAÇÃO ==================================\n")
    print("A trigonometria é a parte da matemática que estuda as relações")
    print("existentes entre os lados e os ângulos dos triângulos.\n")
    print("Ela usa funções chamadas seno (sen), cosseno (cos) e tangente (tan)")
    print("para relacionar essas medidas.\n")
    print("A trigonometria é muito usada em geometria, física, engenharia, arquitetura e")
    print("em qualquer situação que envolva medir distâncias ou ângulos, como calcular a")
    print("altura de um prédio ou a distância entre dois pontos.\n")
    print("================================================================================")

#============================
def angulos_notaveis():
    print("================== ÂNGULOS NOTÁVEIS ===================\n")
    print("\t30°\t45°\t60°")
    print("SEN\t1/2\t√2/2\t√3/2")
    print("COS\t√3/2\t√2/2\t1/2")
    print("TAN\t√3/3\t1\t√3")
    print("\n=======================================================\n")

#============================
def relacao_trigonometrica():
    print("============================ RAZÕES TRIGONOMÉTRICAS =============================\n")
    print("               /|")
    print("              / |")
    print("             /  |  ← Cateto Oposto")
    print("            /   |")
    print("           /    |")
    print("          /     |")
    print("         /______|")
    print("   ↑")
    print("   |  Hipotenusa")
    print("   →  Cateto Adjacente\n\n")

    print("SENO = Cateto Oposto / Hipotenusa\n")
    print("COSSENO = Cateto Adjacente / Hipotenusa")
    print("\nTANGENTE = Cateto Oposto / Cateto Adjacente")
    print("\n=================================================================================\n")

#============================
def triangulo_retangulo():
    print("============================================= EXPLICAÇÃO ==============================================\n")
    print("Um triângulo retângulo é um triângulo que possui um dos seus ângulos iguais a 90° (reto).")
    print("O lado oposto ao ângulo reto é chamado de hipotenusa, e os outros dois lados são chamados")
    print("de cateto oposto e cateto adjacente, dependendo da posição em relação ao ângulo analisado.\n")

    print("        ________ Cateto Oposto")
    print("       |\\")
    print("       | \\")
    print("       |  \\")
    print("       |   \\  Hipotenusa")
    print("       |    \\")
    print("       |_____\\")
    print("   Cateto Adjacente")
    print("=======================================================================================================")

#============================

def calcular_cateto_oposto(angulo_graus, hipotenusa):
    angulo_radianos = math.radians(angulo_graus)
    return math.sin(angulo_radianos) * hipotenusa
#----
def calcular_cateto_adjacente(angulo_graus, hipotenusa):
    angulo_radianos = math.radians(angulo_graus)
    return math.cos(angulo_radianos) * hipotenusa
#----
def calcular_hipotenusa_por_seno(angulo_graus, cateto_oposto):
    angulo_radianos = math.radians(angulo_graus)
    return cateto_oposto / math.sin(angulo_radianos)
#----
def calcular_hipotenusa_por_cosseno(angulo_graus, cateto_adjacente):
    angulo_radianos = math.radians(angulo_graus)
    return cateto_adjacente / math.cos(angulo_radianos)

#============================
def calculo_trigonometrico():
    while True:
        print("\n===== CÁLCULO DE TRIÂNGULO RETÂNGULO =====")
        print("1 - Calcular cateto oposto")
        print("2 - Calcular cateto adjacente")
        print("3 - Calcular hipotenusa (usando cateto oposto)")
        print("4 - Calcular hipotenusa (usando cateto adjacente)")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if (opcao == "0"):
            print("\n==========================================================================")
            break

        if (opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4"):
            angulo = float(input("Digite o ângulo (em graus): "))

            if (opcao == "1"):
                hipotenusa = float(input("Digite o valor da hipotenusa: "))
                resultado = calcular_cateto_oposto(angulo, hipotenusa)
                print(f"\n-> Cateto oposto = {resultado:.2f}")

            elif (opcao == "2"):
                hipotenusa = float(input("Digite o valor da hipotenusa: "))
                resultado = calcular_cateto_adjacente(angulo, hipotenusa)
                print(f"\n-> Cateto adjacente = {resultado:.2f}")

            elif (opcao == "3"):
                cat_oposto = float(input("Digite o valor do cateto oposto: "))
                resultado = calcular_hipotenusa_por_seno(angulo, cat_oposto)
                print(f"\n-> Hipotenusa = {resultado:.2f}")

            elif (opcao == "4"):
                cat_adj = float(input("Digite o valor do cateto adjacente: "))
                resultado = calcular_hipotenusa_por_cosseno(angulo, cat_adj)
                print(f"\n-> Hipotenusa = {resultado:.2f}")

        else:
            print("\n=== Opção inválida. Tente novamente! ===")

#============================
def o_que_eh_circulo_trig():
    print("============================================= EXPLICAÇÃO ==============================================\n")
    
    print("""
Um círculo trigonométrico é uma circunferência com raio igual a 1 unidade,
centrada na origem de um plano cartesiano, usada para representar ângulos
e estudar as funções trigonométricas, como seno e cosseno.

Ele é dividido em quatro quadrantes, e o sentido positivo da rotação é
o anti-horário. O eixo x representa os cossenos e o eixo y representa os senos.

---->  Características principais:
  • Raio: 1 unidade
  • Centro: Na origem (0,0) do plano cartesiano
  • Sentido positivo: Anti-horário
  • Eixos: x → cossenos | y → senos
  • Quadrantes: 4 partes (I, II, III, IV)
  • Volta completa: 360° ou 2π rad -> π = 180°
  • Medida de ângulos: a partir do eixo x positivo, no sentido anti-horário

---->  Funções trigonométricas:
  • Coordenada x do ponto → cosseno(θ)
  • Coordenada y do ponto → seno(θ)
""")
    print("=======================================================================================================")

#============================
def conversao_unidade():
    print("========== TIPO DE CONVERSÃO ==========")
    print("\n\t1. de radianos para graus.")
    print("\t2. de graus para radianos.")

    conversao = int(input("\nDigite o tipo de conversão: "))

    if (conversao == 1):
        print("\n======== ATENÇÃO SIGA OS EXEMPLOS ABAIXO: ========")
        print("π = 180°, logo para 7π/4 radianos -> digite 7 em RADIANOS e 4 no DIVISOR;")
        print("Para 2π -> digite 2 em RADIANOS e 1 no DIVISOR;")
        print("Para π -> digite 1 em RADIANOS e 1 no DIVISOR;\n")

        rad = int(input("Digite o valor do ângulo em RADIANOS: "))
        div = int(input("Digite o valor do DIVISOR: "))

        em_graus = (rad*180 / div) * (180 / 180)

        if (div == 1):
            print("\n--> {}π para graus = {}°".format(rad, em_graus))
        else:
            print("\n--> {}π/{} para graus = {}°".format (rad, div, em_graus))

    elif (conversao == 2):
        grau = int(input("\nDigite o valor do ângulo em graus: "))

        mdc = math.gcd(grau, 180)
        num = grau // mdc
        den = 180 // mdc

        print(f"\n--> O ângulo simplificado = {num}π/{den} radianos.")        

    print("\n==========================================================================")

#============================
def reduz_quadrante():
    print("======================== REDUÇÃO DE QUADRANTE ============================\n")
    grau = float(input("Digite o ângulo em graus: "))

    grau = grau % 360

    if 0 <= grau <= 90:
        angulo_ref = grau
        quadrante = 1
    elif 90 < grau <= 180:
        angulo_ref = 180 - grau
        quadrante = 2
    elif 180 < grau <= 270:
        angulo_ref = grau - 180
        quadrante = 3
    else:
        angulo_ref = 360 - grau
        quadrante = 4

    print("\n--- Resultado ---")
    print(f"Ângulo reduzido: {grau:.2f}°")
    print(f"Quadrante: {quadrante}º")
    print(f"Ângulo de referência (1º quadrante): {angulo_ref:.2f}°")
    print("\n==========================================================================\n")

#============================
def main():
    print("\n===== Seja bem-vindo(a) ao PyElementar o algoritmo criado para ajudar no estudo da Trigonometria!!! =====\n")

    n = 1

    while n != 0:
        print("\n\t~~~~~ Menu de opções ~~~~~")
        print("\t1. O que é a Trigonometria?")
        print("\t2. Imprimir a tabela dos ângulos notáveis.")
        print("\t3. Imprimir as razões trigonométricas.")
        print("\t4. O que é um triângulo retângulo?")
        print("\t5. Calcular o lado de um triângulo retângulo.")
        print("\t6. O que é o circulo trigonométrico?")
        print("\t7. Conversão de unidades (radianos e graus).")
        print("\t8. Reduzir o ângulo para o 1° Quadrante do circulo trigonométrico.")
        print("\t0. Sair.\n")

        n = int(input("Digite o número da opção: "))
        print()

        if (n == 1):
            o_que_eh_trigonometria()

        elif (n == 2):
            angulos_notaveis()

        elif (n == 3):
            relacao_trigonometrica()

        elif (n == 4):
            triangulo_retangulo()

        elif (n == 5):
            calculo_trigonometrico()

        elif (n == 6):
            o_que_eh_circulo_trig()

        elif (n == 7):
            conversao_unidade()
        
        elif (n == 8):
            reduz_quadrante()
        
        elif (n == 0):
            print("SAINDO DO PROGRAMA...")
            print("============== Produced by Gabriel de Campos and Ruan Sartório ================")
            break

        else:
            print("======= Opção inexistente! =======")

#============================
main()
