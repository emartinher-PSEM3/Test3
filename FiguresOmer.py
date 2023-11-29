import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from matplotlib.lines import Line2D
from matplotlib.patches import Patch 

#Change
#2#


## Figure 2
F2_time_min = [0, 30, 60, 120, 180]
F2_ammonia_SepYield = [0, 29.1, 50.1, 78.7, 91.5]
F2_error = [0, 10, 8, 7, 4]
F2_labels = []
F2_ID = 'F2'

## Figure 3
F3_time_min = [0, 30, 60, 120, 180]
F3_EC = [7.51, 5.17, 4.13, 3.24, 2.79]
F3_EC_error = [0.32, 0.83, 0.60, 0.45, 0.05]

F3_pH = [8.52, 9.33, 9.51, 9.58, 9.54]
F3_pH_error = [0.09, 0.09, 0.15, 0.17, 0.18]
F3_labels=['EC', 'pH']
F3_ID = 'F3'

## Figure 4
F4_time_min = [0, 30, 60, 120, 180]
F4_Raw_ammonia_SepYield = [0, 23.69, 66.02, 87.77]
F4_11_ammonia_SepYield = [0, 13.1, 34.7, 74.3, 96.2]
F4_19_ammonia_SepYield = [0, 19.9, 32.3, 56.3, 65]
F4_1167_ammonia_SepYield = [0, 11.4, 26.6, 41.8, 50.6, 65]
F4_Raw_error = [0,0,0,0]
F4_11_error = [0,0,0,0,0]
F4_19_error = [0,0,0,0,0]
F4_1167_error = [0,0,0,0,0,0]
F4_labels = ['Raw centrate','1:1','1:9','1:167',]
F4_ID = 'F4'

## Figure 6
F6_time_min = [0, 30, 60, 120, 180]

F6_EC = [13.7, 12.12, 10.22, 7.14, 6.07]
F6_EC_error = [1.22, 0.57, 0.97, 0.77, 0.50]

F6_pH = [1.81, 1.86, 2.00, 2.50, 8.33]
F6_pH_error = [0.09, 0.09, 0.05, 0.01, 0.58]

F6_labels=['EC', 'pH']
F6_ID = 'F6'

def ScatterFunc (xValues, yValues, errorValues, labels, ID, xlabel, ylabel):
    markersize=6
    linewidth=2
    nSeries = len(yValues)
    fig, ax1 = plt.subplots(figsize=(4*1.618, 4))
    counter = 0
    colors = ['#293462','#37E2D5','#C70A80','#FBCB0A','#36AE7C']
    for i,error,ii in zip(yValues, errorValues, labels):
        # For smooth line
        XY_spline = make_interp_spline(xValues,i)
        X = np.linspace(min(xValues),max(xValues),500)
        Y = XY_spline(X)

        ax1.plot(xValues, i, linestyle='none', linewidth=linewidth,
                 marker='o', markersize=markersize, markerfacecolor=colors[counter], markeredgecolor=colors[counter],
                 label=ii)
        ax1.plot(X, Y, linestyle='-', linewidth=linewidth, color=colors[counter], marker='none', markersize=markersize, label=ii)

        if ID != 'F4':
            ax1.errorbar(xValues, i, yerr=error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[counter] )
        else:
            pass
        #ax1.set_xlim(0,190)

        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)
        ax1.grid(True,linestyle='--')

        if ID != 'F2':
            plt.legend()
        else:
            pass
       
        counter = counter+1

    plt.savefig(ID+'.pdf', bbox_inches = 'tight')
    plt.savefig(ID+'.png', bbox_inches = 'tight', dpi=600)
    plt.savefig(ID+'.svg', bbox_inches = 'tight')

ScatterFunc(F2_time_min,[F2_ammonia_SepYield],[F2_error],[F2_labels],F2_ID,'Time (min)','Ammonia separation yield (%)')
#ScatterFunc(F3_time_min,[F3_ammonia_SepYield],[F3_error],[F3_labels],F3_ID,'Time (min)','Ammonia separation yield (%)')
#ScatterFunc(F4_time_min,[F4_Raw_ammonia_SepYield,F4_11_ammonia_SepYield,F4_19_ammonia_SepYield,F4_1167_ammonia_SepYield],
#            [F4_Raw_error,F4_11_error,F4_19_error,F4_1167_error],[F4_labels],F4_ID,'Time (min)','Ammonia recovery yield (%)')
#ScatterFunc(F6_time_min,[F6_ammonia_SepYield],[F6_error],[F6_labels],F6_ID,'Time (min)','Ammonia separation yield (%)')

