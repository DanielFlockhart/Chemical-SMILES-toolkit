import ast
import numpy as np
# Get the levenshtein_distanct(str1,str2) function from utils package from the parent directory


from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from utils import levenshtein_distance

data_folder = r"C:\Users\0xdan\Documents\CS\Catergories\Healthcare_Medical\Drug Discovery\DrugInteractions\data"
data_file = fr"{data_folder}\smiles.txt"
p = 0
def collect_data():
    """ 
    Data Collection

    Read data from text file (Structure [[name,smiles],...]) that I previously webscraped from pubchempy
    Note To Self : include webscraping in this file
       
    """
    # Read data from text file (Structure [[name,smiles],...])
    with open(data_file,"r+",encoding="utf8") as f:
        data = ast.literal_eval(f.read())

        
    return data


def compute_similarity(str1, str2,i,count):
    global p
    """
    Computes the similarity between two strings using the Levenshtein distance.

    Returns a similarity score between 0 and 1, where 1 indicates the strings are identical.
    """

    # Calculate the Levenshtein distance
    distance = levenshtein_distance(str1, str2)

    # Compute the similarity score
    similarity_score = 1 - (distance / max(len(str1), len(str2)))
    if p != i:
        p = i
        print(f"Progress: {i}/{count}")

    return similarity_score

def create_distance_matrix(strings):
    """
    Creates a distance matrix for the strings using the compute_similarity function.
    """
    num_strings = len(strings)
    distances = [[compute_similarity(strings[i], strings[j],i,num_strings) for j in range(num_strings)] for i in range(num_strings)]
    distances = 1 - np.array(distances)
    return distances

def cluster_strings(strings, num_clusters):
    # Create the distance matrix
    distances = create_distance_matrix(strings)

    # Perform clustering using AgglomerativeClustering
    clustering = AgglomerativeClustering(n_clusters=num_clusters, affinity='precomputed', linkage='complete')
    clustering.fit(distances)
    clustering

    # Retrieve the cluster labels
    
    cluster_labels = clustering.labels_

    # Return the cluster labels
    return cluster_labels


def cluster(number_of_clusters):
    global p
    # Set the number of clusters, Just an estimation for now, would use elbow method to find optimal number

    # Perform clustering
    data = collect_data()
    # Get the smiles from data
    clustered_data = [[] for x in range(number_of_clusters)]
    smiles = [x[1] for x in data]
    cluster_labels = cluster_strings(smiles, number_of_clusters)
    # Print the cluster labels for each string
    for i, label in enumerate(cluster_labels):
        clustered_data[label].append([data[i][0],smiles[i]])

    # Write clustered data to file
    with open(fr"{data_folder}\clustered_data{number_of_clusters}.txt","w+",encoding="utf8") as f:
        f.write(str(clustered_data))
    # Print progress if it has changed
    
    p = 0
    print(f"Finished Clustering with {number_of_clusters} clusters")

# def evaluation():
#     # Evaluate clusters to workout the best number of clusters to use. Using Silhouette Coefficient
    

#     # Initialize an empty list to store the silhouette scores
    

#     # Evaluate the clustering results for each cluster number
#     for n_clusters in range(min_clusters, max_clusters+1):
#         # Create an instance of AgglomerativeClustering
#         clustering = AgglomerativeClustering(n_clusters=n_clusters)
        
#         # Fit the model and predict the clusters
#         labels = clustering.fit_predict(X)
        
#         # Calculate the silhouette score
#         silhouette = silhouette_score(X, labels)
        
#         # Append the score to the list
#         silhouette_scores.append(silhouette)

#     # Print the silhouette scores for each cluster number
#     for n_clusters, silhouette in zip(range(min_clusters, max_clusters+1), silhouette_scores):
#         print(f"Number of clusters: {n_clusters}")
#         print(f"Silhouette score: {silhouette}")
#         print()

#     # Plot the silhouette scores to visualize the results
#     plt.plot(range(min_clusters, max_clusters+1), silhouette_scores)
#     plt.xlabel("Number of clusters")
#     plt.ylabel("Silhouette score")
#     plt.show()
    
def get_similar_smiles(smile,data_folder):
    data = []
    # Get the clustered data from clustered_data100.txt
    with open(fr"{data_folder}\clustered_data100.txt","r+",encoding="utf8") as f:
        data = eval(f.read())
    
    #iterate through array of clusters and find the cluster that is most similar to the smile
    max_similarity = 0
    max_similarity_cluster = []
    # Using average similarity score
    for cluster in data:
        similarity_score = 0
        for item in cluster:
            similarity_score += compute_similarity(smile,item[1],0,0)
        similarity_score = similarity_score/len(cluster)
        if similarity_score > max_similarity:
            max_similarity = similarity_score
            max_similarity_cluster = cluster
    return max_similarity_cluster


if __name__ == "__main__":
    cluster(100)

