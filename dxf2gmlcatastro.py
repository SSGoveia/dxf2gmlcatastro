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

Ejemplos
python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml
python dxfgmlcatastro.py carpetadxf/archivocad.dxf carpetagml/gmlsalida.gml
python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml 25831

"""

import sys
try:
    from osgeo import ogr, osr, gdal
	
except:
    sys.exit('ERROR: Parece que no están instalados los GDAL/OGR')

import os.path


def crea_gml(dxffile):
	""" Primera línea de documentación define la función
	
	Siguientes líneas completan el resto de la documentación y declaran los inputs y outputs.
	Genera el archivo GML según el estándar de catastro y añade la primera parte
	del texto	
	"""
	# Accede mediante GDAL al archivo DXF
	driver = ogr.GetDriverByName('DXF')
	data_source = driver.Open(dxffile, 0)
	layer = data_source.GetLayer()

	# print('Archivo CAD',sys.argv[1])
	# print('Archivo GML',sys.argv[2])
	# print('Total de arg:',len(sys.argv))

	with open(sys.argv[2], 'w') as filegml:
	    filegml.writelines(PLANTILLA_1)

	    print("El archivo %s contiene %i geometría." % (dxffile, 
			  layer.GetFeatureCount()))

	    
	    for feature in layer:
	        geom = feature.GetGeometryRef()
			
	        area = geom.Area()
	        print('El área del polígono es %.4f m2.' % (area))
			
	        filegml.writelines(str(area))  # Añade área al GML
			
	        perimetro = geom.GetGeometryRef(0)
	        print('Total de vértices del polígono: %s' % (perimetro.GetPointCount()))
	        print('Listado de coordenadas:\nid,x,y')

	        filegml.writelines(PLANTILLA_2)  # Añade texto tras área

	        src = 'SCR_25830' #src por defecto

	        if len(sys.argv) == 4: # Si existe el argumento SRC (25829 o 2531) modifica variable src
	        	src = 'SCR_%s' % (sys.argv[3])
	        	filegml.writelines(src)
        	else:
        		filegml.writelines(src)

	        for i in range(0, perimetro.GetPointCount()):
	            pt = perimetro.GetPoint(i)
	            coordlist = [str(pt[0]), ' ', str(pt[1]), '\n']
				
	            filegml.writelines(coordlist)  # Añade listado de coordenadas X e Y
				
	            print("%i,%.4f,%.4f" % (i, pt[0], pt[1]))

	    filegml.writelines(PLANTILLA_3)


if __name__ == '__main__':
	# Comprueba que plantillacatastro existe en el mismo directorio
	try:
		from plantillacatastro import *

	except:
		sys.exit('ERROR: No se encuentra la plantilla "plantillacatastro"')

	# Comprueba que parcelacad.dxf existe en el mismo directorio
	#dxffile = "parcelacad.dxf"
	
	# usa el primer argumento para localizar el archivo DXF
	dxffile = sys.argv[1]

	# if os.path.isfile(dxffile):
	# 	print("Archivo %s existente." % (dxffile))
		
	# else:
	# 	print("No existe el fichero %s. Revise la ruta y el nombre del DXF." % (dxffile))

	# 	sys.exit()


	crea_gml(dxffile)
