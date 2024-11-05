# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:07:42 2024

@author: dy2507
"""

import numpy as np
import sys
import math
import copy
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-deep')  

file_path = '/home/dp7972/Desktop/DAYOU/PlottingDayou/DREP_plot_table'

table_name = '/Tables_draft_version/Draft_version_table_500x500.txt'
rows = []
with open(file_path+table_name,'r') as infile:
    i=0
    for row in infile:
        i=i+1
        hold = [x for x in row.split(' ') if x !='' and x!='\n']
        rows.append(hold)


j = 0
density = []
temperature = []
pressure = []
energy = []
for item in rows:
    if j>=1:
        if len(item)==3 and item[0]=='Density=':
            density_c = item[1]
        
        if (len(item)==3 and item[0]!='Temperature(eV)' and item[0]!='Density='):
            density.append(float(density_c))
            temperature.append(float(item[0]))
            pressure.append(float(item[1]))
            energy.append(float(item[2]))
    j = j+1


C1 = np.array(density).reshape(len(density),1)
C2 = np.array(temperature).reshape(len(density),1)
C3 = np.array(pressure).reshape(len(density),1)
C4 = np.array(energy).reshape(len(density),1)
C = np.array([C1,C2,C3,C4]).reshape(4,len(density)).T

D = C[C[:,2]!=0]

density = list(set(D[:,0]))
density.sort()
data_list = []
for dens_v in density:
    data_list.append(D[np.where(D[:,0]==dens_v)[0],:])

pred_list = copy.deepcopy(data_list)

C = np.load(file_path+'/data_v9.npy')


density = list(set(C[:,0]))
density.sort()
data_list = []
for dens_v in density:
    data_list.append(C[np.where(C[:,0]==dens_v)[0],:])

import matplotlib.colors as mcolorsline_sty
colors='tab_color'
if colors=='tab_color':
    line_sty = ['tab:blue','tab:orange','tab:green','tab:red','tab:purple','tab:brown','tab:olive','tab:pink','tab:gray','tab:cyan']


task = 'plot3'
if task=='plot1':
    pred_ind = [25,74,109,173,213,253,289,339,366,412]
    plot_list1 = []
    for ind in pred_ind:
        plot_list1.append(pred_list[ind])
        
        
    pred_ind1 = [15,90,125,200,230,270,310,350,400,450]
    plot_list3 = []
    for ind in pred_ind1:
        plot_list3.append(pred_list[ind])
        
        
        
    ref_ind = [0,1,6,11,16,26,31,36,41,46]
    
    
    plot_list2 = []
    for ind in ref_ind:
        plot_list2.append(data_list[ind])
    
    ax = plt.figure()
    
    
    ct = 0

    for data in plot_list1:
        plt.plot(data[:,1],data[:,2],line_sty[ct],linewidth = 2,label = f'{data[0,0]:.2f}g/cc')
        ct+=1

    ct = 0

    for data in plot_list3:
        plt.plot(data[:,1],data[:,2],line_sty[ct],linewidth = 2,linestyle = '--',label = f'{data[0,0]:.2f}g/cc')
        ct+=1

    cl = 0
    for data in plot_list2:
        plt.plot(data[:,1],data[:,2],'s',mec=line_sty[cl],mfc='none',markersize=3,label = f'{data[0,0]:.2f}g/cc')
        cl+=1

    plt.ticklabel_format(style='sci', axis='both')#, scilimits=(0,0))    
    plt.tick_params(axis='both', labelsize=20)
    # plt.xlabel('Temperature (K)',fontsize = 30)
    # plt.ylabel('Pressure (Mbar)',fontsize = 30)

    plt.xlabel('Temperature (K)', fontsize=16, labelpad=10)
    plt.ylabel('Pressure (Mbar)', fontsize=16, labelpad=10)
    plt.title('Pressure vs Temperature', fontsize=18, pad=15)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xscale('log')
    plt.yscale('log')
    # plt.title('Pressure',fontsize = 30)
    # plt.legend(loc=2,fontsize=10,fancybox=True, framealpha=0.5)
    # plt.legend(bbox_to_anchor=(0.5, 1.2),loc='upper center',fontsize=10,fancybox=True, framealpha=0.8,ncol=10)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12, fancybox=True, framealpha=0.5, ncol=2)
    plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.4)
    plt.savefig(f'/home/dp7972/Desktop/DAYOU/PlottingDayou/DREP_plot_table_DP/plot_table/DREP_P_{data[0,0]:3.1e}.pdf',bbox_inches='tight',format='pdf')
    
elif task=='plot2':
    pred_ind = [25,74,109,173,213,253,289,339,366,412]
    plot_list1 = []
    for ind in pred_ind:
        plot_list1.append(pred_list[ind])
        
        
    pred_ind1 = [15,90,125,200,230,270,310,350,400,450]
    plot_list3 = []
    for ind in pred_ind1:
        plot_list3.append(pred_list[ind])
        
        
        
    ref_ind = [0,1,6,11,16,26,31,36,41,46]
    
    
    plot_list2 = []
    for ind in ref_ind:
        plot_list2.append(data_list[ind])
    
    ax = plt.figure()
    
    
    ct = 0

    for data in plot_list1:
        plt.plot(data[:,1],data[:,3],line_sty[ct],linewidth = 2,label = f'{data[0,0]:.2f}g/cc')
        ct+=1

    ct = 0

    for data in plot_list3:
        plt.plot(data[:,1],data[:,3],line_sty[ct],linewidth = 2,linestyle = '--',label = f'{data[0,0]:.2f}g/cc')
        ct+=1

    cl = 0
    for data in plot_list2:
        plt.plot(data[:,1],data[:,3],'s',mec=line_sty[cl],mfc='none',markersize=4,label = f'{data[0,0]:.2f}g/cc')
        cl+=1

    plt.ticklabel_format(style='sci', axis='both')#, scilimits=(0,0))    
    plt.tick_params(axis='both', labelsize=20)
    plt.xlabel('Temperature (K)', fontsize=16, labelpad=10)
    plt.ylabel('Internal Energy (eV/atom)', fontsize=16, labelpad=10)
    plt.title('Internal Energy vs Temperature', fontsize=18, pad=15)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12, fancybox=True, framealpha=0.5, ncol=2)
    plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.4)

    plt.savefig(f'/home/dp7972/Desktop/DAYOU/PlottingDayou/DREP_plot_table_DP/plot_table/DREP_E_{data[0,0]:3.1e}.pdf',bbox_inches='tight',format='pdf')
    
    
    
elif task=='plot3':
    pred_ind = [25,74,109,173,213,253,289,339,366,412]
    plot_list1 = []
    for ind in pred_ind:
        plot_list1.append(pred_list[ind])
        
        
    pred_ind1 = [70,90,125,200,230,270,310,350,400,450]
    plot_list3 = []
    for ind in pred_ind1:
        plot_list3.append(pred_list[ind])
        
        
        
    ref_ind = [0,1,6,11,16,26,31,36,41,46]
    
    
    plot_list2 = []
    for ind in ref_ind:
        plot_list2.append(data_list[ind])
    
    ax = plt.figure()
    
    
    ct = 0

    for data in plot_list1:
        plt.plot(np.log10(data[:,1]),np.log10(data[:,3]+16),line_sty[ct],linewidth = 2,label = f'{data[0,0]:.2f}g/cc')
        ct+=1

    ct = 0

    for data in plot_list3:
        plt.plot(np.log10(data[:,1]),np.log10(data[:,3]+16),line_sty[ct],linewidth = 2,linestyle = '--',label = f'{data[0,0]:.2f}g/cc')
        ct+=1

    cl = 0
    for data in plot_list2:
        plt.plot(np.log10(data[:,1]),np.log10(data[:,3]+16),'s',mec=line_sty[cl],mfc='none',markersize=4,label = f'{data[0,0]:.2f}g/cc')
        cl+=1

    plt.ticklabel_format(style='sci', axis='both')
    plt.tick_params(axis='both', labelsize=20)
    plt.xlabel('Temperature (K)', fontsize=16, labelpad=10)
    plt.ylabel('Internal Energy (eV/atom)', fontsize=16, labelpad=10)
    plt.title('Internal Energy', fontsize=18, pad=15)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12, fancybox=True, framealpha=0.5, ncol=2)
    plt.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.4)
    plt.savefig(f'/home/dp7972/Desktop/DAYOU/PlottingDayou/DREP_plot_table_DP/plot_table/DREP_E_log_{data[0,0]:3.1e}.pdf', bbox_inches='tight', format='pdf')
