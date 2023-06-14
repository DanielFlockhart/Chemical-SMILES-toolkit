# Chemical Compound Clustering

This Python project aims to cluster chemical compounds based on their SMILES (Simplified Molecular Input Line Entry System) representation. It provides a user-friendly interface to input a SMILES string and obtain a cluster of similar chemicals along with their respective SMILES.

There is no requirement to rerun the dataset.py, cluster.py or evaluation.py files for the purpose of testing the software unless you wish to cluster a different dataset.

## Features

The project consists of the following main components:

1. **Webscraping**: The project includes a webscraping module that fetches drug SMILES and names from reliable sources. This data will serve as the basis for chemical compound clustering.

2. **Clustering**: The clustering module utilizes a suitable algorithm (e.g., k-means) to cluster the chemical compounds based on their SMILES. It computes the similarity between compounds and assigns them to appropriate clusters.

3. **Evaluation**: The evaluation module implements the elbow method to determine the optimal number of clusters for the given dataset. This process helps in finding the most meaningful and representative clusters.

4. **User Interface (UI)**: The project provides a user interface that allows users to input a SMILES string and retrieves a cluster of similar chemicals. The UI offers a seamless and intuitive way for users to interact with the clustering functionality.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielFlockhart/chemical-compound-clustering.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chemical-compound-clustering
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. In the case you want to use your own dataset please upload your txt of chemical names in the form. If you only wish to test the software, please skip to step 4.
   
   drugs.txt
   ```
   chemical_name_1
   chemical_name_2
   ...
   ```

2. In the case you want to use your own dataset:

   ```bash
   python webscraping.py
   ```

   This will collect the necessary data from reliable sources and store it for further processing.

2. Cluster the chemical compounds using the provided smiles:

   ```bash
   python clustering.py
   ```

   This will use the collected SMILES data to cluster the chemical compounds using an appropriate algorithm.

3. Evaluate the clusters to determine the optimal number of clusters:

   ```bash
   python evaluation.py
   ```

   The evaluation module applies the elbow method to find the best number of clusters based on the given data.

4. Launch the user interface:

   ```bash
   python ui.py
   ```

   The UI will be displayed, allowing users to input a SMILES string and retrieve a cluster of similar chemicals along with their respective SMILES.

## Contribution

Contributions to this project are welcome! If you have any suggestions, improvements, or new features to propose, please submit a pull request. You can also report any issues or bugs by opening an issue on the project's GitHub repository.

When contributing, please follow the existing code style, write clear and concise commit messages, and provide appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Credits

The project acknowledges the following resources for their valuable contributions:

- [Source 1](https://example.com) - Data source for drug SMILES and names
- [Source 2](https://example.com) - Data source for drug SMILES and names

Thank you for using our Chemical Compound Clustering project! We hope it proves to be useful for your chemical analysis and research.