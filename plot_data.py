import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def get_hsv_colors():
    # https://matplotlib.org/3.1.0/gallery/color/named_colors.html
    by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(color))), name) 
                    for name, color in mcolors.CSS4_COLORS.items())
    return [name for _, name in by_hsv]



def PlotTS(
        df: pd.DataFrame,
        cols: list,
        title: str,
        ylab: str,
        footnote: "",
        clrs = ['#6495ED', '#0000FF', '#00FFFF','#00BFFF', '#7B68EE'],
        fig_size = (10,6)
):
    '''
    Plots a nice graph for a dataframe indexed by datetime

    Inputs: 
    df - dataframe with datetime index
    cols - list of columns to plot
    title - plot title
    ylab - y-axis title
    footnote - footnote str
    clrs - list of colors
    fig_size - tuple figure size


    Output:
    matplotlib graph
    '''
    
    
    ax = df[cols].plot(color=clrs, figsize=fig_size)

    # Prettify
    plt.title(title, fontdict={'fontsize':15})
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.02), 
              ncol=5, frameon=False)
    ax.set_xlabel(' ')
    plt.ylabel(ylab)

    ## Borderless
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(axis='y')
    ax.tick_params(left = False, bottom=False)
    #plt.tick_params(left = False, bottom=False)


    #Footnote
    plt.figtext(0.5, 0.01, footnote, 
                ha="left", fontsize=10,
                bbox={"facecolor":"orange", "alpha":0.2, "pad":5})

    #fig.tight_layout(rect=(0,.05,1,1)) 
    plt.show()










if __name__=='__main__':
    # Test df
    ds = pd.date_range("2023-01-01", "2024-02-01")
    df_test = pd.DataFrame(
        {'ds': ds,
        'x1': (1+np.random.uniform(0,1/250, len(ds))).cumprod()-1,
        'x2': (1+np.random.uniform(0,1/250, len(ds))).cumprod()-1,
        'x3': (1+np.random.uniform(-1/250,1/250, len(ds))).cumprod()-1,
        'x4': (1+np.random.uniform(-1/250,1/250, len(ds))).cumprod()-1,
        'x5': np.random.uniform(-1/250,0, len(ds)),
        }
    ).set_index('ds')
    
    PlotTS(df_test, cols = ['x1','x2','x3', 'x4'], 
           title='Test Title', ylab='Test Label', footnote='Test footnote')
