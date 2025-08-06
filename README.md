# 🌲 California Wildfires

**A geospatial machine learning system for predicting property damage risk from California wildfires - expanded beyond UCD’s COMP47350 coursework.**

---

## 📚 Project Overview
This project builds on the initial **COMP47350** assignment, which focused on binary classification of wildfire damage using a subset of CAL FIRE’s public [Damage Inspection (DINS)](https://data.ca.gov/dataset/cal-fire-damage-inspection-dins-data) dataset.  
The original work trained and evaluated linear regression, logistic regression, and random forest models to predict whether a structure would be **“No Damage”** or **“Destroyed (>50%)”** based on descriptive features.

The expanded version moves from binary classification to dollar-value damage estimation and geospatial risk mapping. It integrates multiple data sources to model wildfire impact at a given location and time, including fire perimeters, weather data, vegetation indices, and property value data.


### Key Features:
- **Dollar-value damage estimation**: Predict the financial loss associated with property damage caused by wildfires.
- **Geospatial risk mapping**: Visualize wildfire risk across California, helping to understand areas vulnerable to significant damage.
- **Comprehensive data integration**: Combines multiple datasets for more accurate and dynamic predictions of wildfire impact.

### Data Sources:
- **CAL FIRE Damage Inspection (DINS)**: Publicly available damage reports detailing the severity of destruction caused by wildfires.
- **NOAA Historical Weather Data**: Temperature, humidity, and precipitation data that helps predict fire spread and severity.
- **USGS Vegetation Indices (NDVI)**: Vegetation health data used to estimate fuel load and fire risk.
- **Property Value Data**: Real estate pricing data to estimate the financial impact of damage to properties.
- **Topographic Data**: Elevation and slope data from USGS to assess how terrain influences fire spread.
- **Census Data**: Population density and housing types to understand the human impact of wildfires.

---

## 📁 Project Structure

```
├── apps/
│   ├── frontend/               
│   └── backend/                

├── data/                       # Data science & ML models

├── packages/
│   └── shared/                 # Shared code between apps

└── README.md                   # This file
```

---
