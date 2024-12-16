# NASA Battery Aging Analysis

## Project Overview
This project visualizes the aging characteristics of Li-ion batteries using the NASA Battery Dataset, focusing on key electrochemical impedance parameters during charge and discharge cycles.

### Dataset Source
[NASA Battery Dataset on Kaggle](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset/data)

## Key Features
- Interactive battery parameter visualizations
- Tracking battery aging through impedance measurements
- Plotly-based interactive charts

## Parameters Analyzed
- **Re (Electrolyte Resistance)**: Measures the resistance of the battery's electrolyte
- **Rct (Charge Transfer Resistance)**: Indicates the resistance to charge transfer at the electrode-electrolyte interface
- **Capacity**: Battery capacity changes over cycling

## Technologies Used
- Python
- Pandas
- Plotly
- Streamlit

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
git clone https://github.com/yourusername/nasa-battery-aging-analysis.git
cd nasa-battery-aging-analysis
pip install -r requirements.txt
```

### Requirements File (requirements.txt)
```
pandas
plotly
streamlit
```

## Usage
```bash
streamlit run app.py
```

## Key Insights
Battery aging is characterized by:
- Increasing electrolyte resistance (Re)
- Increasing charge transfer resistance (Rct)
- Gradual capacity degradation

## License
[Specify License - e.g., MIT]

## Acknowledgments
- NASA for providing the battery dataset
- Kaggle for hosting the dataset

## Contributing
Contributions, issues, and feature requests are welcome!
