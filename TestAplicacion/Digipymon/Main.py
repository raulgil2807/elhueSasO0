
## Hemos importado todas las clases de  nuestro Videojuego
import random
# Este import se utiliza para wue el texto que se muestre tenga una duración
import time
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from ListaNombres import ListaNombres
from Digipymon import Digipymon 


def main():
    print("")
    print("Bienvenido a Digipymon!! Podrás hacerte con todos?!")
    time.sleep(0.5)
    print("")
    nombre_jugador = str(input("¿Cúal es tu nombre ser de Luz? "))
    print("")
    print(f"Bienvenido {nombre_jugador}!!") 
    print("")
    jugador1 = Jugador(nombre_jugador)
    inventario1 = Inventario()
    inventario1.añadir_objeto("Digipyball",3)
    bucle = True
    while bucle:
        print("")
        opcion_menu = menu()
        if opcion_menu == 7:
            print("¡Hasta luego!")
            bucle = False
        elif opcion_menu == 1:
            
            digipymon1 = buscar_digipymon(jugador1,inventario1)  
            probabilidad = 100 - (digipymon1.nivel * 10)
            print("La probabilidad de captura de este" , str(digipymon1.nombre) ,"es :", str(probabilidad),"%")
            print("")
            captura = str(input("Quieres intentar capturarlo? (y/n): "))
            print("")
            cuantas_digipyballs = inventario1.objetos.get("Digipyball")
            if captura == "y" or captura == "Y":
                if cuantas_digipyballs > 0 and jugador1.cantidad_digipymon < 6:
                    bucle1 = True
                    while bucle1:
                        cuantas_digipyballs = inventario1.objetos.get("Digipyball")
                        aleatorio = random.randint(1, 100)
                        inventario1.usar_objeto("Digipyball")
                        if aleatorio > 0 and aleatorio <= probabilidad :
                            jugador1.añadir_digipymon(digipymon1)
                            print("")
                            print("Enhorabuena, has capturado este ",str(digipymon1.nombre))  
                            print("")
                            bucle1 = False
                        else:
                            print("No has podido capturar este digipymon")
                            print("")
                            if cuantas_digipyballs > 0:
                                pregunta1 = str(input("Quieres volver a intentarlo? (y/n)"))
                                if pregunta1 == "n" or pregunta1 == "N" or cuantas_digipyballs <= 0:
                                    bucle1 = False
                            else: 
                                print("¡Ya no tienes digipyballs!")
                                bucle1 = False
                            
                        
                elif cuantas_digipyballs == 0:
                    print("!!!No tienes suficientes digipyballs¡¡¡")
                    print("")
                elif jugador1.cantidad_digipymon == 6:
                    print("No tienes suficiente espacio para guardar otro digipymon")
            elif captura == "n" or captura == "N":
                print("Has huido con éxito")
            else:
                print("Opción inválida. Intente de nuevo.")
        elif opcion_menu == 2:
            combate(jugador1)
        elif opcion_menu == 6:
            consultar_digipymons(jugador1)
        elif opcion_menu == 3:
            digishop_completo(jugador1,inventario1)
        elif opcion_menu == 5:
            inventario1.mostrar_objetos()
        elif opcion_menu == 4:
            inventario1.mostrar_objetos()
            opcion_usar = str(input("¿Qué objeto del inventario deseas usar? Anabolizante (A|P) Pociones: "))
            print("")
            if opcion_usar == "A" or opcion_usar == "a":
                consultar_digipymons(jugador1)
                cualquiere = int(input("A que número de digipymon quieres chetar: "))
                digipymon_elegido = jugador1.lista_digipymon[cualquiere-1]
                print("")
                print("Inyectando esteroides a "+ str(digipymon_elegido.nombre))
                time.sleep(3)
                print("")
                print("WUAOOU ESO HA SENTADO GENIAL!!")
                time.sleep(2)
                print("")
                inventario1.usar_objeto("Anabolizantes")
                digipymon_elegido.ataque += 5
                print("Sus nuevas estadísticas son: ")
                print("")
                print(digipymon_elegido)

                ############################ VAMOS POR AQUI BUSCANSO UN SET
                
                ###jugador1.digipymon_elegido.
                
                
            elif opcion_usar == "P" or opcion_usar == "p":
                consultar_digipymons(jugador1)
                cualquiere2 = int(input("A que número de digipymon quieres chetar: "))
                print("")
                digipymon_elegido = jugador1.lista_digipymon[cualquiere2-1]
                print("Bebiendo poción repugnante")
                time.sleep(3)
                print("")
                print("SIENTE EL PODER DE LA CURACIÓN! ¡TU VITALIDAD HA SIDO RESTAURADA. ¡ADELANTE, HÉROE, TU CAMINO SIGUE BRILLANDO!")
                time.sleep(2)
                print("")
                inventario1.usar_objeto("Poción Curativa")
                print("")
                digipymon_elegido.vida += 10
                print("Sus nuevas estadísticas son: ")
                print("")
                print(digipymon_elegido)
