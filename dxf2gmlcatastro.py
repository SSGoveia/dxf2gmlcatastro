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
	- python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml
	- python dxfgmlcatastro.py carpetadxf/archivocad.dxf carpetagml/gmlsalida.gml
	- python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml 25831

"""
import sys
import os.path
try:
	from osgeo import ogr, osr, gdal
	
except ImportError:     # Capturada excepción al importar
	sys.exit('ERROR: Paquetes GDAL/OGR no encontrados. Compruebe que están instalados correctamente')


def crea_gml(dxf_origen_file, gml_salida_file, src):
	""" Generar un archivo GML según la geometría de origen y el estándar de catastro elegido

	Transforma la información de la geometría del archivo DXF al estándar de catastro elegido entre SRC_25829,
	SRC_25830 y SRC_25831. Devuelve archivo en formato GML en el mismo directorio con dicha información

	:dxf_origen_file:   Dirección del archivo en formato DXF con la geometría de origen
	:gml_salida_file:   Dirección del archivo en formato GML a sobreescribir con el resultado
	:src:               Estándar de catastro elegido
	"""
	# Accede mediante GDAL al archivo DXF
	driver = ogr.GetDriverByName('DXF')
	data_source = driver.Open(dxf_origen_file, 0)
	layer = data_source.GetLayer()

	print('Archivo GML de salida: {}'.format(sys.argv[2]))
	print('Código EPSG seleccionado: {}\n'.format(sys.argv[3]))

	with open(gml_salida_file, 'w') as filegml:
		filegml.writelines(PLANTILLA_1)

		print('El archivo {} contiene {} geometría.'.format(dxf_origen_file, layer.GetFeatureCount()))

		for feature in layer:
			geom = feature.GetGeometryRef()
			
			area = geom.Area()
			print('El área del polígono es {:.4f} m2.'.format(area))
			
			filegml.writelines(str(area))       # Añade el área al GML
			
			perimetro = geom.GetGeometryRef(0)

			print('Total de vértices del polígono: {}'.format(perimetro.GetPointCount()))
			print('Listado de coordenadas:\nid,x,y')

			filegml.writelines(PLANTILLA_2)                 # Añade XML tras área
			filegml.writelines(SRC_DICT[sys.argv[3]])       # Añade XML SRC selecionado

			for i in range(0, perimetro.GetPointCount()):
				pt = perimetro.GetPoint(i)
				coordlist = [str(pt[0]), ' ', str(pt[1]), '\n']
				
				filegml.writelines(coordlist)       # Añade listado de coordenadas X e Y
				
				print('{},{:.4f},{:.4f}'.format(i, pt[0], pt[1]))

		filegml.writelines(PLANTILLA_3)


if __name__ == '__main__':
	# Comprueba que plantillacatastro existe en el directorio actual
	try:
		from plantillacatastro import *

	except ImportError:
		sys.exit('ERROR: No se encuentra el script plantilla "plantillacatastro" en el directorio')

	if len(sys.argv) < 4:
		sys.exit('ERROR: Algunos argumentos no indicados: archivo dxf, archivo gml y/o código SRC.')

	dxf_origen_file = sys.argv[1]       # Archivo DXF de origen
	gml_salida_file = sys.argv[2]       # Archivo GML de salida
	src = sys.argv[3]                   # Formato SRC

	if os.path.isfile(dxf_origen_file):     # Comprueba que el archivo DXF existe
		print('Archivo CAD de entrada: {}'.format(sys.argv[1]))
		
	else:
		sys.exit('ERROR: No existe el fichero DXF {}. Revise la ruta y el nombre de archivo.'.format(dxf_origen_file))

	SRC_DICT = {'25829': SRC_25829,
	            '25830': SRC_25830,
	            '25831': SRC_25831}     # Los dict en multilínea son algo más legibles. En mayus. por ser const. global

	src = SRC_DICT.get(sys.argv[3])
	if not src:
		sys.exit('ERROR: SRC indicado incorrecto. SRC permitidos: 25829, 25830, 25831')

	crea_gml(dxf_origen_file, gml_salida_file, src)
