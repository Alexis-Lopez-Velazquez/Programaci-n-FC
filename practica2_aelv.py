# -*- coding: utf-8 -*-
"""Practica2-AELV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xtzt8Ri_tUqNo2CLRqdSdaBJT3hCjTE_

Practica 2
López Velázquez Alexis Eduardo  
Centro de llamadas
"""

import numpy as np
import matplotlib.pyplot as plt
#Definimos las clases que usarmeos en esta simulacion:
class Clientes():
  """
  Representara a los clentes de nuesra simulación, sus atributos seran:
  hora de llegada, hora de atencion, hora de salida y tipo de cliente, si es
  normal sera tipo 0 y si es Premiere sera tipo 1.
  """
  def __init__(self,h_ll,h_at,h_s,tipo):
    self.hora_llegada = h_ll
    self.hora_atencion = h_at
    self.hora_salida = h_s
    self.tipo_de_cliente = tipo
class Cola():
  """
  La clase cola simulara la fila virtual que hacen los clientes en la linea
  de espera antes de ser atendidos, se simulara con una lista, con los metodos
  LLegada, Salida de clientes, y Vacia para saber si la cola esta vacia o no.
  """
  def __init__(self):
    self.cola = [] #En un inicio la cola esta vacia
  def llegada(self,cliente):
    """
    Este metodo agrega un cliente a la cola, requiere al cliente y
    no devuelve nada
    """
    self.cola.append(cliente)
    def salida(self,cliente):
      """
      Este metodo elimina un cliente de la cola, requiere al cliente, verifica
      si la cola esta vacia y en caso de no estarlo devuelve
      al cliente que salio.

      """
      if len(self.cola) > 0:
        x=self.cola.pop(0) #sacamos al primero que llego a la fila
        return x
      else:
        print("No hay clientes en la cola")
  def vacia(self):
    """
    Este metodo verifica si la cola esta vacia o no, devuelve True si esta vacia
    y False si no lo esta
    """
    if len(self.cola) == 0:
      return True
    else:
      return False
class Servidor():
  """
  La clase servidor simulara a todas las lineas del centro de llamadas, su
  atributo es el numero de lineas y se simula con una lista de ceros, donde
  cero indica que la linea esta vacia, tendra los metods atender y linea_libre.
  """
  def __init__(self,numero_lineas):
    self.servidor=[0]*(numero_lineas)
  def atender(self,min_at,max_at,numero_de_linea):
    """
    Este metodo recibe los tiempos minimo y maximo de atencion, asi  commo el
    numero de linea que atendera y devuelve el tiempo de atencion en horas,
    distribuido cn probabilidad uniforme entre el tiempo minimo y maximo.
    """
    tiempo_atencion=np.random.uniform(min_at,max_at)
    self.servidor[numero_de_linea]=(tiempo_atencion)/60
    return (tiempo_atencion)/60
  def buscar_linea(self):
    """
    Este metodo busca en el servidor una linea desocupada, es decir cuyo valor
    sea cero, devuelve el numero de linea desocupada.
    """
    for i,linea in enumerate(self.servidor):
      if linea==0:
        return i
    return None
class Simulacion():
  """
  Esta es la clase principal, sus atributos son el numero de clientes, de lineas
  ,la probabilidad uniforme de tener un cliene premiere, una cola premiere
  y otra cola normal, asi como el tiempo minimo y maximo de arribo y atencion.
  """
  def __init__(self,n_clientes,n_lineas,proba,max_at,min_at,max_int,min_int):
    self.numero_clientes=n_clientes
    self.numero_lineas=n_lineas
    self.proba_premiere=proba
    self.max_atencion=max_at
    self.min_atencion=min_at
    self.max_interarribo=max_int
    self.min_interarribo=min_int
    self.cola_normal=Cola()
    self.cola_premiere=Cola()
  def simular(self):
    """
    Este metodo ejecuta la simulacion del centro de llamadas caracteriazado por
    los atributos definidos en la clase simulacion, con los atributos se simula
    la interaccion entre el servidor de lineas y los clientes, ponidolos en
    espera y atendiendoles de acuerdo a su tipo, el metodo devuelve dos listas
    con los tiempos de espera de cada cliente en la cola de cada tipo.
    """
    tiempos_espera_normal=[]
    tiempos_espera_premiere=[]
    interarribos=(np.random.uniform(self.min_interarribo,
                   self.max_interarribo,self.numero_clientes))
    minutos_llegada=interarribos.cumsum() #cumsum da la suma acumulada
    horas_llegada=[minutos/60 for minutos in minutos_llegada]
    servidores=Servidor(self.numero_lineas) #se crea el servidor
    contador_de_clientes=0
    while contador_de_clientes <= self.numero_clientes: #limite de la simulacion
      reloj=0
      if servidores.servidor.buscar_linea()!=None: #linea libre
         linea=servidores.servidor.buscar_linea()
         hora_llegada=horas_llegada.pop(0)
         probabilidad=np.random.uniform(0,1) #determinamos si es premiere o no
         if probabilidad <= self.proba_premiere:
           tipo_de_cliente = 1
         else:
           tipo_de_cliente = 0
         cliente=Clientes(hora_llegada,hora_llegada,0,tipo_de_cliente) #creamos al cliente
         if tipo_de_cliente ==1:  #Formamos al cliente
           self.cola_premiere.llegada(cliente)
         else:
           self.cola_normal.llegada(cliente)
         x=servidores.atender(self.min_atencion,self.max_atencion,linea)
         h_s=hora_llegada+x
         servidores.servidor[linea]=h_s #la linea tiene la hora de salida
         cliente.hora_salida=h_s
         if tipo_de_cliente==1:
           tiempos_espera_premiere.append(0)
         else:
          tiempos_espera_normal.append(0)
         contador_de_clientes+=1
      elif servidores.servidor.buscar_linea()==None:
        reloj=min(servidores.servidor)







    return tiempos_espera_normal, tiempos_espera_premiere
  if __name__ == "__main__": #se implementa el amin del programa
    simulacion1=Simulacion(100,19,1/6,81,1,3,1)
    tiempos_espera_normal,tiempos_espera_premiere=simulacion1.simular()
    print(tiempos_espera_normal)
    print(tiempos_espera_premiere)

def buscar_linea(lista):
  for i,linea in enumerate(lista):
    if linea==0:
      return i
  return None

l=[2,5,6,0,8,8]
print(buscar_linea(l))