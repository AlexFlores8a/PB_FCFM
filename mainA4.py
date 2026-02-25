from A4 import procesar_contactos
"""Si quieren probar su código pueden guardarlo en su computadora
en la misma ubicación que este script.
Luego, en terminal como Admin teclean:
pip install faker
Y pueden ejecutar este script para ver si hace lo que se pide"""

from faker import Faker


fake = Faker()
lista = []
for _ in range(5):
    nombre = fake.name()
    telefono = fake.phone_number()
    telefono = telefono.replace("-","")
    telefono = telefono.replace("(","")
    telefono = telefono.replace(")","")
    telefono = telefono.replace("+","")
    telefono = telefono.replace("x","")
    mail = fake.email()
    mail = mail.replace("example","gmail")
    contacto = (nombre, telefono, mail)
    lista.append(contacto)
        
for contacto in lista:
    print(contacto)

lista_nueva = procesar_contactos(lista)
for contacto in lista_nueva:
    print(contacto)
