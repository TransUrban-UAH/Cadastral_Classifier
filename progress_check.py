# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:53:45 2024

@author: nikolai.shurupov
"""

from copy import deepcopy

progress_each_mun = 100/90 # state the progress bar evolution caps

i = 0 # store numerically the initialization
for selected in range (1, 90):
    
    progress_start = i * progress_each_mun
    # state the cap that has to be reached once all the operations
    # in the mun are performed
    progress_cap = progress_each_mun + i * progress_each_mun
    
    progress_total_increase = progress_cap - progress_start

    progress = deepcopy(progress_start)
    
    
    progress += 0.01 * progress_total_increase
    progress += 0.01 * progress_total_increase
    progress += 0.01 * progress_total_increase
    
    max_iter_p1 = 14000

            
    progress_1st_process_increase = ((progress_cap - progress_start)*0.29)/max_iter_p1

    for index in range (1, 14000):

        progress += progress_1st_process_increase
    
    max_iter_p2 = 14000
    
    progress_2nd_process_increase = ((progress_cap - progress_start)*0.69)/max_iter_p2

    
    # iterate over all features
    for f in range (1, 14000):
        
        # update the progress bar
        progress += progress_2nd_process_increase
        
        print (progress)

    i += 1
    
        
    
