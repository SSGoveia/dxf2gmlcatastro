#!/usr/bin/env python
# -*- coding: utf-8 -*-

# >> Anotaciones en comentarios y al final del archivo

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

Ejemplos:
python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml
python dxfgmlcatastro.py carpetadxf/archivocad.dxf carpetagml/gmlsalida.gml
python dxfgmlcatastro.py archivocad.dxf gmlsalida.gml 25831

"""

import sys
try:
	from osgeo import ogr, osr, gdal
	
except ImportError:     # Capturada excepción al importar
	sys.exit('ERROR: Parece que no están instalados los GDAL/OGR')

import os.path


def crea_gml(dxf_origen_file, gml_salida_file, src):
	""" Primera línea de documentación define la función
	
	Siguientes líneas completan el resto de la documentación y declaran los inputs y outputs.
	Genera el archivo GML según el estándar de catastro y añade la primera parte
	del texto	
	"""
	# Accede mediante GDAL al archivo DXF

	driver = ogr.GetDriverByName('DXF')
	data_source = driver.Open(dxf_origen_file, 0)
	layer = data_source.GetLayer()


	print('Archivo GML de salida: ',sys.argv[2])
	print('Código EPSG seleccionado: ',sys.argv[3], '\n')
	

	with open(gml_salida_file, 'w') as filegml:

		filegml.writelines(PLANTILLA_1)

		print("El archivo {} contiene {} geometría.".format(dxf_origen_file, layer.GetFeatureCount()))
		# Te recomendaría usar siempre el formato de str con ''.format(), es mucho más sencillo de usar!

		for feature in layer:
			geom = feature.GetGeometryRef()
			
			area = geom.Area()
			print('El área del polígono es %.4f m2.' % (area))
			
			filegml.writelines(str(area))  # Añade área al GML
			
			perimetro = geom.GetGeometryRef(0)
			print('Total de vértices del polígono: %s' % (perimetro.GetPointCount()))
			print('Listado de coordenadas:\nid,x,y')

			filegml.writelines(PLANTILLA_2)  # Añade texto tras área

			
			filegml.writelines(src_dict[sys.argv[3]]) # Añade texto SRC selecionado

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

	
	if len(sys.argv)<4: # Comprueban si están todos los argumentos necesarios
		print('Falta algunos de los argumentos (archivo dxf, archivo gml y/o código SRC.)')
		
		sys.exit()

	dxf_origen_file = sys.argv[1] # Usa el primer argumento para localizar el archivo DXF
	gml_salida_file = sys.argv[2] # Usa el segundo argumento para crear el archivo GML
	src = sys.argv[3] # Usa el tercer argumento para definir el SRC


	if os.path.isfile(dxf_origen_file): # Comprueba que el archivo DXF existe
		print('\nArchivo CAD de entrada: ',sys.argv[1])
		
	else:
		print("No existe el fichero %s. Revise la ruta y el nombre del DXF." % (dxf_origen_file))

		sys.exit()

	src_dict = {'25829': SRC_25829, '25830': SRC_25830, '25831': SRC_25831}

	src = src_dict.get(sys.argv[3])

	if not src: # compruba que el SRC esté en el diccionario
		print('El SRC indicado es incorrecto. Los SRC permitidos son 25829, 25830, 25831')

		sys.exit()


	crea_gml(dxf_origen_file, gml_salida_file, src)
