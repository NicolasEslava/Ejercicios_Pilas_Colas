# COLAS (5 ejercicios)
class Cola:
    """Clase padre para todos los ejercicios de colas."""

    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop(0)

    def buscar(self, elemento):
        return elemento in self.elementos

    def mostrar(self):
        return self.elementos

    def primero(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos[0]

    def ultimo(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)

# EJERCICIO 1: COLA DE SUPERMERCADO
# Simular una fila de clientes en un supermercado.
# Los clientes llegan al final de la cola y se atiende
# primero al cliente que llego primero.


class ColaSupermercado(Cola):

    def agregar_cliente(self, nombre):
        self.agregar(nombre)

    def atender_cliente(self):
        cliente = self.eliminar()

        if cliente is None:
            print("No hay clientes en la fila.")
        else:
            print("Atendiendo a:", cliente)

    def buscar_cliente(self, nombre):
        if self.buscar(nombre):
            print("El cliente esta en la fila.")
        else:
            print("El cliente no esta en la fila.")


# EJERCICIO 2: COLA DE IMPRESION
# Simular una cola de documentos enviados a una impresora.
# Los documentos se imprimen en el mismo orden en que fueron
# enviados.

class ColaImpresion(Cola):

    def agregar_documento(self, documento):
        self.agregar(documento)

    def imprimir_documento(self):
        documento = self.eliminar()

        if documento is None:
            print("No hay documentos para imprimir.")
        else:
            print("Imprimiendo:", documento)

    def siguiente_documento(self):
        return self.primero()

# EJERCICIO 3: COLA DE ATENCION MEDICA
# Crear una cola sencilla para organizar pacientes.
# Los pacientes se registran en la cola y se atienden en el
# orden de llegada.


class ColaPacientes(Cola):

    def registrar_paciente(self, paciente):
        self.agregar(paciente)

    def atender_paciente(self):
        paciente = self.eliminar()

        if paciente is None:
            print("No hay pacientes esperando.")
        else:
            print("Atendiendo paciente:", paciente)

    def paciente_en_espera(self, paciente):
        return self.buscar(paciente)


# EJERCICIO 4: COLA DE PEDIDOS DE RESTAURANTE
# Simular una cola de pedidos que deben ser preparados en
# cocina. Cada pedido se agrega al final y el cocinero
# prepara primero el pedido que llego primero.

class ColaPedidos(Cola):

    def recibir_pedido(self, pedido):
        self.agregar(pedido)

    def preparar_pedido(self):
        pedido = self.eliminar()

        if pedido is None:
            print("No hay pedidos pendientes.")
        else:
            print("Preparando:", pedido)

    def pedido_pendiente(self, pedido):
        if self.buscar(pedido):
            print("El pedido esta pendiente.")
        else:
            print("El pedido no esta pendiente.")


# EJERCICIO 5: ROUND ROBIN
# Simular el algoritmo Round Robin utilizando una cola.
# Cada proceso recibe un tiempo limitado de ejecucion.
# Cuando termina su turno y todavia necesita tiempo,
# vuelve al final de la cola.

class RoundRobin(Cola):

    def agregar_proceso(self, nombre, tiempo):
        proceso = [nombre, tiempo]
        self.agregar(proceso)

    def ejecutar(self, quantum):
        if self.esta_vacia():
            print("No hay procesos.")
            return

        proceso = self.eliminar()
        nombre = proceso[0]
        tiempo = proceso[1]

        print("Ejecutando:", nombre)

        if tiempo > quantum:
            tiempo = tiempo - quantum
            self.agregar([nombre, tiempo])
            print("Tiempo restante:", tiempo)
        else:
            print("Proceso terminado:", nombre)


# EJERCICIO SUPERMERCADO
# supermercado = ColaSupermercado()
# supermercado.agregar_cliente("Carlos")
# supermercado.agregar_cliente("Maria")
# supermercado.agregar_cliente("Juan")
# supermercado.buscar_cliente("Maria")
# supermercado.atender_cliente()
# print(supermercado.mostrar())

# EJERCICIO IMPRESORA
# impresora = ColaImpresion()
# impresora.agregar_documento("Trabajo.pdf")
# impresora.agregar_documento("Tarea.docx")
# impresora.agregar_documento("Informe.pdf")
# impresora.imprimir_documento()
# print("Siguiente:", impresora.siguiente_documento())

# EJERCICIO ATENCION MEDICA
# pacientes = ColaPacientes()
# pacientes.registrar_paciente("Pedro")
# pacientes.registrar_paciente("Laura")
# pacientes.registrar_paciente("Andres")
# pacientes.atender_paciente()
# print(pacientes.mostrar())

# PEDIDOS DE RESTAURANTE
# pedidos = ColaPedidos()
# pedidos.recibir_pedido("Pedido 101")
# pedidos.recibir_pedido("Pedido 102")
# pedidos.recibir_pedido("Pedido 103")
# pedidos.pedido_pendiente("Pedido 102")
# pedidos.preparar_pedido()
# print(pedidos.mostrar())

# ROUND ROBIN
# round_robin = RoundRobin()
# round_robin.agregar_proceso("Proceso A", 7)
# round_robin.agregar_proceso("Proceso B", 4)
# round_robin.agregar_proceso("Proceso C", 6)
# round_robin.ejecutar(3)
# round_robin.ejecutar(3)
# round_robin.ejecutar(3)
# print(round_robin.mostrar())
