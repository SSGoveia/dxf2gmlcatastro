# -*- coding: utf-8 -*-.
import dxf2gmlcatastro

# carpeta de trabajo
path = '/home/pasoriano/Documentos/scriptqgis/'

# define archivos
dxf = 'parcelacad.dxf'
gml = 'catastrogml.gml'

#Define variables
dxffile = path + dxf
gmlfile = path + gml
src = '25830'

# Crea GML
dxf2gmlcatastro.crea_gml(dxffile, gmlfile, src)

#Añade capa GML a QGIS
layer = iface.addVectorLayer(gmlfile, "gmlcatastro", "ogr")