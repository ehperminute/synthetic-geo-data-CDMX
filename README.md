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
│   ├── raw/           # colonia boundaries, alcaldía shapes
│   ├── interim/       # merged geodata
│   └── processed/     # generated synthetic students + tables
│
├── notebooks/
│   └── education_analytics_simulation.ipynb   # clean Colab notebook
│
├── src/
│   ├── generate_population.py
│   ├── simulate_dropout.py
│   ├── geospatial_processing.py
│   ├── visualizations.py
│   └── utils.py
│
├── requirements.txt
└── README.md



---

## 🚀 How to Run

### Option 1 — Google Colab
Open the notebook directly in Colab and run all cells.

### Option 2 — Local (Jupyter)
```bash
pip install -r requirements.txt
jupyter notebook
