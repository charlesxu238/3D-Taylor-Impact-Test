# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 10:47:11 2022

@author: xucha
"""

#Import Libraries 
import numpy as np

#Main

#Empty Sets
g1_n = []
g1_e = []
g2_n = []
g2_e = []

#Import Grains
with open("cyltest_vol1.txt",'r') as f:
    #Parse List 
    grain1 = f.read().splitlines()  
    grain1_nodes = grain1[1:72]
    grain1_elements = grain1[73:226]
    for x in range(len(grain1_nodes)):
        temp_n = np.fromstring(grain1_nodes[x], sep=',')
        g1_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain1_elements)):
        temp_e = np.fromstring(grain1_elements[y], sep=',')
        g1_e.append(temp_e.reshape(1,-1))
f.close()

with open("cyltest_vol2.txt",'r') as f:
    #Parse List 
    grain2 = f.read().splitlines()  
    grain2_nodes = grain2[1:57]
    grain2_elements = grain2[58:175]
    for x in range(len(grain2_nodes)):
        temp_n = np.fromstring(grain2_nodes[x], sep=',')
        g2_n.append(temp_n.reshape(1,-1))
    for y in range(len(grain2_elements)):
        temp_e = np.fromstring(grain2_elements[y], sep=',')
        g2_e.append(temp_e.reshape(1,-1))
f.close()

#Merged Lists Nodes
g1_merged_n = np.vstack(g1_n)
g1_merged_e = np.vstack(g1_e)
g2_merged_n = np.vstack(g2_n)
g2_merged_e = np.vstack(g2_e)

#Getting the unique nodal list
master_nodes = np.concatenate((g1_merged_n,g2_merged_n))
mn_index = np.delete(master_nodes,0,1)
mn_list = np.linspace(1,len(master_nodes),len(master_nodes)).reshape(-1,1)
mn_indexed = np.hstack((mn_list,mn_index))
u, sn = np.unique(mn_index,return_index=True,axis=0)
scalped_nodes = u[np.argsort(sn)]
index = np.linspace(1,len(scalped_nodes),len(scalped_nodes)).reshape(-1,1)

#Unique set of indexed nodes
sn_indexed = np.hstack((index,scalped_nodes))


g1_map = []
for a in range(len(g1_n)):
    g1_map.append(master_nodes[a])

g1_map = np.array(g1_map)
g1_map_n = np.delete(g1_map,0,1)

g2_nodes = np.array(g2_n).reshape(-1,4)
g2_node_list = g2_nodes[:,0].reshape(-1,1)
g2_scalped_n = np.delete(g2_nodes,0,1)

g2_node_renum = g2_node_list + len(g1_n)


for x in range(len(g2_scalped_n)):
    for y in range(len(scalped_nodes)):
        if np.array_equal(g2_scalped_n[x],scalped_nodes[y]) == True:
            g2_node_renum[x,0] = y+1
            print('test'+str(x)+' '+'test'+str(y))
    
g2_map_n = np.hstack((g2_node_list,g2_node_renum,(g2_node_list+len(g1_n))))


g1_ele = np.array(g1_e).reshape(-1,5)
g2_ele = np.array(g2_e).reshape(-1,5)

#Remove the index of the element 
g1_ele_scalp = np.delete(g1_ele,0,1)
g2_ele_scalp = np.delete(g2_ele,0,1) 
g2_e_index = np.linspace(1,len(g2_map_n),len(g2_map_n)).reshape(-1,1)+len(g1_n) #index list of elements

g2_ele_renum = g2_ele_scalp + len(g1_n)

#Renumbered g2 element list
for x in range(len(g2_ele_renum)):
    for y in range(4):
        for z in range(len(g2_map_n)):
            if g2_ele_renum[x,y] == g2_map_n[z,2]:
                g2_ele_renum[x,y] = g2_map_n[z,1]
            else:
                pass

#Combined Element List
elements_combined = np.vstack((g1_ele_scalp,g2_ele_renum))

#Labeled Element List
ec_indexed = np.hstack((np.linspace(1,len(elements_combined),
                                    len(elements_combined)).reshape(-1,1),
                        elements_combined))

#writing to text file
with open('merged_test.inp','w') as f:
    f.writelines("""*NODE\n""")
    np.savetxt(f, sn_indexed,
                fmt = ['%1.0i', '%.08f', '%.08f', '%.08f'],
                delimiter = ',')
    f.writelines("""*ELEMENT, type=C3D4, ELSET=Volume1\n""")
    np.savetxt(f, ec_indexed, 
                fmt = '%.1i', delimiter =',')


# for x in range(len(g2_map)):
#     for y in range(len(g1_map_n)):
#         if np.array_equal(g2_map[x],g1_map_n[y]) == True:
#             g2_map_n[x,0] = 1+y
#             print('test'+str(x)+' '+str(y))
            



# for a in range(len(g2_merged_n)):
#     for b in range(len(g1_merged_n)):
#         for i in range(3):
#             if 
            


#Creating a key for the nodes
# grain_index = []
# #Sort through both lists to find the shared indices
# for x in range(len(scalped_nodes)):
#     for y in range(len(mn_index)):
#             if ((scalped_nodes[x,0] == mn_index[y,0]) and
#                 (scalped_nodes[x,1] == mn_index[y,1]) and
#                 (scalped_nodes[x,2] == mn_index[y,2])):
#                     grain_index.append(y)
#     if len(grain_index)%2 != 0:
#         grain_index.append(0)
# gi_array = np.array(grain_index)
# #Tracks which nodes are shared
# gi_sorted = np.resize(gi_array,(int(len(gi_array)/2),2))

# # #grain 1 element scalp
# g1_e_scalped=np.delete(g1_merged_e,0,1)
# # g1_er = g1_e_scalped
# # for x in range(len(g1_e_scalped)):
# #     for y in range(4):
# #         for z in range(len(gi_sorted)):
# #             if g1_er[x,y] == gi_sorted[z,1]:
# #                 g1_er[x,y] == gi_sorted[z,0]
# # g1_er_sorted = np.array(g1_er).reshape(-1,4)

# #grain 2 element scalp
# g2_e_scalped=np.delete(g2_merged_e,0,1)
# g2_er = g2_e_scalped+70
# g2_m_n = np.delete(g2_merged_n,0,1)

# for x in range(len(g2_er)):
#     for n in range(4):
#         for y in range(len(gi_sorted)):
#             if g2_er[x,n] == gi_sorted[y,1]:
#                 g2_er[x,n] = gi_sorted[y,0]
                

    
# for x in range(len(g2_e_scalped)):
#     for n in range(4):
#         check = 0
#         for m in range(3):
#             for y in range(len(scalped_nodes)):
#                 for p in range(3):
#                     if (mn_index[int((g2_er[x,n]))-1,m] == scalped_nodes[y,p]):
#                         check_ = check+1
#                         if check == 3:
#                             g2_er[x,n] == sn_indexed[y,0]
#                             print('test'+str(x))
#                             check = 0

                      

# # g2_er_sorted = np.array(g2_er).reshape(-1,4)

# #combined list of elements
# element_combined = np.vstack((g1_e_scalped,g2_er))
# element_set_sorted = np.hstack((np.linspace(1,len(element_combined),len(element_combined)).reshape(-1,1),
#                                 element_combined))

