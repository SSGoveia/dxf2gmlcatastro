#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Nombre:
dxfparcela2gmlcatastro.py

Autor:
Patricio Soriano :: SIGdeletras.com

Descripción:
El script general el correspondiente fichero GML de parcela catastral según las
especificaciones de Castastro.

Especificaciones:
    - http://www.catastro.minhap.gob.es/esp/formatos_intercambio.asp

Requisistos:
- Es necesario tener instalado Python y GDAL
- El archivo DXF debe ser copiado en la misma ruta que los archivos .py

"""

import sys
try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: parece que no están instalados los GDAL/OGR')

#from osgeo import ogr
import os.path
from plantillacatastro import *

# Comprueba que parcelacad.dxf existe en el mismo directorio

dxffile = "parcelacad.dxf"
if os.path.isfile(dxffile):
    print "Archivo %s existente." % (dxffile)
else:
    print "No existe el fichero  %s." % (dxffile)
    print  "Añádalo en la misma carpeta que los archivos python."
    sys.exit()

# Accede mediante gdal al archivo DXF

driver = ogr.GetDriverByName('DXF')
dataSource = driver.Open(dxffile, 0)
layer = dataSource.GetLayer()

# Genera el archivo gml según el estándar de catastro
# añade la primera parte del texto

filegml = open(r'gmlcatastro.gml', 'w')
filegml.writelines(cabecera1)

print 'El archivo', dxffile, 'contiene', layer.GetFeatureCount(), 'geometría'

for feature in layer:
    geom = feature.GetGeometryRef()
    area = geom.Area()
    print 'El área del polígono es %.4f m2.' % (area)
    filegml.writelines(str(area))  # añade área al gml
    perimetro = geom.GetGeometryRef(0)
    print 'Total de vértices del polígono:', perimetro.GetPointCount()
    print 'Listado de coordenadas:'
    print 'id,x,y'

    filegml.writelines(cabecera2)  # añade texto tras área

    for i in range(0, perimetro.GetPointCount()):
        pt = perimetro.GetPoint(i)
        coordlist = [str(pt[0]), ' ', str(pt[1]), '\n']
        filegml.writelines(coordlist)  # añade listado de coordenadas X e Y
        print "%i,%.4f,%.4f" % (i, pt[0], pt[1])

filegml.writelines(fin)
dataSource = None
filegml.close()
