# synthetic-geo-data
# Synthetic Geographic Data Generator & Mapping

This project creates a synthetic geographic dataset (population, services, and infrastructure distribution), visualizes it on a simple map, and demonstrates a reproducible data workflow using Python.

The goal is to show how synthetic data can be generated, cleaned, analyzed, and visualized without relying on external real-world datasets. This makes the project portable, safe to share, and easy to extend.

---

## 🔍 Features

- **Synthetic data generation** for:
  - population counts
  - coordinates / regions
  - education and service indicators
  - random demographic attributes

- **Geospatial processing** using Python

- **Visualizations**, including:
  - heatmaps
  - point maps
  - region-level aggregations

- **Fully reproducible notebook** (Colab or Jupyter)

---

## 🧪 Technologies Used
- Python  
- NumPy  
- Pandas  
- Matplotlib / Plotly  
- (Optional) GeoPandas / Folium  
- Jupyter / Google Colab  

---

## 📁 Repository Structure

synthetic-geo-data/
│
├── data/
│ └── synthetic_dataset.csv
│
├── notebooks/
│ └── synthetic_geo_data.ipynb
│
├── src/
│ ├── generator.py # data generator
│ ├── visualizations.py # map functions
│ └── utils.py
│
└── README.md


---

## 🚀 How to Run

### Option 1 — Google Colab
Open the notebook directly in Colab and run all cells.

### Option 2 — Local (Jupyter)
```bash
pip install -r requirements.txt
jupyter notebook
