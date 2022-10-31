# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 14:05:06 2022

@author: xucha
"""

import numpy as np
#Importing and setting up all the data

#Empty Sets of Grains
grain1,grain2,grain3,grain4,grain5,grain6,grain7 = ([] for i in range(7))

#Empty Sets for nodes and elements
g1_n,g1_e = ([] for i in range(2))
g2_n,g2_e = ([] for i in range(2))
g3_n,g3_e = ([] for i in range(2))
g4_n,g4_e = ([] for i in range(2))
g5_n,g5_e = ([] for i in range(2))
g6_n,g6_e = ([] for i in range(2))
g7_n,g7_e = ([] for i in range(2))



#Importing and parsing data
with open("test_vol_fill.txt",'r') as f:
    #Parse List 
    grain1 = f.read().splitlines()  
    grain1_nodes = grain1[1:98]
    grain1_elements = grain1[99:327]
    for x in range(len(grain1_nodes)):
        temp_n = np.fromstring(grain1_nodes[x], sep=',')
        g1_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain1_elements)):
        temp_e = np.fromstring(grain1_elements[y], sep=',')
        g1_e.append(temp_e.reshape(1,-1))
f.close()

with open("test_vol_fill1.txt",'r') as f:
    #Parse List 
    grain2 = f.read().splitlines()  
    grain2_nodes = grain2[1:68]
    grain2_elements = grain2[69:213]
    for x in range(len(grain2_nodes)):
        temp_n = np.fromstring(grain2_nodes[x], sep=',')
        g2_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain2_elements)):
        temp_e = np.fromstring(grain2_elements[y], sep=',')
        g2_e.append(temp_e.reshape(1,-1))
f.close()

with open("test_vol_fill3.txt",'r') as f:
    #Parse List 
    grain3 = f.read().splitlines()  
    grain3_nodes = grain3[1:25]
    grain3_elements = grain3[26:58]
    for x in range(len(grain3_nodes)):
        temp_n = np.fromstring(grain3_nodes[x], sep=',')
        g3_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain3_elements)):
        temp_e = np.fromstring(grain3_elements[y], sep=',')
        g3_e.append(temp_e.reshape(1,-1))
f.close()

with open("test_vol_fill4.txt",'r') as f:
    #Parse List 
    grain4 = f.read().splitlines()  
    grain4_nodes = grain4[1:77]
    grain4_elements = grain4[78:245]
    for x in range(len(grain4_nodes)):
        temp_n = np.fromstring(grain4_nodes[x], sep=',')
        g4_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain4_elements)):
        temp_e = np.fromstring(grain4_elements[y], sep=',')
        g4_e.append(temp_e.reshape(1,-1))
f.close()

with open("test_vol_fill5.txt",'r') as f:
    #Parse List 
    grain5 = f.read().splitlines()  
    grain5_nodes = grain5[1:50]
    grain5_elements = grain5[51:153]
    for x in range(len(grain5_nodes)):
        temp_n = np.fromstring(grain5_nodes[x], sep=',')
        g5_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain5_elements)):
        temp_e = np.fromstring(grain5_elements[y], sep=',')
        g5_e.append(temp_e.reshape(1,-1))
f.close()

with open("test_vol_fill6.txt",'r') as f:
    #Parse List 
    grain6 = f.read().splitlines()  
    grain6_nodes = grain6[1:105]
    grain6_elements = grain6[106:356]
    for x in range(len(grain6_nodes)):
        temp_n = np.fromstring(grain6_nodes[x], sep=',')
        g6_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain6_elements)):
        temp_e = np.fromstring(grain6_elements[y], sep=',')
        g6_e.append(temp_e.reshape(1,-1))
f.close()

with open("test_vol_fill7.txt",'r') as f:
    #Parse List 
    grain7 = f.read().splitlines()  
    grain7_nodes = grain7[1:162]
    grain7_elements = grain7[163:592]
    for x in range(len(grain7_nodes)):
        temp_n = np.fromstring(grain7_nodes[x], sep=',')
        g7_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain7_elements)):
        temp_e = np.fromstring(grain7_elements[y], sep=',')
        g7_e.append(temp_e.reshape(1,-1))
f.close()

#Creating the array sets for the nodes and elements
g1_nl = np.vstack(g1_n)
g1_el = np.vstack(g1_e)
g2_nl = np.vstack(g2_n)
g2_el = np.vstack(g2_e)
g3_nl = np.vstack(g3_n)
g3_el = np.vstack(g3_e)
g4_nl = np.vstack(g4_n)
g4_el = np.vstack(g4_e)
g5_nl = np.vstack(g5_n)
g5_el = np.vstack(g5_e)
g6_nl = np.vstack(g6_n)
g6_el = np.vstack(g6_e)
g7_nl = np.vstack(g7_n)
g7_el = np.vstack(g7_e)

##############################################################################

#Setting up Master Node list
master_nodes = np.concatenate((g1_nl,g2_nl,g3_nl,g4_nl,g5_nl,g6_nl,g7_nl))
mn_index = np.delete(master_nodes,0,1)
mn_list = np.linspace(1,len(master_nodes),len(master_nodes)).reshape(-1,1)
mn_indexed = np.hstack((mn_list,mn_index))
u, sn = np.unique(mn_index,return_index=True,axis=0)
scalped_nodes = u[np.argsort(sn)]
index = np.linspace(1,len(scalped_nodes),len(scalped_nodes)).reshape(-1,1)
master_nodes_unique = np.hstack((index,scalped_nodes))

##############################################################################

#Master Element List
# master_elements = np.concatenate((g1_el,g2_el,g3_el,g4_el,g5_el,g6_el,g7_el))
# me_index = np.delete(master_elements,0,1)
# me_list = np.linspace(1,len(master_elements),len(master_elements)).reshape(-1,1)
# master_elements_labled = np.hstack((me_list,me_index))

##############################################################################

#Map Createion pointing to each node per grain

#Grain 1 map
g1_map = []
for a in range(len(g1_n)):
    g1_map.append(master_nodes[a])

#Create a list of jsut the positionals of g1
g1_map = np.array(g1_map)
g1_map_n = np.delete(g1_map,0,1)

#Grain 2 map
g2_index = g2_nl[:,0].reshape(-1,1)
g2_scalped_n = np.delete(g2_nl,0,1)
g2_n_renum_index = g2_index + len(g1_n)
for x in range(len(g2_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g2_scalped_n[x],scalped_nodes[y]) == True:
            g2_n_renum_index[x,0] = y+1
            
g2_map_n = np.hstack((g2_index,g2_n_renum_index,(g2_index + len(g1_n))))

#Grain 3 Map
g3_index = g3_nl[:,0].reshape(-1,1)
g3_scalped_n = np.delete(g3_nl,0,1)
g3_n_renum_index = g3_index + len(g1_n) + len(g2_n)
for x in range(len(g3_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g3_scalped_n[x],scalped_nodes[y]) == True:
            g3_n_renum_index[x,0] = y+1
            
g3_map_n = np.hstack((g3_index,g3_n_renum_index,(g3_index+len(g1_n)+len(g2_n))))

#Grain 4 Map
g4_index = g4_nl[:,0].reshape(-1,1)
g4_scalped_n = np.delete(g4_nl,0,1)
g4_n_renum_index = g4_index+len(g1_n)+len(g2_n)+len(g3_n)
for x in range(len(g4_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g4_scalped_n[x],scalped_nodes[y]) == True:
            g4_n_renum_index[x,0] = y+1
            
g4_map_n = np.hstack((g4_index,g4_n_renum_index,(g4_index+
                                                  len(g1_n)+len(g2_n)+
                                                  len(g3_n))))

#Grain 5 Map
g5_index = g5_nl[:,0].reshape(-1,1)
g5_scalped_n = np.delete(g5_nl,0,1)
g5_n_renum_index = g5_index+len(g1_n)+len(g2_n)+len(g3_n)+len(g4_n)
for x in range(len(g5_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g5_scalped_n[x],scalped_nodes[y]) == True:
            g5_n_renum_index[x,0] = y+1
            
g5_map_n = np.hstack((g5_index,g5_n_renum_index,(g5_index+
                                                  len(g1_n)+len(g2_n)+
                                                  len(g3_n)+len(g4_n))))

#Grain 6 Map
g6_index = g6_nl[:,0].reshape(-1,1)
g6_scalped_n = np.delete(g6_nl,0,1)
g6_n_renum_index = g6_index+len(g1_n)+len(g2_n)+len(g3_n)+len(g4_n)+len(g5_n)
for x in range(len(g6_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g6_scalped_n[x],scalped_nodes[y]) == True:
            g6_n_renum_index[x,0] = y+1
            
g6_map_n = np.hstack((g6_index,g6_n_renum_index,(g6_index+len(g1_n)+len(g2_n)+
                                                  len(g3_n)+len(g4_n)+
                                                  len(g5_n))))

#Grain 7 Map
g7_index = g7_nl[:,0].reshape(-1,1)
g7_scalped_n = np.delete(g7_nl,0,1)
g7_n_renum_index = g7_index+len(g1_n)+len(g2_n)+len(g3_n)+len(g4_n)+len(g5_n)+len(g6_n)
for x in range(len(g7_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g7_scalped_n[x],scalped_nodes[y]) == True:
            g7_n_renum_index[x,0] = y+1
            
g7_map_n = np.hstack((g7_index,g7_n_renum_index,(g7_index+len(g1_n)+len(g2_n)+
                                                  len(g3_n)+len(g4_n)+
                                                  len(g5_n)+len(g6_n))))

##############################################################################

#Element Renumbering
#Remove the index of the elements

g1_e_scalp = np.delete(g1_el,0,1)
g2_e_scalp = np.delete(g2_el,0,1)
g3_e_scalp = np.delete(g3_el,0,1)
g4_e_scalp = np.delete(g4_el,0,1)
g5_e_scalp = np.delete(g5_el,0,1)
g6_e_scalp = np.delete(g6_el,0,1)
g7_e_scalp = np.delete(g7_el,0,1)


#Creating a renumbered index for the grains
g1_e_index = np.linspace(1,len(g1_e_scalp),len(g1_e_scalp))
g2_e_index = np.linspace(1,len(g2_e_scalp),len(g2_e_scalp))
g3_e_index = np.linspace(1,len(g3_e_scalp),len(g3_e_scalp))
g4_e_index = np.linspace(1,len(g4_e_scalp),len(g4_e_scalp))
g5_e_index = np.linspace(1,len(g5_e_scalp),len(g5_e_scalp))
g6_e_index = np.linspace(1,len(g6_e_scalp),len(g6_e_scalp))
g7_e_index = np.linspace(1,len(g7_e_scalp),len(g7_e_scalp))

#Renumbering the indicies and elements to the master list equivalent
g2_e_renum = g2_e_index+len(g1_e_index)
g2_e_scalp_renum = g2_e_scalp+len(g1_n)

g3_e_renum = g3_e_index+len(g1_e_index)+len(g2_e_index)
g3_e_scalp_renum = g3_e_scalp+len(g1_n)+len(g2_n)

g4_e_renum = g4_e_index+len(g1_e_index)+len(g2_e_index)+len(g3_e_index)
g4_e_scalp_renum = g4_e_scalp+len(g1_n)+len(g2_n)+len(g3_n)

g5_e_renum = g5_e_index+len(g1_e_index)+len(g2_e_index)+len(g3_e_index)+len(g4_e_index)
g5_e_scalp_renum = g5_e_scalp+len(g1_n)+len(g2_n)+len(g3_n)+len(g4_n)

g6_e_renum = g6_e_index+len(g1_e_index)+len(g2_e_index)+len(g3_e_index)+len(g4_e_index)+len(g5_e_index)
g6_e_scalp_renum = g6_e_scalp+len(g1_n)+len(g2_n)+len(g3_n)+len(g4_n)+len(g5_n)

g7_e_renum = g7_e_index+len(g1_e_index)+len(g2_e_index)+len(g3_e_index)+len(g4_e_index)+len(g5_e_index)+len(g6_e_index)
g7_e_scalp_renum = g7_e_scalp+len(g1_n)+len(g2_n)+len(g3_n)+len(g4_n)+len(g5_n)+len(g6_n)


#Grain 2 renumbering of element nodes
for x in range(len(g2_e_scalp_renum)):
    for y in range(4):
        for z in range(len(g2_map_n)):
            if g2_e_scalp_renum[x,y] == g2_map_n[z,2]:
                g2_e_scalp_renum[x,y] = g2_map_n[z,1]
            else:
                pass

#Grain 3 renumbering of element nodes
for x in range(len(g3_e_scalp_renum)):
    for y in range(4):
        for z in range(len(g3_map_n)):
            if g3_e_scalp_renum[x,y] == g3_map_n[z,2]:
                g3_e_scalp_renum[x,y] = g3_map_n[z,1]
            else:
                pass

#Grain 4 renumbering of element nodes
for x in range(len(g4_e_scalp_renum)):
    for y in range(4):
        for z in range(len(g4_map_n)):
            if g4_e_scalp_renum[x,y] == g4_map_n[z,2]:
                g4_e_scalp_renum[x,y] = g4_map_n[z,1]
            else:
                pass

#Grain 5 renumber
for x in range(len(g5_e_scalp_renum)):
    for y in range(4):
        for z in range(len(g5_map_n)):
            if g5_e_scalp_renum[x,y] == g5_map_n[z,2]:
                g5_e_scalp_renum[x,y] = g5_map_n[z,1]
            else:
                pass

#Grain 6 renumbering of element nodes
for x in range(len(g6_e_scalp_renum)):
    for y in range(4):
        for z in range(len(g6_map_n)):
            if g6_e_scalp_renum[x,y] == g6_map_n[z,2]:
                g6_e_scalp_renum[x,y] = g6_map_n[z,1]
            else:
                pass

#Grain 7 renumbering of element nodes
for x in range(len(g7_e_scalp_renum)):
    for y in range(4):
        for z in range(len(g7_map_n)):
            if g7_e_scalp_renum[x,y] == g7_map_n[z,2]:
                g7_e_scalp_renum[x,y] = g7_map_n[z,1]
            else:
                pass

                
#Elements Combined List
elements_combined = np.vstack((g1_e_scalp,g2_e_scalp_renum,g3_e_scalp_renum,
                               g4_e_scalp_renum,g5_e_scalp_renum,
                               g6_e_scalp_renum,g7_e_scalp_renum))              


element_index = np.linspace(1,len(elements_combined),len(elements_combined)).reshape(-1,1)                         
ec_indexed = np.hstack((element_index,elements_combined))

##############################################################################
#writing to text file
with open('merged_test_full.inp','w') as f:
    f.writelines("""*NODE\n""")
    np.savetxt(f, master_nodes_unique,
                fmt = ['%1.0i', '%.08f', '%.08f', '%.08f'],
                delimiter = ',')
    f.writelines("""*ELEMENT, type=C3D4, ELSET=Volume1\n""")
    np.savetxt(f, ec_indexed, 
                fmt = '%.1i', delimiter =',')




















