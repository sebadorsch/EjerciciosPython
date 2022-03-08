"""
Clases de caracteres: Se pueden especificar clases de caracteres encerrando una lista de caracteres entre corchetes [],
    la que que encontrará uno cualquiera de los caracteres de la lista. Si el primer símbolo después del "[" es "^", la
    clase encuentra cualquier caracter que no está en la lista.


Metacaracteres:

- Delimitadores: Esta clase de metacaracteres nos permite delimitar dónde queremos buscar los patrones de búsqueda.
    Ellos son:
            ^	inicio de línea.
            $	fin de línea.
            \A	inicio de texto.
            \Z	fin de texto.
            .	cualquier caracter en la línea.
            \b	encuentra límite de palabra.
            \B	encuentra distinto a límite de palabra.

- Clases predefinidas: Estas son clases predefinidas que nos facilitan la utilización de las expresiones regulares.
    Ellos son:
            \w	un caracter alfanumérico (incluye "_").
            \W	un caracter no alfanumérico.
            \d	un caracter numérico.
            \D	un caracter no numérico.
            \s	cualquier espacio (lo mismo que [ \t\n\r\f]).
            \S	un no espacio.

- Iteradores: Cualquier elemento de una expresion regular puede ser seguido por otro tipo de metacaracteres,
    los iteradores. Usando estos metacaracteres se puede especificar el número de ocurrencias del caracter previo,
    de un metacaracter o de una subexpresión.
    Ellos son:
            *	    cero o más, similar a {0,}.
            +	    una o más, similar a {1,}.
            ?	    cero o una, similar a {0,1}.
            {n}	    exactamente n veces.
            {n,}	por lo menos n veces.
            {n,m}	por lo menos n pero no más de m veces.
            *?	    cero o más, similar a {0,}?.
            +?	    una o más, similar a {1,}?.
            ??	    cero o una, similar a {0,1}?.
            {n}?	exactamente n veces.
            {n,}?	por lo menos n veces.
            {n,m}?	por lo menos n pero no más de m veces.

- Alternativas: Se puede especificar una serie de alternativas para una plantilla usando "|" para separarlas,
    entonces do|re|mi encontrará cualquier "do", "re", o "mi" en el texto de entrada.Las alternativas son evaluadas de
    izquierda a derecha, por lo tanto la primera alternativa que coincide plenamente con la expresión analizada
    es la que se selecciona.

- Subexpresiones: La construcción ( ... ) también puede ser empleada para definir subexpresiones

    Ejemplos:
        (foobar){10} --> encuentra cadenas que contienen 8, 9 o 10 instancias de 'foobar'

        foob([0-9]|a+)r --> encuentra 'foob0r', 'foob1r' , 'foobar', 'foobaar', 'foobaar' etc.

- Memorias (backreferences): Los metacaracteres \1 a \9 son interpretados como memorias. \ encuentra la subexpresión
previamente encontrada #.

    Ejemplos:
        (.)\1+ --> encuentra 'aaaa' y 'cc'.

        (.+)\1+ --> también encuentra 'abab' y '123123'

        (['"]?)(\d+)\1 --> encuentra '"13" (entre comillas dobles), o '4' (entre comillas simples) o 77 (sin comillas) etc.

"""

# importando el modulo de regex de python
import re

if __name__ == '__main__':
    print("Validando MAILS:")
    """
                                    Validando MAILS: 
    Para validar que un mail tenga la estructura correcta, podemos utilizar la siguiente expresion regular:

        regex: \b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b

        Este es el patrón que utilizamos en el ejemplo de la opción VERBOSE.

    """
    # Ejemplo de VERBOSE
    mail = re.compile(r"""
    \b             # comienzo de delimitador de palabra
    [\w.%+-]       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
    +@             # seguido de @
    [\w.-]         # dominio: Cualquier caracter alfanumerico mas los signos (.-)
    +\.            # seguido de .
    [a-zA-Z]{2,6}  # dominio de alto nivel: 2 a 6 letras en minúsculas o mayúsculas.
    \b             # fin de delimitador de palabra
    """, re.X)

    mails = """raul.lopez@relopezbriega.com, Raul Lopez Briega,
    foo bar, relopezbriega@relopezbriega.com.ar, raul@github.io, 
    https://relopezbriega.com.ar, https://relopezbriega.github.io, 
    python@python, river@riverplate.com.ar, pythonAR@python.pythonAR
    """
    # filtrando los mails con estructura válida
    print(mail.findall(mails))




    print("Validando URLS:")
    """
                                    Validando una URL
                                    
    Para validar que una URL tenga una estructura correcta, podemos utilizar esta expresion regular:
    
    regex: ^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$
    """

    # Validando una URL
    url = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")

    # vemos que https://relopezbriega.com.ar lo acepta como una url válida.
    print(url.search("https://relopezbriega.com.ar"))

    # pero https://google.com/un/archivo!.html no la acepta por el carcter !
    print(url.search("https://google.com/un/archivo!.html"))

    # Acá si:
    print(url.search("https://google.com/un/archivo.html"))





    print("Validando IP:")
    """
                                    Validando una dirección IP
                                    
    Para validar que una dirección IP tenga una estructura correcta, podemos utilizar esta expresión regular:
    
    regex: ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
    
    """

    # Validando una dirección IP
    patron = ('^(?:(?:25[0-5]|2[0-4][0-9]|'
              '[01]?[0-9][0-9]?)\.){3}'
              '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

    ip = re.compile(patron)

    # la ip 73.60.124.136 es valida
    print(ip.search("73.60.124.136"))

    # pero la ip 256.60.124.136 no es valida
    print(ip.search("256.60.124.136"))





    print("Validando una fecha:")
    """
                                    Validando una fecha
                                    
    Para validar que una fecha tenga una estructura dd/mm/yyyy, podemos utilizar esta expresión regular:
    
    regex: ^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$
    
    """

    # Validando una fecha
    fecha = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$')

    # validando 13/02/1982
    print(fecha.search("13/02/1982"))

    # no valida 13-02-1982
    print(fecha.search("13-02-1982"))

    # no valida 32/12/2015
    print(fecha.search("32/12/2015"))

    # no valida 30/14/2015
    print(fecha.search("30/14/2015"))