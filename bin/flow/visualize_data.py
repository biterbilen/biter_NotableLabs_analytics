import matplotlib.pyplot as plt
import seaborn as sns

def scatter(df, ofile, x, y, title=''):
    sns.set(style="whitegrid")
    #sns.set(style="whitegrid", palette="pastel", color_codes=True)

    fig = plt.figure()
    plt.scatter(x, y, data=df)
    plt.title(title)
    fig.savefig(ofile)
    plt.close()
    
    
def violin(df, ofile, x, y, hue=None, scale='count', title=''):
    fig = plt.figure()
    sns.set(style="whitegrid") #, palette="pastel", color_codes=True) 
    sns.violinplot(data=df, x=x, y=y, hue=hue, scale=scale, inner="quart") #split=True,
    ax = fig.add_subplot(111)
    xticklabels = [item.get_text() for item in ax.get_xticklabels()]
    #print xticklabels.iloc[0:10]
    ax.set_xticklabels(xticklabels, rotation = 90)
    plt.title(title + "\n" + x + " " + y)
    fig.savefig(ofile)
    plt.close()
    
    
def pairgrid(df, channels, ofile, frac=1, hue=None, verbose=False):
    plt.figure()

    sns.set(style="white") #no grid
    sdta = df.loc[:,channels].sample(frac=frac)
    
    if verbose:
        print 'data shape:', sdta.shape

    g = sns.PairGrid(sdta, hue=hue)
    g.map_diag(sns.kdeplot, lw=3)
    #g.map_upper(plt.scatter, alpha=0.4, marker='.')
    g.map_lower(sns.kdeplot, cmap="Blues_d", legend=False)
    g.add_legend()
    g.savefig(ofile)
    plt.close()
    
    

