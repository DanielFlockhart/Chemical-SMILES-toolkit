# Chemical Compound Clustering

This Python project aims to cluster chemical compounds based on their SMILES (Simplified Molecular Input Line Entry System) representation and provides a user-friendly interface to input a SMILES string and obtain a cluster of similar chemicals along with their respective SMILES.

There is no requirement to cluster the default data on first use, it has already been clustered using 100 clusters.

## Features

The project consists of the following main components:

1. **Webscraping**: The project includes a webscraping module that fetches drug SMILES and names from reliable sources. This data will serve as the basis for chemical compound clustering.

2. **Clustering**: The clustering module utilizes agglomerative clustering with levenshtein distance to cluster the chemical compounds based on their SMILES. It computes the similarity between compounds and assigns them to appropriate clusters.

3. I intend to add a feature that allows the conversion of canonical smiles to 2D structures to help users visualise the chemical structures.
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielFlockhart/Chemical-SMILES-toolkit.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Chemical-SMILES-toolkit
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



2. Launch the program:

   ```bash
   python main.py
   ```

   The UI will be displayed (When complete), allowing users to either input a SMILES string and retrieve a cluster of similar chemicals along with their respective SMILES, recluster the data with a different number of clusters or use a different dataset.

## Contribution

Contributions to this project are welcome! If you have any suggestions, improvements, or new features to propose, please submit a pull request. You can also report any issues or bugs by opening an issue on the project's GitHub repository.

When contributing, please follow the existing code style, write clear and concise commit messages, and provide appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Credits

The project acknowledges the following resources for their contributions:

- [PubChem](https://pubchem.ncbi.nlm.nih.gov/) - Data source for drug SMILES and names

Thank you for using the Chemical SMILES toolkit project! We hope it proves to be useful for your chemical analysis and research.