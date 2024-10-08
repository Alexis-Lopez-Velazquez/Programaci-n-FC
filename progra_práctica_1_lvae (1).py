# -*- coding: utf-8 -*-
"""Progra_Práctica_1 LVAE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j6mXBS4lwO9lTwmzmKE3rjzJcSFaIVyH
"""

from posixpath import join #La funcion join nos ayudara a crear la cadena final, apartir de una lista
#Se definen las funciones que utilizara el main
def top(lista): #funcion para obtener el último elemento de una lista
  x=lista[-1]
  return x
def separar(cadena):  #funcion para crear una lista con los elementos de una cadena separados por un espacio
  Lista=cadena.split() #se utiliza el metodo split
  return Lista
def Is_operator(caracter):
  operadores={"+":1,"-":1,"/":2,"*":2,"**":3}
  if caracter in operadores:
    valor=operadores[caracter]
  else:
    valor= 0
  return  valor #La funcion nos devuelve el valor asociado a la jerarquia del operador, en caso de no ser operador devuelve cero

if __name__=="__main__": #Se implementa el main del programa
  cadena_inicial="3 * ( 1 + 3 ) ** 2" #cadena inicial en notacion usual con espacio entre caracteres
  lista_inicial=separar(cadena_inicial) #se convierte la cadena inicial en una lista inicial con los caracteres separados por espacios como elementos
  lista_final=[] #Se define la lista final vacia en un inicio, la cua se llenara con la notacion polaca inversa
  pila=[] #Se define la pila en un inicio vacia
  for caracter in lista_inicial: #Con el for se simula un apuntador que recorrera todos los caracteres de la lista inicial
    if caracter.isdigit(): #Se verifica si el caracter es un digito o no
      lista_final.append(caracter) #Se agrega el digito a la lista final
    elif Is_operator(caracter)>0: #Se verifica si el caracter es un operador y se le asigna un valor numerico de acuerdo a la jerarquia de operaciones
        j_caracter=Is_operator(caracter) #Se guarda el valor jerarjico del caracter
        if pila==[]: #Si la pila esta vacia se agrega el operador a la pila
          pila.append(caracter)
        else: #Cuando la pila no es vacia
          t=top(pila) #Se extrae el ultimo elemento de la pila
          j_pila=Is_operator(t) #Se extrae y guarda el valor jerarjico de este ultimo elemento

          if j_pila>j_caracter: #Se compara el valor jerarjico del caracter y el ultimo elemento de la pila
            lista_final.append(top(pila)) #Si el de mayor jerarquia es el de la pila entonces se agrega a la lista final
            pila.pop() #Se retira de la pila al operador anterior
          pila.append(caracter) #Se agrega el caracter a la lista final
    elif caracter=="(": #Si el caracter es un parentesis izquierdo se agrega al final de la pila
         pila.append(caracter)
    elif caracter==")":
         while top(pila)!="(": #Mientras el ultimo elemento de la pila no sea parentesis izquierdo, los operadores se agregan al final de la lista final
            lista_final.append(top(pila))
            pila.pop()
         pila.pop() #Se elimina el parantesis izquierdo de la pila
    else:
      print("La expresion no es admisible, escribe una expresion correcta")
while pila !=[]: #Mientras la pila no este vacía agrega los operadores restantes a la lista final
  lista_final.append(top(pila))
  pila.pop()
cadena_final=" ".join(lista_final) #Usando el metodo join se crea la cadena final a partir de la lista final creada en los pasos anteriores
print("La expresion en notacion usual es: %s" %cadena_inicial)
print("La expresion en notacion polaca inversa es: %s" %cadena_final)

from os import write
informe= open("informe_practica1.txt","w")
informe.write("Notacion Polaca Inversa:\n")
informe.write("El algoritmo recibe una cadena inicial que representa una expresion \n")
informe.write("algebraica en notacion usual con parentesis, dicha cadena debe de \n")
informe.write("tener los caracteres separados por espacios, de lo contrario imprimira\n")
informe.write("un mensaje de error.\n")
informe.write("Con la cadena inicial se sigue el siguiente algoritmo para devolver una\n")
informe.write("cadena con la expresion inicial, pero escrita en notacion polaca inversa:\n")
informe.write("PASO 1: Se convierte la cadena inicial en una lista inicial con la funcion 'separar'\n")
informe.write("PASO 2: Se crea una pila simulada con una lista vacia y una lista final, en esta\n")
informe.write("ultima se agregaran los caracteres output del programa\n")
informe.write("PASO 3: Se crea un ciclo For que recorrera todos los caracteres de la lista inicial\n")
informe.write("PASO 4: Se lee el caracter, si es un DIGITO, se agrega a la lista final y se pasa a\n")
informe.write(" leer el siguiente caracter, en OTRO CASO si es un OPERADOR se compara con el ultimo\n")
informe.write("elemento de la pila, MIENTRAS el elemento de la pila tenga una jerarquia mayor se agregara a\n")
informe.write(" la lista final, al terminar la CONDICION, se agrega el caracter a la pila y se pasa a leer\n")
informe.write("el siguiente caracter, en OTRO CASO si el caracter es un PARENTESIS IZQUIERDO se agrega a la pila\n")
informe.write("y se pasa a leer el siguiente caracter, en OTRO CASO si el caracter es un PARENTESIS DERECHO se\n")
informe.write("extraen los operadores de la pila MIENTRAS no sean un parentesis izquierdo y se van agregando\n")
informe.write("cada uno a la lista final, cuando se llega al parentesis izquierdo, este se elimina de la\n")
informe.write("pila y se pasa a leer el siguiente caracter, el ciclo For termina cuando no hay mas caracteres\n")
informe.write("que leer en la lista inicial\n")
informe.write("PASO 5: Se extraen de final a inicio los operadores restantes que hayan quedado en la pila despues\n")
informe.write("del ciclo For y se van agregando a la cadena final\n")
informe.write("PASO 6: Se crea la cadena final a partir de la lista final con la funcion 'join'\n")
informe.write("PASO 7: Se imprime la cadena inicial en notacion usual y la cadena final en notacion polaca inversa\n")
informe.close()