import pandas as pd
import os 
import matplotlib.pyplot as plt
import seaborn as sns

# Define directory path
data_dir = r"C:\Users\Alexis\Documents\predictive-maintenance-of-hydraulic-systems"

# Initialize sensor dictionary
sensor_data = {}

# Read each file and combine them
for filename in os.listdir(data_dir):
    if filename.endswith('.txt'):
        sensor_type = filename.split('.')[0]
        filepath = os.path.join(data_dir, filename)
        df = pd.read_csv(filepath, delimiter='\t')

        if sensor_type not in sensor_data:
            sensor_data[sensor_type] = df
        else:
            sensor_data[sensor_type] = pd.concat([sensor_data[sensor_type], df])

# Example of accessing the combined DataFrame for a specific sensor type
pressure_data = sensor_data.get('PS1')

# Example of preprocessing
def preprocess_data(df):
    df.dropna(inplace=True)  # Remove missing values
    # Add more preprocessing steps as needed
    return df

# Apply preprocessing
if pressure_data is not None:
    pressure_data = preprocess_data(pressure_data)

    # Example visualization
    plt.figure(figsize=(10, 6))
    sns.histplot(pressure_data['some_column'])  # Replace 'some_column' with an actual column name
    plt.title('Distribution of Some Column')
    plt.show()