## F4
markersize=6
linewidth=2
fig, ax1 = plt.subplots(figsize=(4*1.618, 4))
colors = ['#293462','#37E2D5','#C70A80','#FBCB0A','#36AE7C']

# For smooth line
F4Raw_XY_spline = make_interp_spline([0,30,60,90],F4_Raw_ammonia_SepYield,k=2)
F4Raw_X = np.linspace(min([0,30,60,90]),max([0,30,60,90]),500)
F4Raw_Y = F4Raw_XY_spline(F4Raw_X)

ax1.plot([0,30,60,90], F4_Raw_ammonia_SepYield, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[0], markeredgecolor=colors[0])
ax1.plot(F4Raw_X, F4Raw_Y, linestyle='-', linewidth=linewidth, color=colors[0], marker='none', markersize=markersize, label='Raw centrate')
#ax1.errorbar([0,30,60,90], F4_Raw_ammonia_SepYield, yerr=F4_Raw_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[0])

## For smooth line
F411_XY_spline = make_interp_spline(F4_time_min,F4_11_ammonia_SepYield,k=2)
F411_X = np.linspace(min(F4_time_min),max(F4_time_min),500)
F411_Y = F411_XY_spline(F411_X)

ax1.plot(F4_time_min, F4_11_ammonia_SepYield, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[1], markeredgecolor=colors[1])
ax1.plot(F411_X, F411_Y, linestyle='-', linewidth=linewidth, color=colors[1], marker='none', markersize=markersize, label='Raw centrate')
#ax1.errorbar(F4_time_min, F4_11_ammonia_SepYield, yerr=F4_11_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[0])

## For smooth line
F419_XY_spline = make_interp_spline(F4_time_min,F4_19_ammonia_SepYield,k=2)
F419_X = np.linspace(min(F4_time_min),max(F4_time_min),500)
F419_Y = F419_XY_spline(F419_X)

ax1.plot(F4_time_min, F4_19_ammonia_SepYield, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[2], markeredgecolor=colors[2])
ax1.plot(F419_X, F419_Y, linestyle='-', linewidth=linewidth, color=colors[2], marker='none', markersize=markersize, label='Raw centrate')
#ax1.errorbar(F4_time_min, F4_19_ammonia_SepYield, yerr=F4_19_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[0])

## For smooth line
F41167_XY_spline = make_interp_spline([0,30,60,90,120,180],F4_1167_ammonia_SepYield,k=2)
F41167_X = np.linspace(min([0,30,60,90,120,180]),max([0,30,60,90,120,180]),500)
F41167_Y = F41167_XY_spline(F41167_X)

ax1.plot([0,30,60,90,120,180], F4_1167_ammonia_SepYield, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[3], markeredgecolor=colors[3])
ax1.plot(F41167_X, F41167_Y, linestyle='-', linewidth=linewidth, color=colors[3], marker='none', markersize=markersize, label='Raw centrate')
#ax1.errorbar([0,30,60,90,120,180], F4_1167_ammonia_SepYield, yerr=F4_1167_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[0])


ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Ammonia recovery yield (%)')

ax1.grid(True,linestyle='--')

legend_elements = [Line2D([0], [0], color=colors[0], lw=linewidth, label='Raw centrate'),
                   Line2D([0], [0], color=colors[1], lw=linewidth, label='1:1'),
                   Line2D([0], [0], color=colors[2], lw=linewidth, label='1:9'),
                   Line2D([0], [0], color=colors[3], lw=linewidth, label='1:167')]

ax1.legend(handles=legend_elements, loc='lower right')

plt.savefig('F4'+'.pdf', bbox_inches = 'tight')
plt.savefig('F4'+'.png', bbox_inches = 'tight', dpi=600)
plt.savefig('F4'+'.svg', bbox_inches = 'tight')

## F3
markersize=6
linewidth=2
fig, ax1 = plt.subplots(figsize=(4*1.618, 4))
colors = ['#293462','#37E2D5','#C70A80','#FBCB0A','#36AE7C']

