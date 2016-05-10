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

Para usar el módulo en QGIS 
- Instalar [QGIS](https://www.qgis.org/en/site/forusers/download.html)
- Definir variable PYTHONPATH con la carpeta donde se encuentre los archivos de dxf2gmlcatastro
- Importar *dxf2gmlcatastro* usando la consola de Python de QGIS
- Ejecutar la función crea_gml

    dxf2gmlcatastro.crea_gml('C:\carpeta\archivoparcela.dxf', 'C:\carpeta\gmlcatastro.gml', '25830')

Más información en la entrada [Cómo usar módulos de Python en QGIS. Un ejemplo con dxf2gmlcatastro](http://www.sigdeletras.com/2016/como-usar-modulos-de-python-en-qgis-un-ejemplo-con-dxf2gmlcatastro)

## Informacióm sobre el "Identificativo local de la parcela (localId)"
Según el documento [Formato GML de parcela catastral](http://www.catastro.meh.es/documentos/formatos_intercambio/Formato%20GML%20parcela%20catastral.pdf)

*Identificativo de la parcela (cp:inspireId):Se compone de un identificador (localId) y un espacio de nombres (namespace)*

- *Si  la  parcela  está  inscrita  en  las  bases  de  datos  de  catastro,  o  se  desea conservar la referencia catastral en el caso de una segregación o agregación, el valor del atributo identificativo localId será la referencia catastral y el valor del  atributo namespace empleado  será ES.SDGC.CP ,  propio  de  la  Dirección General del Catastro.*
- *Si la parcela no  existe  en la  base  de  datos  de  catastro  se deberá  emplear el valor  del  atributo namespace  ES.LOCAL.CP  y  un  identificador  unívoco  dentro del negocio jurídico en el cual se incluye el GMl de parcela catastral*

**En esta versión el GML se ha generado como si la parcela catastral no existiera por lo que el atributo atributo namespace  es ES.LOCAL.CP y el id asignado es el mismo que el GML de ejemplo (ES.LOCAL.CP.1A). Este id puede ser editado con cualquier editor de texto.**

## 2do
* Añadir el "Identificativo local de la parcela (localId)" como argumento.
* Generar un GML de varias parcelas catastrales(localId)
* Probarlo en otros Sistemas Operativos (MacOS)

## Notas
De acuerdo con el artículo 18.3 del RD 417/2006, de 7 de abril, por el que se desarrolla el texto refundido de la Ley del Catastro Inmobiliario, aprobado por el Real Decreto legislativo 1/2004, de 5 de marzo , e n los siguientes supuestos la asignación de la referencia catastral se realizará conforme a las siguientes reglas:

- División  o  agrupación  de  inmuebles:  la  referencia  de  la  finca  matriz  o  de  las  fincas  agrupadas  desaparecerá  y  se asignará una nueva a cada una de las fincas resultantes.
- Segregación  de  inmuebles:  se  mantendrá  la  referencia  de  la  finca  sobre la  que  se  practica  la  segregación  y  se asignará una nueva a cada una de las fincas segregadas.
- Agregación de inmuebles: se mantendrá la referencia de la finca sobre la que se practica la agregación.
