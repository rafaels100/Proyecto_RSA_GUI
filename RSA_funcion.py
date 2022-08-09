from math import gcd
from random import randint

def RSA(a):
    p = 101
    q = 97
    n = p*q

    #[2]
    #Bob busca un numero e tal que
    #1 <= e < (p-1)(q-1)
    #y e coprimo con (p-1)(q-1)
    #Esto lo puedo hacer haciendo:
    m = (p-1)*(q-1)
    #y busco un numero e tal que (e:m) = 1 con e < m - 2
    """
    #Por que e < m - 2 ?
    #Porque, por ej, si
    e = 67 => 67 coprimo con 66
    e = 710 => 710 es coprimo con 709
    e = 198 => 198 es coprimo con 197
    Todo numero menor en 1 al numero elegido sera coprimo con e, por lo que sirve,
    pero es muy facil de adivinar.
    """
    #Agrego un poco de randomness al situar el inicio de la busqueda en algun
    #numero entre 1 y 50. Digamos, 35
    for i in range(35, m - 1):
        if gcd(i, m) == 1:
            e = i
            break
##    print("e: ", e)
    #[3]
    #Resuelve e x conguente a 1 mod m, es decir
    # e*x % m == 1
    #Sea d con 1 <= d < m una solucion particular de la ecuacion de arriba
    #(es decir, un x que la resuelve)
    for i in range(0, m):
        if (e * i) % m == 1:
            d = i
            break
##    print(d)
    #Bob crea entonces la clave privada como
    pr_key = [n, e]
    print("private key: ", pr_key)
    #y la clave publica como
    pu_key = [n, d]
    print("public key: ", pu_key)


    #[4]
    #Supongamos ahora que Alice tiene un mensaje a para enviarle a Bob
    #Crea una lista con los numeros correspondientes a cada letra del mensaje A
    #en codigo ascii, utilizando la funcion ord()
    A_ = [ord(x) for x in a]
    print("letras sin encriptar: ", A_)
    #Alice toma su mensaje a y lo eleva a la d (utilizando la clave publica de Bob),
    #para despues calcular el mod n de dicho numero (n tambien lo saca de la clave publica)
    #Alice llama a su mensaje encriptado, c:
    #Esto lo hago para cada numero del codigo ascii, encriptando cada uno de ellos
    C = [((x**pu_key[1]) % pu_key[0]) for x in A_]
    print("letras encriptadas: ", C)

    #[5]
    #Bob recibe c, el mensaje encriptado que Alice le envio, y lo eleva a la e,
    #numero que forma parte de su clave privada y que solo el conoce. Luego le
    #calcula el mod n (que forma parte tanto de su clave privada como publica).
    #Llama al mensaje desenciptado c_a
    #Desencripto cada numero correspondiente al codigo ascii y luego lo paso a
    #su forma de string con chr()
    
    #Este paso lo hago en la otra aplicacion que desencripta
    return C
##RSA(5)