def generar_digipymon_aleatorio():
    vida = random.randint(10, 20)
    ataque = random.randint(1,10)
    nivel = random.randint(1,3)
    tipos = ["Fuego", "Agua", "Planta"]
    tipo = random.choice(tipos)
    lista = ListaNombres()
    nombre = lista.obtener_nombres_digipymon()
    digipymon = Digipymon(nombre, vida, ataque,tipo, nivel)
    return digipymon

def menu():
    print("** Digipymon:                  ****")
    time.sleep(0.15)
    print("1. Buscar digipymon            ****")
    time.sleep(0.15)
    print("2. Luchar contra un entrenador ****")
    time.sleep(0.15)
    print("3. Ir a la tienda              ****")
    time.sleep(0.15)
    print("4. Usar objetos                ****")
    time.sleep(0.15)
    print("5. Consultar inventario        ****")
    time.sleep(0.15)
    print("6. Consultar digipymons        ****")
    time.sleep(0.15)
    print("7. Salir")
    time.sleep(0.15)
    print("")
    opcion = int(input("Ingrese una opcion: "))
    print("")
    return opcion

def buscar_digipymon(Jugador,Inventario):
    
    #Estaría bacano agregar zonas distintas donde buscar digipymons.
    #Sitios que aparezcan más de fuego, otra que aparezcan más de planta etc.
    #Estaría guay tambien agregar zonas donde salgan digipymons más fuertes e incluso digipymons evolucionados muy 
    #dificiles de capturar.
    #Hay que agregar tambien lo que viene siendo lo de las evoluciones.

    digipymon1 = generar_digipymon_aleatorio()
    print(digipymon1)
   
    return digipymon1
    
