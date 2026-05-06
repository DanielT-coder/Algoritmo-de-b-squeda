# Algoritmo-de-búsqueda
Código de la tarea de algoritmos de búsqueda-Método asignado: Búsqueda Secuencial.

 # ANÁLISIS DE COMPLEJIDAD:
 La búsqueda secuencial consiste en recorrer la lista elemento por elemento hasta encontrar el valor buscado o llegar al final.

 ## Mejor caso:
 ### O(1)
 Ocurre cuando el elemento está en la primera posición.
 ## Caso promedio:
 ### O(n)
 Se debe recorrer aproximadamente la mitad de la lista.
 ## Peor caso:
 ### O(n)
 Ocurre cuando el elemento está al final o no existe en la lista.

 # ¿CUÁNDO ES MEJOR USARLO?
La búsqueda secuencial es recomenadable usarla cuando: 
- La lista es pequeña.
- Los datos no están ordenados.
- Se requiere una implementación simple.
- No se justifica usar algoritmos más complejos.

## Tambien es recomendable cuando: 
- los datos cambian constantemente.
- No hay tiempo de ordenarlos previamente.

# COMPARATIVA CON OTRO MÉTODO (BÚSQUEDA BINARIA)

## La búsqueda secuencial:
Recorre los datos uno por uno sin necesidad de que estén ordenados. Es fácil de implementar, pero lenta en listas grandes, con complejidad O(n).

## La búsqueda binaria: 
Requiere datos ordenados y divide el problema a la mitad en cada paso, por lo que es mucho más rápida, con complejidad O(log n).

La búsqueda secuencial destaca por su simplicidad, mientras que la búsqueda binaria ofrece mayor eficiencia. Por ello, la secuencial es ideal cuando se busca facilidad de implementación o los datos no están ordenados, mientras que la binaria es la mejor opción cuando se requiere rapidez en grandes volúmenes de información.
