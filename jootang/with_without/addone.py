# Load required libraries
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Inheritance from the other module
from .create_buckets import buckets


def addone(df, response, nbuckets = 5):

    # Fit a linear regression model with all the variables in given dataframe as predictors

    try:
        # Response variable in y
        y = pd.DataFrame(df[response])
    except KeyError:
        print("Ensure that the response variable is present in the data")
    else:

        # Predictors in X
        predictors = list(df.columns)
        predictors.remove(response)
        X = df[predictors]

        # Model fit
        lm = linear_model.LinearRegression()
        model = lm.fit(X,y)

        # Store the predicted values in a new column
        predicted_all = model.predict(X)
        df['predict_all'] = predicted_all


        # Loop through each one of the predictor variables
        for predictor in predictors:

            # Create new column for bucket of the corresponding predictor variable.
            new_colname = predictor + '_bkt'
            new_col = buckets(df[predictor], nbuckets)
            df['%s' %(new_colname)] = new_col

            # Create a list of predictor variable names other than one predictor each time.
            predictors_without_one = predictors.copy()
            predictors_without_one.remove(predictor)

            # Fit a linear regression model with all the variables except one.
            X_without_one = df[predictors_without_one]
            model_without_one = lm.fit(X_without_one, y)

            # Compute predicted values using this model and store them in a new column.
            predicted_values = model_without_one.predict(X_without_one)
            new_col_name1 = predictor + '_predict_wo'
            df['%s' %(new_col_name1)] = predicted_values


            # For plotting, group by each bucket of predictor to compute the mean value of response variable

            # For model WITH all the variables
            df1 = df.groupby('%s' %(new_colname))['predict_all'].agg('mean')

            # For model WITHOUT one variable
            df2 = df.groupby('%s' %(new_colname))['%s' %(new_col_name1)].agg('mean')

            # For ACTUAL values of response variable
            df3 = df.groupby('%s' %(new_colname))[response].agg('mean')

            # Plot line plots to show the impact of each variable on model fit
            # (One plot for each predictor)
            print(predictor)
            plt.plot(df1.index, df1.values, color = 'red', label = "predicted with")
            plt.plot(df2.index, df2.values, color = 'black', label = "predicted without")
            plt.plot(df3.index, df3.values, color = 'green', label = "actual values")
            plt.xlabel("Buckets of %s" %(predictor))
            plt.ylabel("Mean of %s" %(response))
            plt.legend()
            plt.show()

        return list(np.round(df2.values, 2))
