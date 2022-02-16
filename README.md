![plugin icon](https://github.com/TransUrban-UAH/Cadastral_Classifier/blob/main/icon.jpg)# Cadastral Classifier: a QGIS plugin to classify Spamish municipalities using cadastral information 

## Summary
Cadastral Classifier (CC) is a plugin to classify urban parcels of any Spanish municipality (excluding Navarra and País Vasco) using cadastral information (obtainable via official channels). It has been developed under version 3.16 of QGIS, that includes a Python 3.7 version and a QT Designer version, and it supports version 3.0 or higher. The main objective is to offer, to a different user profiles, the possibility of carrying out classifications of spanish municipalities at parcel level, by implementing 3 types of classifications, that increase in complexity and depths on their analysis. This development has been carried out within the framework of the SIM4PLAN project, financed by the R+D+i Projects Proof of Concept 2021 from the Ministry of Science and Innovation of the Government of Spain and NextGenerationEU of the European Union, with reference PDC2021-121568-C21, as well as the grant “Stimulus to Excellence for Permanent University Professors” with reference EPU-INV/2020/009 from the UAH and the Community of Madrid, granted to Dr. Francisco Aguilera Benavente. Both sources of funding have allowed the Cadastral Classifier plugin to be made available to users free of charge.

## Developer team
Nikolai Shurupov, Ramón Molinero Parejo, Francisco Aguilera, Victor Rodríguez Espinosa and Ricardo Gascuñana Duro

## Installation
To use this tool it is needed to download it, preferably from the official channels of QGIS, using the plugin manager of the QGIS program itselfs, introducing "Cadastral Classifier" in the search engine. Alternatively, it is possible to download it from the GitHub repository, and add the file to the directory where the rest of the QGIS plugins are saved. This path is usually: `*\QGIS\QGIS3\profiles\default\python\plugins`

## Main files
* `cadastral_classifier.py`: this is the main function script, that contains the code that performs all the processes
* `cadastral_classifier_dialog_base.ui`: this is the file that contains the user interface
* `clasif`: folder that contains CSV files that define each of the classification properties
* `diagrams`: folder that contains the images of the diagrams related to the main proceses of the tool
* `utils`: folder that contains the different modules that the main function requires. This contains the following files:
  - `cadastral_structure.py`: this script contain the structured dictionaries to extract information from CAT files to table-type format (CSV)
  - `shp_utils.py`: script that contains different methods to process Shapefile files
  - `table_type_generator.py`: script that use the cadastral structure to generate the table-types
  - `use_definer.py`: script that stores the different methods of defining the use of a parcel
  - `palette_generator.py`: script that generate a palette to be used in the map visualization of the results

---

# Clasificador Catastral: plugin de QGIS para la clasificación parcelaria de municipios españoles utilizando información catastral ![icono plugin](https://github.com/TransUrban-UAH/Cadastral_Classifier/blob/main/icon.jpg)

## Resumen
Clasificador Catastral (CC) es un complemento para la clasificación del parcelario de cualquier municipio español (excluyendo Navarra y País Vasco) utilizando la información de la Dirección General del Catastro. Ha sido desarrollado bajo la versión 3.16 de QGIS, que incluye la versión 3.7 de Python y un módulo de QT Designer, y soporta la versión 3.0 o superior. El objetivo principal es ofrecer, a diferentes perfiles de usuarios, la posibilidad de realizar clasificaciones de los municipios español a nivel de parcela, mediante 3 tipos de clasificaciones que presentan distintos niveles de complejidad y profundidad en sus analisis. Este desarrollo ha sido realizado en el marco del proyecto SIM4PLAN financiado por la convocatoria Proyectos I+D+i Pruebas de Concepto 2021 del Ministerio de Ciencia e Innovación del Gobierno de España y  NextGenerationEU de la Unión Europea, con referencia PDC2021-121568-C21, así como gracias a la ayuda “Estímulo a la Excelencia para Profesores Universitarios Permanentes” con referencia EPU-INV/2020/009 de la UAH y la Comunidad de Madrid, concedida al Dr. Francisco Aguilera Benavente. Ambas fuentes de financiación han permitido que la herramienta Clasificador catastral 1.0  sea puesta a disposición de los usuarios de forma gratuita.

## Instalación
Para utilizar esta herramienta hay que descargarla, preferiblemente desde los canales oficiales de QGIS, utilizando el gestor de complementos del programa QGIS, introduciendo "Cadastral Classifier" en el motor de búsqueda. Alternativamente puede descargarlo desde el repositorio de GitHub y añadir la carpeta al directorio en el que tenga guardados el resto de complementos de QGIS. Esta ruta normalmente es la siguiente: `*\QGIS\QGIS3\profiles\default\python\plugins`

## Equipo desarrollador
Nikolai Shurupov, Ramón Molinero Parejo, Francisco Aguilera, Victor Rodríguez Espinosa y Ricardo Gascuñana Duro

## Archivos principales
* `cadastral_classifier.py`: este script contiene las funciones principales que ejecutan todos los procesos necesarios
* `cadastral_classifier_dialog_base.ui`: archivo que contiene la interfaz de usuario (GUI) de la herramienta
* `clasif`: carpeta que contiene los diferentes archivos CSV que definen las propiedades de cada tipo de clasificación
* `diagrams`: carpeta que contiene las imágenes de los diagramas de cada uno de los procesos principales de la herramienta
* `utils`: carpeta que contiene los diferentes módulos que el script principal utiliza. Esta contiene los siguientes archivos:
  - `cadastral_structure.py`:script que contiene los diccionarios con las estructuras de las diferentes tablas tipo utilizadas por la DGC
  - `shp_utils.py`: script que contiene diferentes métodos para gestionar los archivos Shapefile
  - `table_type_generator.py`: script que se encarga de utilizar la la estructura de tablas tipos catastrales para generarlas en formato CSV
  - `use_definer.py`: script que define los distintos métodos de definir la clase (uso) de una parcela en función del tipo de clasificación
  - `palette_generator.py`: script que genera una paleta de color para ser utilizada a la hora de mostrar los resultados en el mapa
