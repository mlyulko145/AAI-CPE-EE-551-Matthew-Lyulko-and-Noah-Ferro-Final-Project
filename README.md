# AAI-CPE-EE-551-Matthew-Lyulko-and-Noah-Ferro-Final-Project
# Grocery Value Analyzer

## Team Members

- Matthew Lyulko (mlyulko@stevens.edu)
- Noah Ferro (nferro@stevens.edu)

## Problem Description

Grocery prices vary significantly across stores, and consumers often struggle to determine which items provide the best overall value when considering price, necessity, and shelf life. This project addresses this real-world problem by analyzing grocery pricing data and computing a composite quality score for grocery items.

The Grocery Value Analyzer combines:

   - Item price relative to the average price

   - Consumer-rated necessity scores

   - Product expiration duration

to produce a normalized quality score that helps identify the best value grocery items and compare store performance.

## Data Source 

The datasets used in this project are created by us using data found on the stores online page and then put into CSV files. They simulate realistic grocery pricing and necessity rankings.

Files:

   - data/prices.csv
     
   - data/necessity_survey.csv
     
## Program Structure

- `notebook/finalprojectmain.ipynb`: Main analysis and visualization
- `src/food_item.py`: FoodItem class
- `src/quality_metric.py`: QualityMetric class
- `src/utils.py`: Helper functions
- `src/main.py` : Extra entry point
- `data/`: CSV input datasets
- `tests/`: Pytest unit tests

## How to Run

1. Clone the repository
2. Open `notebook/finalprojectmain.ipynb`using Jupyter Notebook
3. Run all cells
4. View:
   - Ranked grocery items by quality score
     
   - Average quality score per store visualization
5. Run tests with:
   ```bash
   pytest

## Visualization Output

The program generates a bar chart showing the average quality score per store, enabling direct comparison of grocery stores based on overall value rather than price alone.

## Team Contributions

Matthew Lyulko

1. Dataset design and preprocessing

2. Core analysis logic in the Jupyter Notebook

3. Data visualization and result interpretation

4. Integration testing and debugging

5. Object-oriented class design

6. Quality metric formulation

7. Utility function development

8. Pytest unit test creation

## Python Version

Developed and tested using Python 3.12 / 3.13.
