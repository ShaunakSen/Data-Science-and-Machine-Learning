# Hackerearth ML Project: Pet Adoption

URL: https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-pet-adoption/machine-learning/pet-adoption-9-5838c75b/

## Problem statement

A leading pet adoption agency is planning to create a virtual tour experience for their customers showcasing all animals that are available in their shelter. To enable this tour experience, you are required to build a Machine Learning model that determines type and breed of the animal based on its physical attributes and other factors.

## Data description

![https://i.imgur.com/ddR8vXO.png](https://i.imgur.com/ddR8vXO.png)

## Evaluation metric

![https://i.imgur.com/E9BzzgK.png](https://i.imgur.com/E9BzzgK.png)

## Exploratory Data Analysis

1. Condition has missing values
    1. KNN imputation?
    2. Check if it is related to any cols
2. Since X1 and X2 affect breed v=cat in similar manner is there corr bw them?
3. Condition should ideally be categorical
    1. When condition is NULL it is always breed = 2, so simply replace null with -1 and create feature condition_NULL
4. Date - month, year, weekday, weekend
    1. Listing date has time as well
5. Encode color how?
6. Diff of days bw issue and listing date