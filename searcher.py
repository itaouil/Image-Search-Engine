import numpy as np

# Compares image features
# and determines distance
# metrics
class Searcher:

    def __init__(self, index):
        # Initialise our index
        # features file
        self.index = index

    def search(self, queryFeatures):

        # Results dictionary
        results = {}

        # Loop over features
        for (k, features)  in self.index.items():
            # Compute chi-squared distance metrics
            d = self.chi2_distance(features, queryFeatures)

            # Update distance results
            results[k] = d

        # Sort results with
        # smallest distace first
        results = sorted([(v,k) for (k,v) in results.items()])

        return results

    def chi2_distance(self, histA, histB, eps = 1e-10):
        # compute the chi-squared distance
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])

        # return the chi-squared distance
        return d
