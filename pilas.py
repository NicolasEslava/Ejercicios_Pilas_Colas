# PILAS (5 ejercicios)

class Pila:
    """Clase padre para todos los ejercicios de pilas."""

    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos.pop()

    def buscar(self, elemento):
        return elemento in self.elementos

    def mostrar(self):
        return self.elementos

    def cima(self):
        if len(self.elementos) == 0:
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)


# EJERCICIO 1: HISTORIAL DE PAGINAS WEB
# Crear una pila que represente el historial de navegacion de
# un usuario. Cada pagina visitada se agrega a la pila.
# La opcion volver elimina la pagina actual y regresa a la
# pagina anterior.

class HistorialWeb(Pila):

    def visitar(self, pagina):
        self.agregar(pagina)

    def volver(self):
        pagina = self.eliminar()

        if pagina is None:
            print("No hay paginas anteriores.")
        else:
            print("Regresando desde:", pagina)

    def pagina_actual(self):
        return self.cima()

# EJERCICIO 2: DESHACER ACCIONES
# Crear una pila para guardar acciones realizadas en un
# programa. La opcion deshacer elimina la ultima accion
# realizada.


class DeshacerAcciones(Pila):

    def realizar_accion(self, accion):
        self.agregar(accion)

    def deshacer(self):
        accion = self.eliminar()

        if accion is None:
            print("No hay acciones para deshacer.")
        else:
            print("Accion deshecha:", accion)


# EJERCICIO 3: PILA DE PLATOS
# Simular una pila de platos en un restaurante.
# Se puede agregar un plato, retirar el plato de arriba,
# buscar un plato y consultar cual esta arriba.

class PilaPlatos(Pila):

    def colocar_plato(self, plato):
        self.agregar(plato)

    def retirar_plato(self):
        plato = self.eliminar()

        if plato is None:
            print("No hay platos en la pila.")
        else:
            print("Plato retirado:", plato)

    def buscar_plato(self, plato):
        if self.buscar(plato):
            print("El plato esta en la pila.")
        else:
            print("El plato no esta en la pila.")


# EJERCICIO 4: CONVERSION DECIMAL A BINARIO
# Convertir un numero decimal a binario utilizando una pila.
# Se divide el numero entre 2 y se guardan los residuos.
# Luego se sacan los residuos de la pila para obtener el
# numero binario en el orden correcto.

class DecimalBinario(Pila):

    def convertir(self, numero):
        if numero == 0:
            return "0"

        while numero > 0:
            residuo = numero % 2
            self.agregar(residuo)
            numero = numero // 2

        binario = ""

        while not self.esta_vacia():
            binario += str(self.eliminar())

        return binario

# EJERCICIO 5: VERIFICAR PARENTESIS
# Determinar si una expresion tiene los parentesis
# correctamente cerrados.
# Cada parentesis de apertura se guarda en la pila.
# Cuando aparece un parentesis de cierre, se elimina uno
# de la pila.


class VerificarParentesis(Pila):

    def verificar(self, expresion):
        for caracter in expresion:

            if caracter == "(":
                self.agregar(caracter)

            elif caracter == ")":
                if self.esta_vacia():
                    return False

                self.eliminar()

        return self.esta_vacia()

# HISTORIAL WEB
# historial = HistorialWeb()
# historial.visitar("google.com")
# historial.visitar("youtube.com")
# historial.visitar("github.com")
# print(historial.mostrar())
# historial.volver()
# print("Pagina actual:", historial.pagina_actual())

# DESHACER ACCIONES
# acciones = DeshacerAcciones()
# acciones.realizar_accion("Escribir texto")
# acciones.realizar_accion("Borrar texto")
# acciones.realizar_accion("Cambiar color")
# acciones.deshacer()
# print(acciones.mostrar())

# PILA DE PLATOS
# platos = PilaPlatos()
# platos.colocar_plato("Plato 1")
# platos.colocar_plato("Plato 2")
# platos.colocar_plato("Plato 3")
# platos.buscar_plato("Plato 2")
# platos.retirar_plato()
# print(platos.mostrar())

# DECIMAL BINARIO
# conversion = DecimalBinario()
# print(conversion.convertir(25))

# PARENTESIS
# parentesis = VerificarParentesis()
# print(parentesis.verificar("(a + b) * (c - d)"))
# print(parentesis.verificar("(a + b) * (c - d"))