# For smooth line
F3EC_XY_spline = make_interp_spline(F3_time_min,F3_EC)
F3EC_X = np.linspace(min(F3_time_min),max(F3_time_min),500)
F3EC_Y = F3EC_XY_spline(F3EC_X)

ax1.plot(F3_time_min, F3_EC, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[2], markeredgecolor=colors[2])
ax1.plot(F3EC_X, F3EC_Y, linestyle='-', linewidth=linewidth, color=colors[2], marker='none', markersize=markersize, label='EC')
ax1.errorbar(F3_time_min, F3_EC, yerr=F3_EC_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[2])

ax2 = ax1.twinx()

# For smooth line
F3pH_XY_spline = make_interp_spline(F3_time_min,F3_pH)
F3pH_X = np.linspace(min(F3_time_min),max(F3_time_min),500)
F3pH_Y = F3pH_XY_spline(F3pH_X)

ax2.plot(F3_time_min, F3_pH, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[3], markeredgecolor=colors[3],)
ax2.plot(F3pH_X, F3pH_Y, linestyle='-', linewidth=linewidth, color=colors[3], marker='none', markersize=markersize, label='pH')
ax2.errorbar(F3_time_min, F3_pH, yerr=F3_pH_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[3])

ax1.set_ylim(2,8)
ax2.set_ylim(8,10)

ax1.set_xlabel('Time (min)')
ax1.set_ylabel('EC (ms/cm)')
ax2.set_ylabel('pH')
ax1.grid(True,linestyle='--')

legend_elements = [Line2D([0], [0], color=colors[2], lw=linewidth, label='EC'),
                   Line2D([0], [0], color=colors[3], lw=linewidth, label='pH'),]

ax1.legend(handles=legend_elements, loc='center right')

plt.savefig('F3'+'.pdf', bbox_inches = 'tight')
plt.savefig('F3'+'.png', bbox_inches = 'tight', dpi=600)
plt.savefig('F3'+'.svg', bbox_inches = 'tight')


## F6
markersize=6
linewidth=2
fig, ax1 = plt.subplots(figsize=(4*1.618, 4))
colors = ['#293462','#37E2D5','#C70A80','#FBCB0A','#36AE7C']

# For smooth line
F6EC_XY_spline = make_interp_spline(F6_time_min,F6_EC)
F6EC_X = np.linspace(min(F6_time_min),max(F6_time_min),500)
F6EC_Y = F6EC_XY_spline(F6EC_X)

ax1.plot(F6_time_min, F6_EC, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[2], markeredgecolor=colors[2])
ax1.plot(F6EC_X, F6EC_Y, linestyle='-', linewidth=linewidth, color=colors[2], marker='none', markersize=markersize, label='EC')
ax1.errorbar(F6_time_min, F6_EC, yerr=F6_EC_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[2])

ax2 = ax1.twinx()

# For smooth line
F6pH_XY_spline = make_interp_spline(F6_time_min,F6_pH)
F6pH_X = np.linspace(min(F6_time_min),max(F6_time_min),500)
F6pH_Y = F6pH_XY_spline(F6pH_X)

ax2.plot(F6_time_min, F6_pH, linestyle='none', linewidth=linewidth,
         marker='o', markersize=markersize, markerfacecolor=colors[3], markeredgecolor=colors[3],)
ax2.plot(F6pH_X, F6pH_Y, linestyle='-', linewidth=linewidth, color=colors[3], marker='none', markersize=markersize, label='pH')
ax2.errorbar(F6_time_min, F6_pH, yerr=F6_pH_error, fmt='.', linewidth=linewidth*0.75, capsize=3, color=colors[3])

ax1.set_ylim(0,16)
ax2.set_ylim(1,10)

ax1.set_xlabel('Time (min)')
ax1.set_ylabel('EC (ms/cm)')
ax2.set_ylabel('pH')
ax1.grid(True,linestyle='--')

legend_elements = [Line2D([0], [0], color=colors[2], lw=linewidth, label='EC'),
                   Line2D([0], [0], color=colors[3], lw=linewidth, label='pH'),]

ax1.legend(handles=legend_elements, loc='lower right')

plt.savefig('F6'+'.pdf', bbox_inches = 'tight')
plt.savefig('F6'+'.png', bbox_inches = 'tight', dpi=600)
plt.savefig('F6'+'.svg', bbox_inches = 'tight')

