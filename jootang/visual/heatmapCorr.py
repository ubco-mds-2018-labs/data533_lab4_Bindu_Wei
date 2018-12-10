import numpy as np
import matplotlib.pyplot as plt

def heatmapCorr(df, colname1, colname2):
    #calculate correlation
    try:
        list1 = df[colname1]
        list2 = df[colname2]
    
        try:
            matrix = np.round(np.corrcoef(list1, list2),2)
        except:
            print('Please drop null values in selected columns and make sure two columns have same length.')

        #for element of matrix[0][1], same for matrix[1][0]
        #strong postive correlation
        if matrix[0][1] >= 0.5 and matrix[0][1] < 1:
            col = 'firebrick'
        #weak postive correlation
        if matrix[0][1] >= 0 and matrix[0][1] < 0.5:
            col = 'mistyrose'
        #strong negative correlation
        if matrix[0][1] < -0.5:
            col = 'lightcoral'
        #weak negative correlation
        if matrix[0][1] >= -0.5 and matrix[0][1] < 0:
            col = 'indianred'


        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.axis('off')
        rect1 = plt.Rectangle((0.25, 0.5), 0.25, 0.25, color='maroon', alpha=0.3)
        plt.text(0.38, 0.6, '1', size=10)
        rect2 = plt.Rectangle((0.25, 0.25), 0.25, 0.25, color=col, alpha=0.3)
        plt.text(0.35, 0.35, matrix[1][0], size=10)
        rect3 = plt.Rectangle((0.5, 0.5), 0.25, 0.25, color=col, alpha=0.3)
        plt.text(0.6, 0.6, matrix[1][0], size=10)
        rect4 = plt.Rectangle((0.5, 0.25), 0.25, 0.25, color='maroon', alpha=0.3)
        plt.text(0.62, 0.35, '1', size=10)

        plt.text(0.33, 0.8, colname1, size=15)
        plt.text(0.58, 0.8, colname2, size=15)
        plt.text(0.13, 0.6, colname1, size=15)
        plt.text(0.13, 0.37, colname2, size=15)
        ax.add_patch(rect1)
        ax.add_patch(rect2)
        ax.add_patch(rect3)
        ax.add_patch(rect4)
        
        return matrix
    except:
        print('Please enter column names within data frame.')
    
    
