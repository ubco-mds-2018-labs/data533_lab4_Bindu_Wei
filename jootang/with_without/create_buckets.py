import numpy as np

def buckets(x, nbuckets = 5):
    
    try:
        x = np.array(x)
    except TypeError:
        print("Ensure that the input array is either a list or a numpy array")
    else:

        # Create a list to store output
        x_bucket = []

        max_val = max(x)
        min_val = min(x)

        try:
            bucket_size = (max_val - min_val)/nbuckets
        except TypeError:
            print("Ensure that the number of buckets in input is an integer")
        else:

            limits = [min_val]
            for i in range(1,nbuckets+1):
                limits.append(limits[i-1]+bucket_size)
            limits[-1] = max_val

            for number in x:

                for i in range(len(limits)-1):

                    if number >= limits[i]:

                        lower = str(np.round(limits[i], 2))
                        upper = str(np.round(limits[i+1], 2))

                        if i == len(limits)-2 and number == limits[i+1]:
                            bucket = "["+ lower +", "+ upper +"]"
                            x_bucket.append(bucket)

                        if number < limits[i+1]:
                            if i == len(limits)-2:
                                bucket = "["+ lower +", "+ upper +"]"
                            else:
                                bucket = "["+ lower +", "+ upper +")"
                            x_bucket.append(bucket)
                    else:
                        break

            return x_bucket
