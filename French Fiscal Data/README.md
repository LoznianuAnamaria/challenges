# French Fiscal AI Innovation and Prediction Challenge


This challenge is posted by Ocean Protocol and hosted on Desights. For more information, visit the [Desights Challenge Page](https://competitions.desights.ai/challenge/26).

This repository contains all the data and analysis for the French Fiscal AI Innovation and Prediction Challenge, held in collaboration with the Joint Research Centre (JRC), the Science Hub of the European Union Commission.

## Overview

The challenge presents a unique opportunity to examine 40 years of French tax data, aiming to enhance data-driven decision-making for EU policymakers. Participants will employ their analytical and predictive modeling skills to reveal significant insights into the fiscal behaviors of French municipalities.

## Challenge Objectives

- Rank municipalities by their tax revenue to identify those with the highest income from direct local taxes.
- Create graphical representations to illustrate revenue trends in selected towns.
- Classify municipalities based on their growth in tax revenues over various periods.
- Investigate the relationship between population size and tax revenue.
- Assess the impact of eliminating the professional tax collected before 2010.

## Dataset

The dataset is an aggregation of French REI (Répertoire des Élus et des Institutions) data files, providing detailed financial and administrative information on French municipalities. Originally a 3.6GB CSV file, it has been converted into a 0.6GB Parquet file for efficient analysis.

## Tools and Recommendations

- **Parquet**: The columnar storage format allows faster data access, reduced file size, and improved query performance.
- **DuckDB**: A high-performance, in-memory database engine optimized for SQL querying on local machines. DuckDB is recommended for interacting with the dataset, ensuring quick and effective analysis.

## Files Included

