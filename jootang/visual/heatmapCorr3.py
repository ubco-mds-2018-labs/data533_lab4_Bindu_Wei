import numpy as np
import matplotlib.pyplot as plt

def heatmapCorr3(df,colname1,colname2,colname3):
    #calculate correlation
    try:
        matrix = np.round(df[[colname1,colname2,colname3]].corr(),2)
    
        
        col = [None]*3


        try:
            #for element of matrix[0][1], same for matrix[1][0]
            #strong postive correlation
            if matrix.iloc[0,1] >= 0.5 and matrix.iloc[0,1] < 1:
                col[0] = 'firebrick'
            #weak postive correlation
            if matrix.iloc[0,1] >= 0 and matrix.iloc[0,1] < 0.5:
                col[0] = 'mistyrose'
            #strong negative correlation
            if matrix.iloc[0,1] < -0.5:
                col[0] = 'lightcoral'
            #weak negative correlation
            if matrix.iloc[0,1] >= -0.5 and matrix.iloc[0,1] < 0:
                col[0] = 'indianred'

            #for element of matrix[0][2], same for matrix[2][0]
                #strong postive correlation
            if matrix.iloc[0,2] >= 0.5 and matrix.iloc[0,2] < 1:
                col[1] = 'firebrick'
            #weak postive correlation
            if matrix.iloc[0,2] >= 0 and matrix.iloc[0,2] < 0.5:
                col[1] = 'mistyrose'
            #strong negative correlation
            if matrix.iloc[0,2] < -0.5:
                col[1] = 'lightcoral'
            #weak negative correlation
            if matrix.iloc[0,2] >= -0.5 and matrix.iloc[0,2] < 0:
                col[1] = 'indianred'

            #for element of matrix[1][2], same for matrix[2][1]
            if matrix.iloc[1,2] >= 0.5 and matrix.iloc[1,2] < 1:
                col[2] = 'firebrick'
            #weak postive correlation
            if matrix.iloc[1,2] >= 0 and matrix.iloc[1,2] < 0.5:
                col[2] = 'mistyrose'
            #strong negative correlation
            if matrix.iloc[1,2] < -0.5:
                col[2] = 'lightcoral'
            #weak negative correlation
            if matrix.iloc[1,2] >= -0.5 and matrix.iloc[1,2] < 0:
                col[2] = 'indianred'
        except ValueError as err:
            print("Unable to assign colour. Error: err")


        #plot heatmap: closer to 1, darker colour, shows a higher positive correlation
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.axis('off')

        #matrix[1][1]
        rect1 = plt.Rectangle((0.35, 0.4), 0.25, 0.25, color='maroon', alpha=0.3)
        plt.text(0.47, 0.52, '1', size=10)

        #matrix[1][2] 
        rect2 = plt.Rectangle((0.35, 0.15), 0.25, 0.25, color=col[2], alpha=0.3)
        plt.text(0.7, 0.52, matrix.iloc[1,2], size=10)

        #matrix[2][1]                             
        rect3 = plt.Rectangle((0.6, 0.4), 0.25, 0.25, color=col[2], alpha=0.3)
        plt.text(0.45, 0.27, matrix.iloc[2,1], size=10)

        #matrix[2][2]                             
        rect4 = plt.Rectangle((0.6, 0.15), 0.25, 0.25, color='maroon', alpha=0.3)
        plt.text(0.72, 0.27, '1', size=10)

        #matrix[0][0]                          
        rect5 = plt.Rectangle((0.1, 0.65), 0.25, 0.25, color='maroon', alpha=0.3)
        plt.text(0.22, 0.77, '1', size=10)

        #matrix[0][1]                              
        rect6 = plt.Rectangle((0.35, 0.65), 0.25, 0.25, color=col[0], alpha=0.3)
        plt.text(0.45, 0.77, matrix.iloc[1,0], size=10)

        #matrix[1][0]   
        rect8 = plt.Rectangle((0.1, 0.4), 0.25, 0.25, color=col[0], alpha=0.3)
        plt.text(0.2, 0.52, matrix.iloc[1,0], size=10)

        #matrix[0][2]
        rect7 = plt.Rectangle((0.6, 0.65), 0.25, 0.25, color=col[1], alpha=0.3)
        plt.text(0.7, 0.77, matrix.iloc[0,2], size=10)

        #matrix[2][0]
        rect9 = plt.Rectangle((0.1, 0.15), 0.25, 0.25, color=col[1], alpha=0.3)
        plt.text(0.2, 0.27, matrix.iloc[2,0], size=10)


        ax.add_patch(rect1)
        ax.add_patch(rect2)
        ax.add_patch(rect3)
        ax.add_patch(rect4)
        ax.add_patch(rect5)
        ax.add_patch(rect6)
        ax.add_patch(rect7)
        ax.add_patch(rect8)
        ax.add_patch(rect9)


        plt.text(0.18, 0.92, colname1, fontname='Comic Sans MS', size=13)
        plt.text(0.44, 0.92, colname2, fontname='Comic Sans MS', size=13)
        plt.text(0.67, 0.92, colname3, fontname='Comic Sans MS', size=13)
        plt.text(0.01, 0.78, colname1, fontname='Comic Sans MS', size=13)
        plt.text(0.01, 0.52, colname2, fontname='Comic Sans MS', size=13)
        plt.text(-.01, 0.24, colname3, fontname='Comic Sans MS', size=13)

        return matrix

    except:
        print('Please check selected columns: same length, no null, within data frame.')
