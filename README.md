# Predictive Maintenance of Hydraulic Systems

This project focuses on predicting hydraulic system failures using time-series sensor data and anomaly detection models. The project uses ARIMA and SARIMA models for forecasting and anomaly detection, as well as RandomForestClassifier to identify key features that predict system failures.

## Key Results

- **Feature Importance**: The top 10 most important features identified by the Random Forest model were mainly pressure sensors, including:
  1. Pressure_Sensor_56
  2. Pressure_Sensor_7
  3. Pressure_Sensor_11
  4. Pressure_Sensor_30
  5. Pressure_Sensor_13
  6. Pressure_Sensor_6

- **Model Accuracy**: The RandomForest model achieved 99% accuracy in predicting cooler failure.

- **Visualizations**:
  - [Feature Importance](Visuals/bar_plot.png)
  - [Confusion Matrix](Visuals/confusion_matrix.png)
  - [Time-Series Data](Visuals/Time_Series.png)
  - [Auto ARIMA Forecast](Visuals/Auto_Arima.png)
  - [Manual SARIMA Forecast](Visuals/Manual_Sarima.png)

## How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/Smolbitties/predictive-maintenance-of-hydraulic-systems.git
    ```

2. Install dependencies:
    ```bash
    conda activate <environment-name>
    pip install -r requirements.txt
    ```

3. Run the Jupyter notebooks for analysis:
    ```bash
    jupyter notebook Notebooks/data_analysis_with_markdown.ipynb
    ```

4. View the visualizations in the `Visuals/` folder.

## Future Improvements

- Collecting additional data for model refinement.
- Exploring different machine learning algorithms for better predictions.
