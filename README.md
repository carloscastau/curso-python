
#Curso de Python Intermedio Platzi

##Comprehensions, Lambdas y Manejo de Errores

![](https://static.platzi.com/media/achievements/badge-intermedio-de-python-d0d16518-5edd-450a-b2a9-0710bded1494.png)
### Features

- Finalizado
- Finalización mayo 26, 2022
- Profesor: Facundo García Martoni
- Escuela/Carrera: Escuela de Data Science




**Table of Contents**

[TOCM]

[TOC]

#Preparación antes de empezar
##Zen de Python
###import this "En consola"
1. Bello es mejor que feo: *"Pyhton es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética."*
2. Explícito es mejor que implícito: *"Hacer más fácil que las otras personas entiendan el código."*
3. Simple es mejor que complejo: *"Es mejor tener una implementación simple, que ocupe pocas lineas de código y sea entendible, a que sea una larga y complicada."*
4. Complejo es mejor que complicado: *"Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal."*
5. Plano es mejor que anidado: *"Es mejor evitar el anidamiento, y hacer las cosas de manera plana."*
> "El anidamiento es cuando tenemos un bloque de código dentro de otro bloque de código (dependiendo de este). Esto se nota en Python por la identación, nos quedarían estos bloques muy corridos a la derecha."5. Plano es mejor que anidado:" 

6. Espaciado es mejor que denso: *"Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado."*
7. La legibilidad es importante: *"Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajemos con otros en los proyectos."*
8. Los casos especiales nunca son tan especiales para romper las reglas, 
9. (Sin embargo la practicidad le gana a la pureza): *"Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy puro o muy ‘Pythonista’, este pierde legibilidad, es mejor ser más prácticos y romper o saltearnos algunas de estas reglas para que el código sea más eficiente. Por lo tanto, llegado el momento debermos decidir si es mejor hacer las cosas de manera pura o práctica."*
10. Los errores nunca deberían pasar silenciosamente, 
11. (A menos que se silencie explicitamente):*"Manejar los erroes es fundamental. Cada error nos dice algo y hay que prestarle atención. A menos que seas capaz de silenciar un error explícitamente, aunque para esto hay que tener criterio."*
12. Frente a la ambigüedad alejese de la tentación de adivinar: *"Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución."*
13. Debería haber una, y preferiblemente sola, una manera obvia de hacerlo, 
14. (Aunque esa manera puede no ser obvia al principio a menos que seas holandés): *"Esto hace referencia al creador de Python ''Guido van Rossum", que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo"*
15. Ahora es mejor que nunca, : *"Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante."*
16. (Aunque nunca suele ser mejor que ahora mismo): *"Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal."*
17. Si la implementación es díficil de explicar, es una mala idea, 
18. Si es fácil de explicar, puede ser una buena idea: *"Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución."*
19. Los espacios de nombres son una gran idea, ¡hagamos más de eso!

##Documentación de Python
La puedo encontrar en español:
[Documentación de Python](https://docs.python.org/es/3/ "Documentación de Python")
#Entorno virtual
##¿Qué es un entorno virtual?
Un entorno virtual es un Python aislado para cada proyecto, en el que puedes controlar las versiones y módulos instalados. Los módulos jamás se deben instalar en global, si no en entornos virtuales. Lo que pase dentro del virtual environment no afectará al Python global.
[![Entornos virtuales](https://i0.wp.com/3.214.197.113/wp-content/uploads/2021/07/entornos_python.png?resize=602%2C469 "Entornos virtuales")](https://i0.wp.com/3.214.197.113/wp-content/uploads/2021/07/entornos_python.png?resize=602%2C469 "Entornos virtuales")
##El primer paso profesional: creación de un entorno virtual
1. Buenas practicas:
**code .** *"abre VSCode en la carpeta que estás"*
1. Como buena práctica, inicializa la carpeta de tu proyecto como un entorno de Git.
**git init** *"inicializa el repositorio"*
2. Crea el entorno virtual en ella con:
**py -m venv venv** *"en Python, llama al módulo venv (virtual environment) y guárdalo en la carpeta "venv"."*
3. Activa el venv para que la computadora trabaje con ese entorno  y no con el global así:
**.\venv\Scripts\activate**  *"activa el venv y aparecerá un: "(venv)" en el inicio de cada línea de la terminal."*
**alias avenv=.\venv\Scripts\activate** *"en la terminal crea un shortcode para activar el venv de una manera más rápida, esto solo funciona con Cmder y queda guardado para siempre. La próxima solo deberás digitar: avenv"*
**deactivate** *"desactiva el venv (desaparece el "(venv)")."*
4. Una buena práctica es ignorar el venv en el repositorio: Crea un archivo en la carpeta principal llamado .gitignore y dentro pon: venv/ y guárdalo. Notarás que ahora el nombre de la carpeta está en gris en VSCode.
##Instalación de dependencias con pip
PIP → **Package Installer for Python**
PIP instala módulos que no vienen dentro de Python. 
Por ejemplo:

- Requests y BeautifulSoup4 → sirven para webscraping
- Pandas y Numpy → se usan en data science para los datos
- Pytest → sirve para realizar testing

###comandos de pip

PIP tiene que ser usada de la mano con venv y no debería ser usado fuera del mismo,
porque va a instalar los módulos con pip solo dentro del proyecto.
- **pip freeze** te muestra los módulos que tienes instalados en tu entorno
virtual.
- **pip install pandas** (pandas es el nombre del módulo) instala el módulo en el venv y ya lo puedes usar en cualquier archivo py dentro del venv. Pandas es un módulo que usa otros módulos para funcionar así que los instalará también.

###¿Qué pasa si quieres compartir tu proyecto? 
Necesitas que los otros desarrolladores lo usen con exactamente las mismas dependencias y módulos.
- **pip freeze > requirements.txt** este comando guarda todos tus módulos en
su versión actual en un nuevo archivo dentro de la carpeta, llamado
requirements.txt. Puedes verlo con cat requirements.txt.
- **pip install -r requirements.txt** instala todos los módulos dentro de
requirements.txt (esto debe ejecutarlo la desarrolladora a la que le compartiste
el proyecto)
#Alternativa a los ciclos: comprehensions
##Listas y dicionarios anidados

Los diccionarios pueden almacenar listas y las listas pueden almacenar diccionarios.

##List comprehensions

A una lista puedes añadirle elementos con un ciclo for y un filtro condicional en una sola línea:
1. **natural_numbers = [i &#42; &#42; 2 for i in range(1, 101) if i % 3 != 0]**


	Lista de los primeros 100 números naturales al cuadrado mientas no sean divisibles para 3

###Estructura:
**[element for element in iterable if condition]**
##Dictionary comprehensions

Es muy parecido a las list comprehensions:
1. **dictionay_naturals = {i: i&#42; &#42;3 for i in range(1, 101) if i % 3 != 0}**


	Dictionary with the first 100 natural numbers as its key and numbers**3 as its values.
###Estructura:
**{key: value for element in iterable if condition}**

#Conceptos avanzados de funciones
##Funciones anónimas: lambda
Hay una forma de crear funciones sin nombre, anónimas. Se las conoce como lambda
functions. Pueden tener todos los argumentos necesarios, pero solo puede tener una
línea de código.
###Estructura:
**lambda argumentos: expresión**

No usa return, ya que por defecto guarda el resultado de la función anónima en la
variable.

Para ejecutar la función, usa la variable en la que la guardaste y ponle como
argumentos los señalados en lambda (en este caso, una string).

##High order funtcions: filter, map and reduce
Una función de orden superior es una función que recibe como parámetro a otra
función.

Las funciones filter, map y reduce son muy importantes en una gran cantidad de
lenguajes:
###Filter
La función filter recibe como parámetros una lambda function y una lista (en realidad un iterable). Devuelve un iterador que puedes guardar en otra lista.

filter devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
###Map

**La diferencia entre filter y map:**

Map funciona muy parecido a filter, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.

###reduce

Se necesita usar el módulo functools para poderlo usar. Hace que todos los números dentro de una lista hagan las operaciones, indicadas en la función, entre sí y devuelve 1 solo valor.

Reduce toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

###Resumen
- **Filter** filtra los datos de una lista retornando solo los que son True
- **Map** manipula los datos de una lista
- **Reduce** opera los datos de una lista entre sí para obtener 1 solo resultado

#Manejo de errores
##Los errores de codigo
Hay errores que Python te avisa que te equivocaste, devolviendo un traceback
(rastreo). Los mensajes traceback se deben leer desde la última línea hasta la primera.

[![Errores](https://static.platzi.com/media/user_upload/error-62a56437-8b39-4cd9-85da-0dac5854ee3d.jpg "Errores")](https://static.platzi.com/media/user_upload/error-62a56437-8b39-4cd9-85da-0dac5854ee3d.jpg "Errores")


Si hay un SyntaxError, el programa no se va a ejecutar. Por otro lado, si son
excepciones, sí se ejecutará.

##Debugging

**Depuración** Hacer esto es la manera correcta de encontrar los errores de tu código en lugar de ir revisando línea por línea. Esto se hace cuando Python no te dice cuál es el error, sino que el error es de tu algoritmo y debes revisar lo que escribiste. Visual Studio Code tiene una función propia que te ayuda con esto. Dale a run and debbug y luego en el menú que te sale, dale a pausa para ir viendo línea a línea qué está pasando. Step over te hace avanzar a cómo se está ejecutando el programa. Step into te mete en la función sobre la que estés. En la parte izquierda sale una pestaña con todas las variables que hay en el código con los valores que contienen. Si le das clic a una línea de código en específico, ya no hay necesidad de usar el botón de pausa, sino que el programa se ejecutará y luego se detendrá en el breakpoint que creaste. Puedes crear varios breakpoints.

##Manejo de excepciones
Para esto hay algunas palabras clave:

###Try and except
Cuando tengas un programa que es posible que haya algún error de excepción, por ejemplo en un formulario o en esta función que se deben ingresar strings, pero el usuario ingresó un number; puedes usar try para que intente ejecutar el programa. Y si hay un error, puedes poner debajo un except error_name y que el programa haga otra cosa para que no se dé el error. Si el error de excepción que se produce es diferente al que colocaste en el except, se producirá el error.

[![Errores](https://hub.packtpub.com/wp-content/uploads/2019/12/image2.png "Errores")](https://hub.packtpub.com/wp-content/uploads/2019/12/image2.png "Errores")

###Raise
Eleva un error para en caso de que pase algo, lo invoque. En la definición se usa un try and except. En el try pon el error con un if (en este caso una cadena vacía) y luego convoca (eleva) un ValueError con raise ValueError("mensaje") . Y luego el return o la función como tal. En el except, vuelve a convocar el ValueError que creaste (el as ve: es una abreviación impuesta) y puedes hacer que se imprima el mensaje que pusiste y un return para la función:

###Finally
Es rara de encontrar. Se la usa al final de un try except para hacer cosas particulares como cerrar un archivo, cerrar una conexión a una base de datos o liberar recursos externos.

##Asser statements
Otra manera de manejar errores. Si bien es menos común que los anteriores, también se puede hacer.
Assert significa afirmar. Así que se lee: afirmo que esta condición es verdadera, si no, imprimo este mensaje de error.
#Manejo de archivos
##¿Cómo trabajar con archivos?

Hay 2 tipos de archivos: los de texto y los binarios.
Los binarios tienen dentro bytes que representan cosas muy complejas. Son archivos con los que no se interactúa con los lenguajes de programación, sino con software especializado.

Hay 3 formas de abrir un archivo de texto con Python:

- **R** Lectura ("Read")
- **W** Escritura (sobreescribir "Write")
- **A** Escritura (agregar al fina "Append")

with — si se cierra el programa o script inesperadamente, hace que el archivo no se rompa.
