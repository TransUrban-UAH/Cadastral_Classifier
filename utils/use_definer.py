# -*- coding: utf-8 -*-
"""
Created on Wed Oct 2 17:21:21 2021

@author: by Nikolai Shurupov (Universidad de Alcalá de Henares)

@purpose: module of use definer of a cadastral parcel for cadastral classifier
          QGIS plugin"""
          
#------------------------------------------------------------------------------

def use_definer_basic (f, d_feature_values, lv_s_names, ls_selected, variables):
    ''' Defines the use of a parcel following simple method, using the parcel
    characteristics, that are defined by different variables

    :param f: QGIS feature of the object (row, single spatial parcel)
    :type feature: QGIS feature class
    
    :param d_feature_values: dictionary of the percentages that each use has 
                             on that parcel
    :type dictionary: int
    
    :param lv_s_names: list with the uses that has more that 0 amount of developed
                      area on that parcel, sorted from maximum to minimum
    :type list: str
    
    :param ls_selected: list of the uses that used selected to add to the analysis
    :type list: str
    
    :param variables: list of different variables, that this function doesn't use
    :type list: many formats
    
    :output use of the parcel
    :type text: str
    '''
    
    # if there is any use in the list (which indicates that it has more than
    # 0m2 developed)
    if len(lv_s_names) > 0:
        
        # if the parcel has any residential use developed
        if any(y in lv_s_names for y in ["RES"]):
            
            # check if its value is greater than 25%
            if d_feature_values["RES"] > 25:
                
                # if it is, and used selected residential to be on the analysis
                # gives it the residential use, ignoring any othe use that could
                # be greater that the residential one
                if "RES" in ls_selected:
                    use = "RES"
            
                else:
                    use = "OTROS"
            # if its not, follow the simple rule, gives the use with the highest
            # percentage
            else:
                if lv_s_names[0] in ls_selected:
                    use = lv_s_names[0]
                else:
                    use = "OTROS"
                    
        # define its use as the one with the most percentage
        else:  
            if lv_s_names[0] in ls_selected:
                use = lv_s_names[0]
            else:
                    use = "OTROS"
    return use

###############################################################################
#------------------------------------------------------------------------------
    
def use_definer_interm (f, d_feature_values, lv_s_names, ls_selected, variables):
    ''' Defines the use of a parcel following intermediate method, using the parcel
    characteristics, that are defined by different variables

    :param f: QGIS feature of the object (row, single spatial parcel)
    :type feature: QGIS feature class
    
    :param d_feature_values: dictionary of the percentages that each use has 
                             on that parcel
    :type dictionary: int
    
    :param lv_s_names: list with the uses that has more that 0 amount of developed
                      area on that parcel, sorted from maximum to minimum
    :type list: str
    
    :param ls_selected: list of the uses that used selected to add to the analysis
    :type list: str
    
    :param variables: list of different variables, gets the mixed values on 
                      dictionary format, the lists of the conglomerates to 
                      difine more precisely the pure uses and the columns that 
                      the shapefile has
                      
    :type list: many formats
    
    :output use of the parcel
    :type text: str
    '''
    
    # get the different auxiliary information
    d_mixed = variables[0]
    list_conglomerate_resi_uni = variables[1]
    list_conglomerate_resi_plu = variables[2]
    columns = variables[3]
    
    # if there is any use that has more than 0m2 developed
    if len(lv_s_names) > 0:
        
        # check if the parcel has any use that is susceptible to be mixed
        if any(y in lv_s_names for y in d_mixed.keys()):
            
            # define use variable with none value to evaluate it later
            use = None 
            
            # for the industrial just checks that the percentage is more than 
            # the selected one. If its not, set the use as mixed
            if "IND" in d_mixed.keys():
                
                ind_percentage = d_feature_values["IND"]
                
                if ind_percentage >= d_mixed["IND"]:
                    use = "IND"
            
                elif (ind_percentage < d_mixed["IND"]) and (ind_percentage >= 20):
                        
                    use = "IND_MX"
                    
            #------------------------------------------------------------------
            
            # for the residentials, check if the conglomerates, not jus the 
            # residential, sum up to 100. If they not, follow same rule as 
            # previously with the industrial one: check the percentage, and 
            # if its greater than the selected one, it will be pure residential
            # and if its not, set its use to mixed
            if "RES_UNI" in d_mixed.keys():
                
                res_uni_percentage = d_feature_values["RES_UNI"]
                
                if res_uni_percentage >= d_mixed["RES_UNI"]:
                    use = "RES_UNI"                                
                    
                elif (res_uni_percentage < d_mixed["RES_UNI"]) and\
                    (res_uni_percentage >= 20):
                        
                    conglomerate_area = 0
                    
                    for e in list_conglomerate_resi_uni:
                        if e in columns:
                            if f[e] > 0:
                                conglomerate_area += f[e]
                        
                    if conglomerate_area == f["A_TOT_EDIF"]:
                        use = "RES_UNI"
                        
                    elif res_uni_percentage > d_feature_values["IND"] and\
                        res_uni_percentage > d_feature_values["RES_PLU"]:
                            
                        use = "RES_UNI_MX"
                        
            #------------------------------------------------------------------
            
            # same as unifamily, but with plurifamily conglomerates
            if "RES_PLU" in d_mixed.keys():
                
                res_plu_percentage = d_feature_values["RES_PLU"]

                if res_plu_percentage >= d_mixed["RES_PLU"]:
                    use = "RES_PLU"
                
                elif (res_plu_percentage < d_mixed["RES_PLU"]) and\
                    (res_plu_percentage >= 20):
                        
                    conglomerate_area = 0
                    
                    for e in list_conglomerate_resi_plu:
                        if e in columns:
                            
                            if f[e] > 0:
                                conglomerate_area += f[e]
                        
                    if conglomerate_area == f["A_TOT_EDIF"]:
                        use = "RES_PLU"
                        
                    elif res_plu_percentage >= d_feature_values["IND"] and\
                        res_plu_percentage >= d_feature_values["RES_UNI"]:
                            
                        use = "RES_PLU_MX"
            #------------------------------------------------------------------
            
            # if not a single use has been define at this stage, it means parcel
            # developed area related to mixed uses moves under 20%. In that case
            # use standard simple method and define with the highes percentage
            if not use:
                if lv_s_names[0] in ls_selected:
                        use = lv_s_names[0]
                        
                else:
                    use = "OTROS"
                    
        #----------------------------------------------------------------------
        
        # any other use follow basic rules: geve it the one with the most
        # percentage
        elif lv_s_names[0] in ls_selected:
                use = lv_s_names[0]
                
        else:
            use = "OTROS"

    return use

