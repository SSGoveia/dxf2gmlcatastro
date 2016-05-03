#!/usr/bin/env python
# -*- coding: utf-8 -*-

SRC_DICT = ['25828', '25829', '25830', '25831']

PLANTILLA_1 = """<?xml version="1.0" encoding="utf-8"?>
<!--Parcela Catastral para entregar a la D.G. del Catastro.-->
<gml:FeatureCollection xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:gmd="http://www.isotc211.org/2005/gmd" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:cp="urn:x-inspire:specification:gmlas:CadastralParcels:3.0" xmlns:base="urn:x-inspire:specification:gmlas:BaseTypes:3.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:x-inspire:specification:gmlas:CadastralParcels:3.0 http://inspire.ec.europa.eu/schemas/cp/3.0/CadastralParcels.xsd" gml:id="ES.LOCAL.1">
   <gml:featureMember>
      <cp:CadastralParcel gml:id="ES.LOCAL.1A">
<!-- Superficie de la parcela en metros cuadrados. Tiene que coincidir con la calculada con las coordenadas.-->
         <cp:areaValue uom="m2">"""

PLANTILLA_2 = """</cp:areaValue>
         <cp:beginLifespanVersion xsi:nil="true" nilReason="other:unpopulated"></cp:beginLifespanVersion>
<!-- Geometria en formato GML       -->
         <cp:geometry><!-- srs Name codigo del sistema de referencia en el que se dan las coordenadas, que debe coincidir con el de la cartografia catastral -->
           <gml:MultiSurface gml:id="MultiSurface_ES.LOCAL.1A" srsName="urn:ogc:def:crs:EPSG::{src}">
             <gml:surfaceMember>
               <gml:Surface gml:id="Surface_ES.LOCAL.1A" srsName="urn:ogc:def:crs:EPSG::{src}">
                  <gml:patches>
                    <gml:PolygonPatch>
                      <gml:exterior>
                        <gml:LinearRing>
<!-- Lista de coordenadas separadas por espacios o en lineas diferentes    -->
                          <gml:posList srsDimension="2">
"""

PLANTILLA_3 = """                          </gml:posList>
                        </gml:LinearRing>
                      </gml:exterior>
                    </gml:PolygonPatch>
                  </gml:patches>
                </gml:Surface>
              </gml:surfaceMember>
            </gml:MultiSurface>
         </cp:geometry>
         <cp:inspireId>
<!-- Identificativo local de la parcela. Solo puede tener letras y numeros. Se recomienda (pero no es necesario) poner siempre un digito de control, por ejemplo utilizando el algoritmo del NIF.-->
           <base:Identifier>
             <base:localId>1A</base:localId>
             <base:namespace>ES.LOCAL</base:namespace>
           </base:Identifier>
         </cp:inspireId>
         <cp:label/>
<!--Siempre en blanco, ya que todavia no ha sido dada de alta en las bases de datos catastrales.-->
         <cp:nationalCadastralReference/>
      </cp:CadastralParcel>
   </gml:featureMember>
<!-- Si se desea entregar varias parcelas en un mismo fichero, se pondra un nuevo featureMember para cada parcela -->
</gml:FeatureCollection>"""
