# dxf2gmlcatastro (v. 2.1)

Script Python para convertir DXF al GML de Parcela Catastral según el estándar de la Dirección General de Catastro.

Más información en la entrada de SIGdeletras [http://sigdeletras.com/2016/dxf2gmlcatastro-script-python-para-convertir-de-dxf-a-gml-parcela-catastral](http://sigdeletras.com/2016/dxf2gmlcatastro-script-python-para-convertir-de-dxf-a-gml-parcela-catastral)

## Versiones de Python y GDAL

El script esta testeado en Python 2.7.6 y Python 3.4.3.
Para Py2 se ha utilizado la versión GDAL 1.11.2. La versión para Py3 es la 1.10.1.


## Requisitos

Tener instalado Python y la libraría GDAL. La librería [GDAL](https://pypi.python.org/pypi/GDAL/) es la que se encargará de todas las operaciones de acceso y lectura del archivo DXF. 

    $ sudo apt-get install python-gdal

### GDAL en Windows

Más información en la entrada ["Instalación de Python y GDAL en Windows"](http://www.sigdeletras.com/2016/instalacion-de-python-y-gdal-en-windows)

#### Usando OSGEO

Tras instalar GDAL mediante [OSGEO4W installer](http://trac.osgeo.org/osgeo4w/wiki) podemos usar *Inicio>OSGeo4W>OSGeo4W Shell* para ejecutar el script.

### Instalando GDAL y definiendo variables del sistema

Podemos seguir alguno de estos dos manuales

* [http://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows](http://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows)
* [http://cartometric.com/blog/2011/10/17/install-gdal-on-windows/](http://cartometric.com/blog/2011/10/17/install-gdal-on-windows/)

## Pasos

* Generar el archivo DXF seguiremos los Pasos 1 y 2 de la [guía de Catastro](http://www.catastro.minhap.es/documentos/portal%20generacion%20GML.pdf).
* Desde terminal ejecutar dxf2gmlcatastro.py añadiendo los arguementos necesarios:
    - ruta/nombre de dxf de entrada
    - nombre del gml de salida
    - Código EPSG del Sistema de Referencia de Coordenadas del archivo DXF
        + 25828 Proyección UTM ETRS89 Huso 28 N
        + 25829 Proyección UTM ETRS89 Huso 29 N
        + 25830 Proyección UTM ETRS89 Huso 30 N
        + 25831 Proyección UTM ETRS89 Huso 31 N

```
$ python dxf2gmlcatastro.py archivodxf.dxf archivogml.gml 25830
```

## Usar dxf2gmlcatastro en QGIS

Definir la variable PYTHONPATH

Importar módulo

Ejecutar la función crea_gml

## 2do
* Investigar qué es el "Identificativo local de la parcela"  y se si debería solicitar al ejecutar el script.
* Generar un GML de varias parcelas catastrales
* Crear un script para edificio
* Probarlo en otros Sistemas Operativos (MacOS)