###############################################################################
#------------------------------------------------------------------------------
    
def use_definer_advanced (f, d_feature_values, lv_s_names, ls_selected, variables):  
    ''' Defines the use of a parcel following advanced method, using the parcel
    characteristics, that are defined by different variables

    :param f: QGIS feature of the object (row, single spatial parcel)
    :type feature: QGIS feature class
    
    :param d_feature_values: dictionary of the percentages that each use has 
                             on that parcel
    :type dictionary: int
    
    :param lv_s_names: list with the uses that has more that 0 amount of developed
                      area on that parcel, sorted from maximum to minimum
    :type list: str
    
    :param ls_selected: list of the uses that used selected to add to the analysis
    :type list: str
    
    :param variables: list of different variables, gets the mixed values on 
                      dictionary format
    
    :output use of the parcel
    :type text: str
    '''
    
    # get the mixed values (pures and mixed establishment)
    d_mixed = variables[0]
             
    # if there is any...
    if len(lv_s_names) > 0:
        
        # check if there is any that is declared with a mixed variant
        if any(y in lv_s_names for y in d_mixed.keys()):
            
            # create variables to evaluate the mixed uses ranks 
            rank_names = []
            rank_values = []
            pure_use = False
            
            # iterate ovet the mixed possibilities
            for mixed in d_mixed.keys():
                
                # if its greater, straight to 'pure' variant
                if d_feature_values[mixed] >= d_mixed[mixed]:
                                                    
                    use = mixed                                
                    pure_use = True
                
                # if its not, append to the rank lists, so in case there is 
                # multiple mixed posibilities, the higher one is selected
                elif d_feature_values[mixed] < d_mixed[mixed] and\
                    d_feature_values[mixed] > 0:
                    
                    rank_names.append(mixed)
                    rank_values.append(d_feature_values[mixed])
            # if there is 'competition' of different mixed possibilities,
            # get the greater and give it the _MX suffix
            if len(rank_names) > 1:
                
                max_value = max(rank_values)
                best_mixed = rank_names[rank_values.index(max_value)]
                
                use = best_mixed + "_MX"
            
            # if there was only one that had not higher developed value than the
            # selected one, gives it the _MX suffix aswell
            elif len(rank_names) == 1 and pure_use == False:
                use = rank_names[0] + "_MX"
                
        # any other, select the one with the higher percentage
        elif lv_s_names[0] in ls_selected:
            use = lv_s_names[0]
            
        else:
            use = "OTROS"
                
    return use

###############################################################################
#------------------------------------------------------------------------------

def use_function_definer(selection):
    ''' Return a function based on the selection

    :param selection: string of the wanted function
    :type text: str
    
    :output function selected (basic, intermediate or advanced)
    :type function
    '''
    
    if selection == "basic":
        use_definer = use_definer_basic
        
    elif selection == "intermediate":
        use_definer = use_definer_interm
        
    elif selection == "advanced":
        use_definer = use_definer_advanced
        
    return use_definer