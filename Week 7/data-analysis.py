import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

class DataAnalyzer:
    def __init__(self):
        self.data = None
        self.features = None
        
    def load_iris_dataset(self):
        """Load the Iris dataset and convert to pandas DataFrame"""
        try:
            iris = load_iris()
            self.data = pd.DataFrame(
                data=np.c_[iris['data'], iris['target']],
                columns=[*iris['feature_names'], 'target']
            )
            # Convert target numbers to species names
            species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
            self.data['species'] = self.data['target'].map(species_map)
            self.features = iris['feature_names']
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading dataset: {e}")
            
    def explore_data(self):
        """Basic data exploration"""
        print("\nFirst 5 rows of the dataset:")
        print(self.data.head())
        
        print("\nDataset Info:")
        print(self.data.info())
        
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        
        print("\nBasic Statistics:")
        print(self.data.describe())
        
    def analyze_by_species(self):
        """Group analysis by species"""
        print("\nMean values by species:")
        grouped_stats = self.data.groupby('species')[self.features].mean()
        print(grouped_stats)
        return grouped_stats
        
    def create_visualizations(self):
        """Create required visualizations"""
        # Set style
        plt.style.use('seaborn')
        
        # 1. Line Chart
        plt.figure(figsize=(10, 6))
        for species in self.data['species'].unique():
            species_data = self.data[self.data['species'] == species]
            plt.plot(range(len(species_data)), 
                    species_data['sepal length (cm)'], 
                    label=species)
        plt.title('Sepal Length Trends by Species')
        plt.xlabel('Sample Index')
        plt.ylabel('Sepal Length (cm)')
        plt.legend()
        plt.savefig('line_chart.png')
        plt.close()
        
        # 2. Bar Chart
        plt.figure(figsize=(10, 6))
        grouped_stats = self.analyze_by_species()
        grouped_stats['petal length (cm)'].plot(kind='bar')
        plt.title('Average Petal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Petal Length (cm)')
        plt.tight_layout()
        plt.savefig('bar_chart.png')
        plt.close()
        
        # 3. Histogram
        plt.figure(figsize=(10, 6))
        for species in self.data['species'].unique():
            species_data = self.data[self.data['species'] == species]
            plt.hist(species_data['sepal width (cm)'], 
                    alpha=0.5, 
                    label=species, 
                    bins=15)
        plt.title('Distribution of Sepal Width')
        plt.xlabel('Sepal Width (cm)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.savefig('histogram.png')
        plt.close()
        
        # 4. Scatter Plot
        plt.figure(figsize=(10, 6))
        for species in self.data['species'].unique():
            species_data = self.data[self.data['species'] == species]
            plt.scatter(species_data['sepal length (cm)'],
                       species_data['petal length (cm)'],
                       label=species,
                       alpha=0.6)
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend()
        plt.savefig('scatter_plot.png')
        plt.close()

def main():
    # Initialize analyzer
    analyzer = DataAnalyzer()
    
    # Load dataset
    analyzer.load_iris_dataset()
    
    # Perform analysis
    analyzer.explore_data()
    analyzer.analyze_by_species()
    
    # Create visualizations
    analyzer.create_visualizations()
    
    print("\nAnalysis complete! Visualization files have been saved.")

if __name__ == "__main__":
    main() 