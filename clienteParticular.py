#! /usr/bin/env python3
from cliente import Cliente

class ClienteParticular(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre, apellido, telefono, mail, id_cliente = None):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(telefono, mail, id_cliente)
        self.clientes=[]
        
    def nuevo_paticular(self, nombre, apellido, telefono, mail):
        c=ClienteParticular(nombre, apellido)
        super().nuevo_cliente(telefono, mail)
        self.clientes.append(c)
        
        print(self.clientes)
