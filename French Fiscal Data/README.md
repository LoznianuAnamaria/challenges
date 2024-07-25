# French Fiscal AI Innovation and Prediction Challenge


This challenge is posted by Ocean Protocol and hosted on Desights. For more information, visit the [Desights Challenge Page](https://competitions.desights.ai/challenge/26).

This repository contains all the data and analysis for the French Fiscal AI Innovation and Prediction Challenge, held in collaboration with the Joint Research Centre (JRC), the Science Hub of the European Union Commission.

## Overview

The challenge presents a unique opportunity to examine 40 years of French tax data, aiming to enhance data-driven decision-making for EU policymakers. Participants will employ their analytical and predictive modeling skills to reveal significant insights into the fiscal behaviors of French municipalities.

## Challenge Objectives

- Rank municipalities by their tax revenue to identify those with the highest income from direct local taxes.
- Rank departments by their tax revenue.
- Create graphical representations to illustrate revenue trends in selected towns.
- Classify municipalities based on their growth in tax revenues over various periods.
- Investigate the relationship between population size and tax revenue.
- Assess the impact of eliminating the professional tax collected before 2010.

## Dataset

The dataset is an aggregation of French REI (Répertoire des Élus et des Institutions) data files, offering detailed financial and administrative information on French municipalities. It was downloaded locally as a Parquet file and utilized for further analysis.


## Files Included
- [Complete Report](French%20Fiscal%20Data%20Analysis.pdf)
- [Notebooks](notebooks/)
- [CompetitionDetails](CompetitionDetails.pdf) - Details about the competition and instructions about data retrieval.

# Note
There are 16 notebooks that retrieve and process data. Please run them in alphabetical order or use the [run_notebooks.ipynb](notebooks/run_notebooks.ipynb) that will run all the notebooks for you and imprint the results. To download the data, there is a dependency on the [DataSharing](https://github.com/ChristianCasazza/datasharing) client.


