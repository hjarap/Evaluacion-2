def agregar_compras(lista):
    monto= int(input("Ingrese el monto de la compra: "))
    lista.append(monto)
    print("La compra se ha agregado correctamente.")
def mostrar_compras(lista):
    if len(lista) == 0:
        print("No hay compras registradas.")
    else:
        print("Lista de compras: ")
        for i, compra in enumerate(lista, start=1):
            print(f"{i}. Monto: {compra}")
def mostrar_total(lista):
    total = sum(lista)
    print("total gastado: ", total)

def main():
    lista = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compras(lista)
        elif opcion == "2":
            mostrar_compras(lista)
        elif opcion == "3":
            mostrar_total(lista)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Ingrese una opción válida.")

main()


