
![Disaster Image](https://cdn.pixabay.com/photo/2020/04/27/14/57/virus-5100206_1280.jpg)
<h3 align="center">1990-2023 Vaccine Analytics</h3>
<p align="center">
A deeper understanding of the relationship between Vaccine, Patients and Symptoms.
<br>
  <a href="https://vaers.hhs.gov/data/datasets.html"><strong>Explore VAERS Data Sets »</strong></a>
</p>

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
To install this project and its dependencies, follow these steps:
1. If you haven't already, install poetry by running the following command:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
Alternatively, you can install poetry using pip:
```angular2html
pip install poetry
```
2. Clone this repository:
```angular2html
git clone https://github.com/tmkhang1999/1990-2023-Vaccine-Analytics.git
```
3. Install the project's dependencies with poetry:
```angular2html
poetry install
```
This will create a new virtual environment for the project and install all of its dependencies, using the information from the poetry.toml and poetry.lock files in the project directory.

## Project Motivation<a name="motivation"></a>
The COVID-19 pandemic has highlighted the importance of vaccine safety and monitoring adverse events. The Vaccine Adverse Event Reporting System (VAERS) is a vital tool for monitoring vaccine safety in the United States. However, the massive amount of data available in VAERS can be overwhelming, and extracting meaningful insights requires specialized skills and tools.

This project aims to analyze real-world VAERS datasets to gain insights into the distribution of adverse events by vaccine type, age, sex, symptoms, and death status. The project utilizes advanced analytical techniques such as Apriori/Fpgrowth algorithms to discover significant Association Rules between these variables.

The project's primary goal is to provide a user-friendly and interactive dashboard that visualizes the number of cases in each vaccine type and associations between the number of deaths, vaccine type, and state based on age/year. 

By providing actionable insights into VAERS data, this project can contribute to improving vaccine safety monitoring and ultimately enhance public health.

## File Descriptions <a name="files"></a>
The 'Vaccine.ipynb' file includes all the steps taken to explore that. It covers data combining, data cleaning and preprocessing, data visualization, and drawing conclusions from the data.

In each year, there are three dataset files:
1. VAERSDATA.csv: contains information about the reported adverse events, including patient demographics, vaccine information, and adverse event details.

2. VAERSVAX.csv: contains information about specific vaccine products, such as manufacturer, product type, and lot number.

3. VAERSSYMPTOMS.csv: contains details about reported symptoms, including onset date, duration, severity, and a list of symptoms for each adverse event.
## Results<a name="results"></a>
https://user-images.githubusercontent.com/74235084/224438080-453d8248-2fe8-4df3-bb68-e4a977bc4a52.mp4

## Acknowledgements<a name="licensing"></a>
We would like to acknowledge the CDC for providing the VAERS dataset and making it available to the public for research purposes.
