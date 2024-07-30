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




About a month ago, I took on a big challenge that I couldn't pass up. France publicly sharing 40 years of tax data 😱 It was so surprising that I had to dive in and see what insights I could uncover. I hope other countries follow their example. 🌍

Now, after countless hours of investigation, research, data preprocessing, tax analysis, coding, and data retrieval, my analysis of the French fiscal system is complete. 📊

The results provide a clear picture of how French municipalities are performing, where they are generating revenue, and valuable information about the economic hubs in the country.

You'll find a few insights in the comments, or you can go through the entire report here: https://github.com/LoznianuAnamaria/challenges/blob/main/French%20Fiscal%20Data/French%20Fiscal%20Data%20Analysis.pdf.


1. Comprehensive Dataset: The dataset includes 1,528,922 rows and 1,181 columns, with approximately 1,080 tax-related columns and 100 columns identifying regions, departments, and syndicates. Just imagine filling it up 😲

2. Municipality Tax Revenue Rankings: Paris dominates with a tax revenue of €51.4B, far exceeding other municipalities. Other top municipalities by tax revenue include Marseille (€7.4B), Toulouse (€6.3B), Nice (€5.9B), and Lyon (€5.5B). Fun fact: Paris, as one of the most visited cities in the world, welcomes over 30 million tourists annually, significantly boosting its revenue. 🌟🌍✨

3. Correlation Between Population and Tax Revenue: There is a strong positive correlation (0.87) between population size and total tax revenue, indicating that population growth is a reliable predictor of tax revenue increases. 📈👥

4. Geographic and Sectoral Diversity: Revenue data highlights the economic importance of regional hubs, port cities, and technological and industrial centers like Toulouse and Grenoble. 🧑‍💻 🐠
Rural and less urbanized departments show significantly lower revenues, highlighting regional economic disparities 🤠

3. Impact of Professional Tax Reform: The abolition of the "Taxe Professionnelle" in 2010 led to a significant decline in professional tax revenue. However, municipalities adapted by increasing reliance on other taxes like property taxes. 🏘️📈
