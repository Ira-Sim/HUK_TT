import os
def paths():
    # set the path to the raw data relative to current working directory
    project_path = os.getcwd()  
    raw_data_path = os.path.realpath(os.path.join(project_path, '..', 'raw_data'))
    # set the path to the data
    data_path =os.path.realpath(os.path.join(project_path, '..', 'working_data'))
    # set the path to the data
    #output_path =os.path.realpath(os.path.join(project_path, '..', 'output'))
    
    return raw_data_path, data_path#, output_path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def formattingStyle():
    # This will change to your computer's default Times New Roman font
    plt.rcParams["font.family"] = "Calibri"
    
    # setting the font size
    SMALL_SIZE = 12
    MEDIUM_SIZE = 12
    BIGGER_SIZE = 18

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    # set the style of the plots
    sns.set_style("white",  {'axes.edgecolor': '0.0', 'axes.linewidth': 0.1, 'grid.color': '.9'}) 

    # set the color palette
    sns.set_palette("YlOrBr")

    pd.options.display.float_format = '{:,.2f}'.format
