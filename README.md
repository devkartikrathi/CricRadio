This repository contains the code and documentation for prioritizing cricket matches based on TRP (Television Rating Points) using data analysis and visualization. It includes both a Jupyter Notebook for in-depth analysis and a Streamlit application for a user-friendly interface.

## Table of Contents

1. [Introduction](#introduction)
2. [Data Analysis and Approach](#data-analysis-and-approach)
   - [Data Understanding](#data-understanding)
   - [Data Preprocessing](#data-preprocessing)
   - [TRP Priority Calculation](#trp-priority-calculation)
   - [Edge Cases and Priority Collision Handling](#edge-cases-and-priority-collision-handling)
   - [Data Visualization](#data-visualization)
3. [Streamlit Application](#streamlit-application)
   - [Features](#features)
   - [Setup and Usage](#setup-and-usage)
4. [Jupyter Notebook](#jupyter-notebook)
5. [How to Use This Repository](#how-to-use-this-repository)
   - [Requirements](#requirements)
   - [Installation](#installation)
   - [Running the Streamlit App](#running-the-streamlit-app)
   - [Running the Jupyter Notebook](#running-the-jupyter-notebook)

## Introduction

The objective of this project is to develop a system that prioritizes cricket matches based on various factors, such as rivalry, match status, time of the match, and others, to maximize user engagement. The project consists of a detailed analysis and a web application where users can upload their data and receive prioritized matches along with visualizations.

## Data Analysis and Approach

### Data Understanding

The dataset provided contains information about cricket matches, including details like series type, rivalry status, match status, teams involved, match time, match category, format, and more. The goal is to calculate a TRP priority score for each match based on these attributes.

### Data Preprocessing

- **Handling Missing Data**: Imputation and exclusion techniques are used to handle missing values.
- **Normalization and Capping**: To prevent any single factor from disproportionately affecting the TRP score, normalization and capping strategies are applied where necessary.

### TRP Priority Calculation

The TRP priority score is calculated using a weighted sum of various factors:

- **Series Type**: Higher priority for major series like the World Cup.
- **Rivalry**: Iconic rivalries like Ind vs Pak receive higher priority.
- **Status**: Live matches are prioritized over upcoming or completed matches.
- **Teams**: Matches involving top teams are prioritized.
- **Time**: Matches played during peak viewing times are given higher priority.
- **Other Factors**: Match category, format, league status, and gender also influence the TRP priority.

### Edge Cases and Priority Collision Handling

- **Edge Cases**: Scenarios such as missing data, ties in TRP scores, and outliers are handled through imputation, secondary sorting, or randomization.
- **Priority Collision**: Conflicts between different factors are resolved using a weighted scoring system and custom rules for special cases like finals.

### Data Visualization

Visualizations are included to provide insights into the distribution of TRP priority scores, top matches, and TRP priority by match status or teams.

## Streamlit Application

### Features

- **File Upload**: Users can upload an Excel file containing match data.
- **TRP Calculation**: Automatically calculates the TRP priority for each match.
- **Visualization**: Generates visualizations such as TRP distribution, top matches, and TRP by match status.
- **Filtered Output**: Provides a prioritized list of matches based on the TRP score.
