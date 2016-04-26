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
	- Es necesario tener instalado Python y el módulo GDAL

Ejemplos:
	- python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml 25831

"""
import sys
import os.path
try:
	from osgeo import ogr, osr, gdal
	
except ImportError:     # Capturada excepción al importar
	sys.exit('ERROR: Paquetes GDAL/OGR no encontrados. Compruebe que están instalados correctamente')

from plantillacatastro import *

SRC_DICT = {'25828': SRC_25828,
			'25829': SRC_25829,
            '25830': SRC_25830,
            '25831': SRC_25831}
# 03 lo tengo que añadir aquí porque si no no encontraba la constantes SRC_DIST
# NameError: name 'SRC_DICT' is not defined

def crea_gml(dxf_origen_file, gml_salida_file, src):
	""" Transforma la información de la geometría de un archivo DXF al estándar de Catastro en formato GML.

	:dxf_origen_file:   Dirección del archivo en formato DXF con la geometría de origen
	:gml_salida_file:   Dirección del archivo en formato GML a sobreescribir con el resultado
	:src:               Sistema de Refencia de Coordendas del DXF. Según cógigos  EPSG
	"""
	# Accede mediante GDAL al archivo DXF
	driver = ogr.GetDriverByName('DXF')
	data_source = driver.Open(dxf_origen_file, 0)
	layer = data_source.GetLayer()

	# print('Archivo GML de salida: {}'.format(sys.argv[2]))
	# print('Código EPSG seleccionado: {}\n'.format(sys.argv[3]))

	##  01 me da un IndexError: list index out of range


	with open(gml_salida_file, 'w') as filegml:
		filegml.writelines(PLANTILLA_1) 
		# 02 he tenido que añadir el from plantillacatastro import * antes (lin 32)
		# porque no encontraba las constantes
		print('El archivo {} contiene {} geometría.'.format(dxf_origen_file, layer.GetFeatureCount()))

		for feature in layer:
			geom = feature.GetGeometryRef()
			
			area = geom.Area()
			print('El área del polígono es {:.4f} m2.'.format(area))
			
			filegml.writelines(str(area))       # Añade el área al GML
			
			perimetro = geom.GetGeometryRef(0)

			print('\nTotal de vértices del polígono: {}'.format(perimetro.GetPointCount()))
			print('Listado de coordenadas de los vértices:\nid,x,y')

			filegml.writelines(PLANTILLA_2)                 # Añade XML tras área
			filegml.writelines(SRC_DICT[sys.argv[3]])       # Añade XML SRC selecionado

			## 04 AQUÍ ME HE QUEDADO!!!!!
			## ME VUELVE A SALIR IndexError: list index out of range
			## PERO NO SE ME OCURRE COMO ARREGLARLO
			
			for i in range(0, perimetro.GetPointCount()):
				pt = perimetro.GetPoint(i)
				coordlist = [str(pt[0]), ' ', str(pt[1]), '\n']
				
				filegml.writelines(coordlist)       # Añade listado de coordenadas X e Y al GML
				
				print('{},{:.4f},{:.4f}'.format(i, pt[0], pt[1]))

		filegml.writelines(PLANTILLA_3) # Añade XML


if __name__ == '__main__':
	# Comprueba que plantillacatastro.py existe en el directorio actual
	try:
		from plantillacatastro import *

	except ImportError:
		sys.exit('ERROR: No se encuentra el script plantilla "plantillacatastro" en el directorio')

	if len(sys.argv) < 4:
		sys.exit('ERROR: Falta alguno de los argumentos obligatorio: archivo dxf, archivo gml y/o código SRC.')

	dxf_origen_file = sys.argv[1]       # Archivo DXF de origen
	gml_salida_file = sys.argv[2]       # Archivo GML de salida
	src = sys.argv[3]                   # Formato SRC

	if os.path.isfile(dxf_origen_file):     # Comprueba que el archivo DXF existe
		print('Archivo CAD de entrada: {}'.format(sys.argv[1]))
		
	else:
		sys.exit('ERROR: No existe el fichero DXF {}. Revise la ruta y el nombre de archivo.'.format(dxf_origen_file))

	# SRC_DICT = {'25828': SRC_25828,
	# 			'25829': SRC_25829,
	#             '25830': SRC_25830,
	#             '25831': SRC_25831}

	src = SRC_DICT.get(sys.argv[3])
	if not src:
		sys.exit('ERROR: SRC indicado incorrecto. SRC permitidos: 25828, 25829, 25830 o 25831')

	crea_gml(dxf_origen_file, gml_salida_file, src)