def combate(jugador1):
    lista1 = ListaNombres()
    nombre = lista1.obtener_nombre_entrenadores()
    
    enemigo1 = Enemigo(nombre)
    for i in range(jugador1.cantidad_digipymon):
        digipymon_enemigo = generar_digipymon_aleatorio()
        enemigo1.añadir_digipymon(digipymon_enemigo)
        
    bucle2 = True
    while bucle2:
        opcion_combate = str(input(f"¿ Quieres enfrentarte a {nombre}? (y/n): ")) 
        if opcion_combate == "y" or opcion_combate == "Y":
            if jugador1.cantidad_digipymon != 0:
                print("¡Comienza el combate!")
                time.sleep(2)
                print("")
                contador_win = 0
                contador_lose = 0
                for i in range(min(len(jugador1.lista_digipymon), len(enemigo1.lista_digipymon))):
                    print(f"Turno {i+1}:")
                    mi_digipymon = jugador1.lista_digipymon[i]
                    enemigo_digipymon = enemigo1.lista_digipymon[i]

                    print(f"Tu {mi_digipymon.nombre} se enfrenta al {enemigo_digipymon.nombre} del enemigo.")
                    print(f"Tu {mi_digipymon.nombre} tiene {mi_digipymon.ataque} de ataque.")
                    print(f"El {enemigo_digipymon.nombre} del enemigo tiene {enemigo_digipymon.ataque} de ataque.")

                    if mi_digipymon.ataque > enemigo_digipymon.ataque and mi_digipymon.vida != 0 :
                        print("¡Ganas el combate!")
                        print("")
                       
                        mi_digipymon.vida -= enemigo_digipymon.ataque
                        if mi_digipymon.vida < 0 :  
                            mi_digipymon.vida = 0
                        contador_win += 1
                        print(f"Tu {mi_digipymon.nombre} ha ganado, pero pierde {enemigo_digipymon.ataque} de vida.")
                        print("")
                    elif mi_digipymon.ataque < enemigo_digipymon.ataque or mi_digipymon.vida <= 0:
                        if mi_digipymon.vida <= 0:
                            print("¡Pierdes el combate! Tu digipymon está reventao pare")
                            contador_lose += 1
                        else:
                            print("¡Pierdes el combate!")
                            print("")
                            
                            mi_digipymon.vida -= enemigo_digipymon.ataque
                            if mi_digipymon.vida < 0 :  
                                mi_digipymon.vida = 0
                            contador_lose += 1
                        
                        print(f"Tu {mi_digipymon.nombre} ha perdido, y pierde {enemigo_digipymon.ataque} de vida.")
                        
                    elif mi_digipymon.ataque == enemigo_digipymon.ataque:
                        print(f"¡Es un empate! Tu {mi_digipymon.nombre} no pierde vida")
                    
                    print("------")
                    print("Fin del combate.")
                    time.sleep(2)
                    print("")
                if contador_win > contador_lose :
                    print("Tu recuento de victorias es favorable!! Enhorabuena ganaste el primer puesto hoy.")
                    print("")
                    jugador1.digicoins += contador_win * 5
                    print(f"Tu oro ha aumentado a : {jugador1.digicoins} oros")
                    bucle2 = False
                    
                elif contador_win < contador_lose :
                    print("Hoy ha sido un mal día, vuelve a intentarlo pronto!")
                    print("")
                    jugador1.digicoins -= contador_lose
                    
                    if jugador1.digicoins < 0:
                        jugador1.digicoins = 0
                    print(f"Tu oro ha descendido a : {jugador1.digicoins} oros")
                    bucle2 = False
                else:
                    print("¡Es un empate!")
                    bucle2 = False
                    jugador1.digicoins += contador_win 
                    print(f"Tu oro ha aumentado a: {jugador1.digicoins} oros")
            else: 
                print("No tienes digipymons")
                bucle2 = False
        elif opcion_combate == "n"  or opcion_combate == "N":
            print("Nos quedamos con uno de oro por tu cobardía")
            jugador1.digicoins -= 1
            bucle2 = False
            
def digishop(jugador1):
    print("MOSTRANDO DIGISHOP...")
    time.sleep(0.3)
    print(f"                                                               ****  ORO: {jugador1.digicoins}")
    print("     TIENDA DIGISHOP:                                          ****")
    print("  1. Digipyball: 5 digicoins                                   ****")
    print("  2. Poción: 3 digicoins (restaura 10p de vida)                ****")
    print("  3. Anabolizantes: 4 digicoins (aumenta 5p de ataque)         ****")
    print("  4. Salir")
    print("")
    opcion_tienda = int(input("Ingrese una opcion: "))
    print("")
    return opcion_tienda
    
def consultar_digipymons(jugador1):
    for i in range(len(jugador1.lista_digipymon)):
        print(f"Digipymon numero {i+1}:")
        print("")
        mi_digipymon = jugador1.lista_digipymon[i]
        print(str(mi_digipymon))
        print("")

def digishop_completo(jugador1,inventario1):
    
    bucle3 = True
    while bucle3:
        opcion_tienda = digishop(jugador1)
        if opcion_tienda == 1:
            if jugador1.digicoins >= 5:
                print("Has comprado una Digipyball")
                print("")
                jugador1.digicoins -= 5
                inventario1.añadir_objeto("Digipyball",1)
            else:
                print("No tienes suficientes digicoins")
                bucle3 = False
        elif opcion_tienda == 2:
            if jugador1.digicoins >= 3:
                print("Has comprado una poción Curativa (+10p de vida)")
                print("")
                jugador1.digicoins -= 3
                inventario1.añadir_objeto("Poción Curativa",1) 
            else:
                print("No tienes suficientes digicoins")
                bucle3 = False
        elif opcion_tienda == 3:
            if jugador1.digicoins >= 4:
                print("Has comprado anabolizantes (+5p de ataque)")
                print("")
                jugador1.digicoins -= 4
                inventario1.añadir_objeto("Anabolizantes",1)
            else:
                print("No tienes suficientes digicoins")
                print("")
                bucle3 = False
        elif opcion_tienda == 4:
            bucle3 = False
        else:
            print("Opción inválida. Intente de nuevo.")


                

def usar_item():
    pass


    

    
main()


 