import ast
import numpy as np

from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from utils import *

class Cluster:
    def __init__(self,number_of_clusters=50):
        self.progress = 0
        self.n_clusters = number_of_clusters
        self.data_folder = os.path.join(get_directory(),"data")
        self.smiles = os.path.join(self.data_folder,"smiles.txt")
        self.clusters_file = os.path.join(self.data_folder,"clustered-data.txt")

    def collect_data(self):
        """ 
        Data Collection

        Read data from text file (Structure [[name,smiles],...]) that I previously attained from pubchempy
        
        """
        # Read data from text file (Structure [[name,smiles],...])
        with open(self.smiles,"r+",encoding="utf8") as f:
            data = ast.literal_eval(f.read())

        return data


    def compute_similarity(self,str1, str2,i,count):
        """
        Computes the similarity between two strings using the Levenshtein distance.

        Returns a similarity score between 0 and 1, where 1 indicates the strings are identical.
        """

        # Calculate the Levenshtein distance
        distance = levenshtein_distance(str1, str2)

        # Compute the similarity score
        similarity_score = 1 - (distance / max(len(str1), len(str2)))

        # Print progress if it has changed
        if self.progress != i:
            self.progress = i
            print(f"Progress: {i}/{count}")

        return similarity_score

    def create_distance_matrix(self,strings):
        """
        Creates a distance matrix for the strings using the compute_similarity function.
        """
        num_strings = len(strings)
        distances = [[self.compute_similarity(strings[i], strings[j],i,num_strings) for j in range(num_strings)] for i in range(num_strings)]
        distances = 1 - np.array(distances)
        return distances

    def cluster_strings(self,strings):
        """
        Cluster the strings using AgglomerativeClustering
        """
        
        # Create the distance matrix
        distances = self.create_distance_matrix(strings)

        # Perform clustering using AgglomerativeClustering
        clustering = AgglomerativeClustering(n_clusters=self.n_clusters, affinity='precomputed', linkage='complete')
        clustering.fit(distances)

        # Retrieve the cluster labels
        cluster_labels = clustering.labels_

        # Return the cluster labels
        return cluster_labels


    def cluster(self):
        """
        Cluster the data
        """

        # Perform clustering
        data = self.collect_data()

        # Get the smiles from data
        clustered_data = [[] for x in range(self.n_clusters)]

        # Get the smiles from data
        smiles = [x[1] for x in data]

        # Get the cluster labels
        cluster_labels = self.cluster_strings(smiles)

        # Print the cluster labels for each string
        for i, label in enumerate(cluster_labels):
            clustered_data[label].append([data[i][0],smiles[i]])

        # Write clustered data to file
        with open(self.clusters_file,"w+",encoding="utf8") as f:
            f.write(str(clustered_data))
            
        self.progress = 0
        print(f"Finished Clustering with {self.n_clusters} clusters")


        
    def get_similar_smiles(self,smile):
        """
        Get the most similar smiles to the given smile
        """
        data = []
        # Get the clustered data
        with open(self.clusters_file,"r+",encoding="utf8") as f:
            data = eval(f.read())
        
        #iterate through array of clusters and find the cluster that is most similar to the smile
        max_similarity = 0
        max_similarity_cluster = []
        # Using average similarity score
        for cluster in data:
            similarity_score = 0
            for item in cluster:
                similarity_score += self.compute_similarity(smile,item[1],0,0)
            similarity_score = similarity_score/len(cluster)
            if similarity_score > max_similarity:
                max_similarity = similarity_score
                max_similarity_cluster = cluster
        return max_similarity_cluster

