🌲 CaliforniaWildfires
A geospatial machine learning system for predicting property damage risk from California wildfires — expanded beyond UCD’s COMP47350 coursework.

This project builds on the initial COMP47350 assignment, which focused on binary classification of wildfire damage using a subset of CAL FIRE’s public Damage Inspection (DINS) dataset. The original work trained and evaluated linear regression, logistic regression, and random forest models to predict whether a structure would be “No Damage” or “Destroyed (>50%)” based on descriptive features.

In this expanded version, the scope moves from binary risk classification to dollar‑value damage estimation and geospatial risk mapping. The system integrates multiple open datasets — CAL FIRE fire perimeters, NOAA historical weather, USGS vegetation indices (NDVI), and property value data — to model wildfire impact at a given location and time.

Key Features

Data Engineering: Automated ETL from CAL FIRE, NOAA, and USGS, with spatial joins in GeoPandas/PostGIS to link weather, vegetation, and property features to fire incidents.

Feature Engineering: Burn history, vegetation health, property density, distance to nearest historical fire, weather variables, and seasonality indicators.

Modeling: LightGBM regression with temporal validation to predict expected property loss in USD; performance tracked via RMSE, MAE, and R².

API Service: Flask/FastAPI /predict endpoint accepts latitude, longitude, date, and conditions to return estimated damage value.

Visualization: Interactive Folium/Leaflet map displaying predicted high‑risk zones, color‑coded by expected loss.

Deployment: Dockerized service with CI/CD via GitHub Actions; can be run locally or hosted on Render/Heroku.

Explainability: Feature importance charts and contextual “why” explanations for each prediction.

Tech Stack
Python · pandas · geopandas · scikit‑learn · LightGBM · PostGIS · Flask/FastAPI · Folium · Docker · GitHub Actions

Potential Applications

Insurance underwriting and premium pricing in wildfire‑prone areas.

Urban planning and zoning risk assessments.

Emergency services resource allocation.
