# dxf2gmlcatastro

Script Python para convertir DXF al GML de Parcela Catastral según el estándar de la Dirección General de Catastro.

***NOTA:El script está generado para archivos DXF en ETRS89 UTM30N (EPGS:25830). A día de hoy para indicar un SRC distinto habrá que editar el archivo plantillacatastro.py o bien cambiar el códifo en el GML final.***

Más información en la entrada de SIGdeletras []()

## Requisitos

Tener instalado Python y la libraría GDAL. La librería [GDAL](https://pypi.python.org/pypi/GDAL/) es la que se encargará de todas las operaciones de acceso y lectura del archivo DXF. 

    $ sudo apt-get install python-gdal

## Pasos

* Generar el archivo DXF seguiremos los Pasos 1 y 2 de la [guía de Catastro](http://www.catastro.minhap.es/documentos/portal%20generacion%20GML.pdf).
* Copia del DXF en la misma carpeta donde se encuentran los ficheros *dxf2gmlcatastro.py* y *plantillacatastro.py*
* Renombrar el DXF a **parcelacad.dxf**
* Desde terminal ejecutar

```
$ pyhon dxf2gmlcatastro.py
```

## 2do

* Permitir elegir el SRC del GML.
* Investigar qué es el "Identificativo local de la parcela"  y se si debería solicitar al ejecutar el script.
* Poder elegir el archivo DXF a transformar
* Poder elegir el archivo GML a crear
* Generar un GML de varias parcelas catastrales
* Crear un script para edificio
* Probarlo en otros Sistemas Operativos
