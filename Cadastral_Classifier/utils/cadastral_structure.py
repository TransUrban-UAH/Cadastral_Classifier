# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:31:08 2021

@author: by Nikolai Shurupov (Universidad de Alcalá de Henares)

@purpose: structured dictionaries to extract information from .CAT files, used 
          in the cadastral classifier QGIS plugin"""

#------------------------------------------------------------------------------

## ESPAÑOL

# Esta es una definicion de los diccionarios que conentran la estrucutra que se
# debe seguir a la hora de realizar la extraccion de la diferente informacion 
# que atañe a cada tipo de tabla. Para cada tipo de tabla que es posible generar,
# para cada columna que tendrá,  se define el punto de comienzo, la longitud,
# el tipo, una descripcion y el codigo interno.

## ENGLISH

# This is a definition of the dictionaries that will store the structure of the 
# extraction caracteristics that each table-type has to follow. Based on this,
# for every type of possible table, for the different columns to generate,
# a start position, length, type, description, and internal codification are
# declared. 

# link/enlace http://www.catastro.meh.es/documentos/formatos_intercambio/catastro_fin_cat_2006.pdf

#------------------------------------------------------------------------------

# generacion de la variable diccionario / dictionary creation
catstruct = {}

# 01 - Registro de cabecera
catstruct[1] = [
    [3, 1, 'X', 'tipo_entidad_generadora', "3_teg"],
    [4, 9, 'N', 'codigo_entidad_generadora', "4_ceg"],
    [13, 27, 'X', 'nombre_entidad_generadora', "13_neg"],
    [40, 8, 'N', 'fecha_generacion_fichero', "40_fgf"],
    [48, 6, 'N', 'hora_generacion_fichero', "48_hgf"],
    [54, 4, 'X', 'tipo_fichero', "54_tf"],
    [58, 39, 'X', 'descripcion_contenido_fichero', "58_dcf"],
    [97, 21, 'X', 'nombre_fichero', "97_nf"],
    [118, 3, 'N', 'codigo_entidad_destinataria', "118_ced"],
    [121, 8, 'N', 'fecha_inicio_periodo', "121_fip"],
    [129, 8, 'N', 'fecha_finalizacion_periodo', "129_ffp"]
]

# 11 - Registro de Finca
catstruct[11] = [
    [24, 2, 'N', 'codigo_delegacion_meh', '24_cd'],
    [26, 3, 'N', 'codigo_municipio_dgc', '26_cmc'],
    [29, 2, 'X', 'bienes_inmuebles_caracteristicas_especiales', '29_cn'],
    [31, 14, 'X', 'parcela_catastral', '31_pc'],
    [51, 2, 'N', 'codigo_provincia_ine', "51_cp"],
    [53, 25, 'X', 'nombre_provincia', "53_np"],
    [78, 3, 'N', 'codigo_municipio_dgc_2', "78_cmc"],
    [81, 3, 'N', 'codigo_municipio_ine', "81_cm"],
    [84, 40, 'X', 'nombre_municipio', "84_nm"],
    [124, 30, 'X', 'nombre_entidad_menor', "124_nem"],
    [154, 5, 'N', 'codigo_via_publica_dgc', "154_cv"],
    [159, 5, 'X', 'tipo_via', "159_tv"],
    [164, 25, 'X', 'nombre_via', "164_nv"],
    [189, 4, 'N', 'primer_numero_policia', "189_pnp"],
    [193, 1, 'X', 'primera_letra', "193_plp"],
    [194, 4, 'N', 'segundo_numero_policia', "194_snp"],
    [198, 1, 'X', 'segunda_letra', "198_slp"],
    [199, 5, 'N', 'kilometro_por_cien', "199_km"],
    [204, 4, 'X', 'bloque', "204_bl"],
    [216, 25, 'X', 'direccion_no_estructurada', "216_td"],
    [241, 5, 'N', 'codigo_postal', "241_dp"],
    [246, 2, 'X', 'distrito_municipal', "246_dm"],
    [248, 3, 'N', 'codigo_municipio_origen_caso_agregacion_dgc', "248_cma"],
    [251, 2, 'N', 'codigo_zona_concentracion', "251_czc"],
    [253, 3, 'N', 'codigo_poligono', "253_cpo"],
    [256, 5, 'N', 'codigo_parcela', "256_cpa"],
    [261, 5, 'X', 'codigo_paraje_dgc', "261_cpaj"],
    [266, 30, 'X', 'nombre_paraje', "266_npa"],
    [296, 10, 'N', 'superficie_finca_o_parcela_catastral_m2', "296_sup"],
    [306, 7, 'N', 'superficie_construida_total', "306_sct"],
    [313, 7, 'N', 'superficie_construida_sobre_rasante', "313_ssr"],
    [320, 7, 'N', 'superficie_construida_bajo_rasante', "320_sbr"],
    [327, 7, 'N', 'superficie_cubierta', "327_sc"],
    [334, 9, 'N', 'coordenada_x_por_cien', "334_xcen"],
    [343, 10, 'N', 'coordenada_y_por_cien', "343_ycen"],
    [582, 20, 'X', 'referencia_catastral_bice', "582_rc_bice"],
    [602, 65, 'X', 'denominacion_bice', "602_n_bice"],
    [667, 10, 'X', 'codigo_epsg', "667_srs"]
]

# 13 - Registro de Unidad Constructiva
catstruct[13] = [
    [24, 2, 'N', 'codigo_delegacion_meh', '24_cd'],
    [26, 3, 'N', 'codigo_municipio_dgc', '26_cmc'],
    [31, 14, 'X', 'parcela_catastral', '31_pc'],
    [45, 4, 'X', 'codigo_unidad_constructiva', "45_cuc"],
    [51, 2, 'N', 'codigo_provincia_ine', "51_cp"],
    [53, 25, 'X', 'nombre_provincia', "53_np"],
    [78, 3, 'N', 'codigo_municipio_dgc_2', "78_cmc"],
    [81, 3, 'N', 'codigo_municipio_ine', "81_cm"],
    [84, 40, 'X', 'nombre_municipio', "84_nm"],
    [124, 30, 'X', 'nombre_entidad_menor', "124_nem"],
    [154, 5, 'N', 'codigo_via_publica_dgc', "154_cv"],
    [159, 5, 'X', 'tipo_via', "159_tv"],
    [164, 25, 'X', 'nombre_via', "164_nv"],
    [189, 4, 'N', 'primer_numero_policia', "189_pnp"],
    [193, 1, 'X', 'primera_letra', "193_plp"],
    [194, 4, 'N', 'segundo_numero_policia', "194_snp"],
    [198, 1, 'X', 'segunda_letra', "198_slp"],
    [199, 5, 'N', 'kilometro_por_cien', "199_km"],
    [216, 25, 'X', 'direccion_no_estructurada', "216_td"],
    [296, 4, 'N', 'anyo_construccion', "296_ac"],    
    [300, 1, 'X', 'exactitud_anyo_construccion', "300_iacons"], 
    [301, 7, 'N', 'superficie_suelo_ocupado', "301_so"],
    [308, 5, 'N', 'longitud_fachada_cm', "308_lf"],
    [410, 4, 'X', 'codigo_unidad_constructiva_matriz', "410_cucm"]
]

# 14 - Registro de Construccion
catstruct[14] = [
    [24, 2, 'N', 'codigo_delegacion_meh', '24_cd'],
    [26, 3, 'N', 'codigo_municipio_dgc', '26_cmc'],
    [31, 14, 'X', 'parcela_catastral', '31_pc'],
    [45, 4, 'N', 'numero_orden_elemento_construccion', "45_noec"],
    [51, 4, 'X', 'numero_orden_bien_inmueble_fiscal ', "51_nobf"],
    [55, 4, 'X', 'codigo_unidad_constructiva_asociada', "55_cuc"],
    [59, 4, 'X', 'bloque', "59_bl"],
    [63, 2, 'X', 'escalera', "63_es"],
    [65, 3, 'X', 'planta', "65_pt"],
    [68, 3, 'X', 'puerta', "68_pu"],
    [71, 3, 'X', 'codigo_destino_dgc', "71_cd"],
    [74, 1, 'X', 'tipo_reforma_o_rehabilitacion', "74_tr"], 
    [75, 4, 'N', 'anyo_reforma', "75_ar"],
    [79, 4, 'N', 'anyo_antiguedad_efectiva_catastro', "79_aec"],
    [83, 1, 'X', 'indicador_local_interior', "83_ili"], # 'S', 'N'
    [84, 7, 'N', 'superficie_total_efectos_catastro_m2', "84_stl"],
    [91, 7, 'N', 'superficie_porches_y_terrazas_m2', "91_spt"],
    [98, 7, 'N', 'superficie_imputable_en_otras_plantas_m2', "98_sil"],
    [105, 5, 'X', 'tipologia_constructiva', "105_tip"],
    [112, 3, 'X', 'modalidad_reparto_elementos_comunes', "112_modl"]
]

# 15 - Registro de Inmueble
catstruct[15] = [
    [24, 2, 'N', 'codigo_delegacion_meh', "24_cd"],
    [26, 3, 'N', 'codigo_municipio_dgc', "26_cmc"],
    [29, 2, 'X', 'clase_bien_inmueble', "29_cn"],
    [31, 14, 'X', 'parcela_catastral', "31_pc"],
    [45, 4, 'N', 'numero_secuencia_en_parcela', "45_car"],
    [49, 1, 'X', 'primer_caracter_control', "49_cc1"],
    [50, 1, 'X', 'segundo_caracter_control', "50_cc2"],
    [51, 8, 'N', 'numero_fijo_bien_inmueble', "51_nfbi"],
    [59, 15, 'X', 'identificacion_inmueble_segun_ayuntamiento', "59_iia"],
    [74, 19, 'X', 'numero_finca_registral', "74_nfv"],
    [93, 2, 'N', 'codigo_provincia_ine', "93_cp"],
    [95, 25, 'X', 'nombre_provincia', "95_np"],
    [120, 3, 'N', 'codigo_municipio_dgc_2', "120_cmc"],
    [123, 3, 'N', 'codigo_municipio_ine', "123_cm"],
    [126, 40, 'X', 'nombre_municipio', "126_nm"],
    [166, 30, 'X', 'nombre_entidad_menor', "166_nem"],
    [196, 5, 'N', 'codigo_via_publica_dgc', "196_cv"],
    [201, 5, 'X', 'tipo_via', "201_tv"],
    [206, 25, 'X', 'nombre_via', "206_nv"],
    [231, 4, 'N', 'primer_numero_policia', "231_pnp"],
    [235, 1, 'X', 'primera_letra', "235_plp"],
    [236, 4, 'N', 'segundo_numero_policia', "236_snp"],
    [240, 1, 'X', 'segunda_letra', "240_slp"],
    [241, 5, 'N', 'kilometro_por_cien', "241_km"],
    [246, 4, 'X', 'bloque', "246_bl"],
    [250, 2, 'X', 'escalera', "250_es"],
    [252, 3, 'X', 'planta', "252_pt"],
    [255, 3, 'X', 'puerta', "255_pu"],
    [258, 25, 'X', 'direccion_no_estructurada', "258_td"],
    [283, 5, 'N', 'codigo_postal', "283_dp"],
    [288, 2, 'X', 'distrito_municipal', "288_dm"],
    [290, 3, 'N', 'codigo_municipio_origen_caso_agregacion_dgc', "290_cma"],
    [293, 2, 'N', 'codigo_zona_concentracion', "293_czc"],
    [295, 3, 'N', 'codigo_poligono', "295_cpo"],
    [298, 5, 'N', 'codigo_parcela', "298_cpa"],
    [303, 5, 'X', 'codigo_paraje_dgc', "303_cpaj"],
    [308, 30, 'X', 'nombre_paraje', "308_npa"],
    [368, 4, 'X', 'numero_orden_inmueble_en_escritura', "368_noe"],
    [372, 4, 'N', 'anyo_antiguedad_inmueble', "372_ant"],
    [428, 1, 'X', 'clave_uso', "428_grbice/coduso"], 
    [442, 10, 'N', 'superficie_construida_m2', "442_sfc"],
    [452, 10, 'N', 'superficie_asociada_m2', "452_sfs"],
    [462, 9, 'N', 'coeficiente_propiedad_en_cienmillonesimas_partes', "462_cpt"]
]

# 16 - Registro de reparto de elementos comunes
catstruct[16] = [
    [24, 2, 'N', 'codigo_delegacion_meh', "24_cd"],
    [26, 3, 'N', 'codigo_municipio_dgc', "26_cmc"],
    [31, 14, 'X', 'parcela_catastral', "31_pc"],
    [45, 4, 'N', 'numero_elemento', "45_ne"],
    [49, 2, 'X', 'calificacion_catastral_subparcela_abstracta', "49_ccsa"],
    [51, 4, 'N', 'numero_orden_segmento', "51_nos"]
    # Aqui hay un bloque que se repite hasta 15 veces, y que nos saltamos
]

# 17 - Registro de cultivos
catstruct[17] = [
    [24, 2, 'N', 'codigo_delegacion_meh', "24_cd"],
    [26, 3, 'N', 'codigo_municipio_dgc', "26_cmc"],
    [29, 2, 'X', 'naturaleza_suelo_ocupado', "29_cn"], 
    [31, 14, 'X', 'parcela_catastral', "31_pc"],
    [45, 4, 'X', 'codigo_subparcela', "45_cspr"],
    [51, 4, 'N', 'numero_orden_fiscal_en_parcela', "51_nobf"],
    [55, 1, 'X', 'tipo_subparcela', "55_tspr"],
    [56, 10, 'N', 'superficie_subparcela_m2', "56_ssp"],
    [66, 2, 'X', 'calificacion_catastral_o_clase_cultivo', "66_ccc"],
    [68, 40, 'X', 'denominacion_clase_cultivo', "68_dcc"],
    [108, 2, 'N', 'intensidad_productiva', "108_ip"],
    [127, 3, 'X', 'codigo_modalidad_reparto', "127_modl"] 
]

# 46 - Registro de situaciones finales de titularidad
catstruct[46] = [
    [24, 2, 'N', 'codigo_delegacion_meh', "24_cd"],
    [26, 3, 'N', 'codigo_municipio_dgc', "26_cmc"],
    [29, 2, 'X', 'naturaleza_suelo_ocupado', "29_cn"], 
    [31, 14, 'X', 'parcela_catastral', "31_pc"],
    [45, 4, 'X', 'codigo_subparcela', "45_cspr"],
    [49, 1, 'X', 'primer_carac_control', "49_pcc"],
    [50, 1, 'X', 'segundo_carac_control', "50_scc"],
    [51, 2, 'X', 'codigo_derecho', "51_cd"],
    [53, 5, 'N', 'porcentage_derecho', "53_pd"],
    [58, 3, 'N', 'ordinal_derecho', "58_od"],
    [61, 9, 'X', 'nif_titular', "61_nt"],
    [70, 60, 'X', 'nombre_titular', "71_nt"], 
    [130, 1, 'X', 'motivo_no_nif', "130_mnn"],
    [131, 2, 'N', 'codigo_provincia_ine', "131_cpi"],
    [133, 25, 'X', 'nombre_provincia', "133_np"],
    [158, 3, 'N', 'codigo_municipio_dgc', "158_cmc"],
    [161, 3, 'N', 'codigo_municipio_ine', "161_cm"],
    [164, 40, 'X', 'nombre_municipio', "164_nm"],
    [204, 30, 'X', 'nombre_entidad_menor', "204_nem"],
    [235, 5, 'N', 'codigo_via_publica_dgc', "235_cvpc"],
    [239, 5, 'X', 'tipo_via', "239_tv"],
    [244, 25, 'X', 'nombre_via', "244_nv"],
    [269, 4, 'N', 'primer_numero_policia', "269_pnp"],
    [273, 1, 'X', 'primera_letra', "273_pl"],
    [274, 4, 'N', 'segundo_numero_policia', "274_snp"],
    [278, 1, 'X', 'segunda_letra', "278_sl"],
    [279, 5, 'N', 'kilometro_por_cien', "279_km"],
    [284, 4, 'X', 'bloque', "284_bl"],
    [288, 2, 'X', 'escalera', "288_es"],
    [290, 3, 'X', 'planta', "290_pl"],
    [293, 3, 'X', 'puerta', "293_pu"],
    [296, 25, 'X', 'direccion_no_estructurada', "296_dne"],
    [321, 5, 'N', 'codigo_postal', "321_cp"],
    [326, 5, 'N', 'apartado_correos', "326_ac"],
    [331, 9, 'X', 'nif_conyuge', "331_nc"],
    [340, 9, 'X', 'nif_cb', "340_ ncb"],
    [349, 20, 'X', 'complemento_titularidad', "349_ct"]
]

# 47 - Registro de comunidad de bienes formalmente constituida presente en una situación final
catstruct[47] = [
    [24, 2, 'N', 'codigo_delegacion_meh', "24_cd"],
    [26, 3, 'N', 'codigo_municipio_dgc', "26_cmc"],
    [29, 2, 'X', 'naturaleza_suelo_ocupado', "29_cn"], 
    [31, 14, 'X', 'parcela_catastral', "31_pc"],
    [45, 4, 'X', 'codigo_subparcela', "45_cspr"],
    [49, 1, 'X', 'primer_carac_control', "49_pcc"],
    [50, 1, 'X', 'segundo_carac_control', "50_scc"],
    [51, 9, 'X', 'nif_comunidad_bienes', "51_ncb"],
    [60, 60, 'X', 'denominacion_razon_socil', "60_drc"],
    [120, 2, 'N', 'codigo_provincia_ine', "120_cp"],
    [122, 25, 'X', 'nombre_provincia', "np"],
    [147, 3, 'N', 'codigo_municipio_dgc', "147_cmc"],
    [150, 3, 'N', 'codigo_municipio_ine', "150_cp"],
    [153, 40, 'X', 'nombre_municipio', "153_nm"],
    [193, 30, 'X', 'nombre_entidad_menor', "193_nem"],
    [223, 5, 'N', 'codigo_via_publica_dgc', "cvpc"],
    [228, 5, 'X', 'tipo_via', "228_tv"],
    [233, 25, 'X', 'nombre_via', "233_nv"],
    [258, 4, 'N', 'primer_numero_policia', "258_pnp"],
    [262, 1, 'X', 'primera_letra', "262_pl"],
    [263, 4, 'N', 'segundo_numero_policia', "263_snp"],
    [267, 1, 'X', 'segunda_letra', "267_sl"],
    [268, 5, 'N', 'kilometro_por_cien', "268_km"],
    [273, 4, 'X', 'bloque', "273_bl"],
    [277, 2, 'X', 'escalera', "277_es"],
    [279, 3, 'X', 'planta', "279_pl"],
    [282, 3, 'X', 'puerta', "282_pu"],
    [285, 25, 'X', 'direccion_no_estructurada', "285_dne"],
    [310, 5, 'N', 'codigo_postal', "310_cp"],
    [315, 5, 'N', 'apartado_correos', "315_ac"]
]

# 90 - Registro de cola
catstruct[90] = [
    [10, 7, 'N', 'numero_registros_tipo_11', "10_nrt_11"],
    [24, 7, 'N', 'numero_registros_tipo_13', "24_nrt_13"],    
    [31, 7, 'N', 'numero_registros_tipo_14', "31_nrt_14"],
    [38, 7, 'N', 'numero_registros_tipo_15', "38_nrt_15"],
    [45, 7, 'N', 'numero_registros_tipo_16', "45_nrt_16"],
    [52, 7, 'N', 'numero_registros_tipo_17', "52_nrt_17"],
    [59, 7, 'N', 'numero_registros_tipo_46', "59_nrt_46"],
    [66, 7, 'N', 'numero_registros_tipo_47', "66_nrt_47"]
]

