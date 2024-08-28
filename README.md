Sure! Here's the complete `README.md` file content, including the "Usage" section, formatted for you to copy and paste directly:

```markdown
# Cricket Match TRP Prioritization

This repository contains a Python-based project for prioritizing cricket matches using a TRP (Television Rating Points) scoring system. The project includes data processing, visualization, and a Streamlit web application for user interaction.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Running the Streamlit App](#running-the-streamlit-app)
   - [Using the Application](#using-the-application)
5. [Data Processing and Analysis](#data-processing-and-analysis)
   - [Handling Duplicates](#handling-duplicates)
   - [TRP Priority Calculation](#trp-priority-calculation)
   - [Key Visualizations](#key-visualizations)
6. [Streamlit Application](#streamlit-application)
   - [Uploading the Data](#uploading-the-data)
   - [Top 10 Matches](#top-10-matches)
   - [Visualizations](#visualizations)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

The project focuses on prioritizing cricket matches based on several factors to determine their potential for high television ratings (TRP). This is useful for broadcasters, analysts, and marketers to understand which matches are likely to draw the most viewers.

## Features

- **Data Processing**: Cleans and processes cricket match data from an Excel file.
- **TRP Calculation**: Assigns a TRP priority score to each match based on factors like series type, rivalry, status, teams, and match format.
- **Duplicate Handling**: Removes redundant matches to ensure accurate analysis.
- **Visualization**: Generates insightful visualizations to highlight key trends and insights.
- **Streamlit Application**: A user-friendly web interface for uploading data, viewing prioritized matches, and visualizing trends.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/devkartikrathi/CricRadio.git
   cd cricket-trp-prioritization
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the necessary packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Streamlit App

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Open the App**:
   The app will open in your default web browser. You can also access it via the link provided in the terminal.

### Using the Application

- **Upload Data**: Use the file uploader to upload your Excel file containing cricket match data.
- **View Top Matches**: The app calculates the TRP priority and displays the top 10 matches based on their scores.
- **Visualize Trends**: Explore various charts that provide insights into the data.

## Data Processing and Analysis

### Handling Duplicates

Before processing, the data is cleaned by removing duplicate rows based on key criteria such as date, time, teams, gender, and match type.

```python
df = df.drop_duplicates(subset=['Date', 'Time (IST)', 'Team A', 'Team B', 'Gender', 'Match Type'], keep='first')
```

### TRP Priority Calculation

TRP priority is calculated based on the following factors:

- **Series Type**: Higher priority for major series like the World Cup.
- **Rivalry**: Iconic rivalries like Ind vs Pak receive higher priority.
- **Status**: Live matches are prioritized over upcoming or completed matches.
- **Teams**: Matches involving top teams are prioritized.
- **Match Category**: International matches are prioritized over domestic ones.
- **Format**: Different formats (T20, ODI, Test) have varying priorities.
- **Is League**: Matches within a league or major event get higher priority.
- **Gender**: Male matches typically have different priorities compared to female matches.

### Key Visualizations

1. **Dates with Most High-Priority Matches**:
   - A bar plot that shows which dates have the highest concentration of high-priority matches.

   ```python
   date_priority = df.groupby('Date')['TRP Priority'].sum().reset_index()
   date_priority = date_priority.sort_values(by='TRP Priority', ascending=True)
   sns.barplot(x='Date', y='TRP Priority', data=date_priority)
   ```

2. **TRP Priority Distribution**:
   - A histogram showing how TRP scores are distributed across all matches.

   ```python
   sns.histplot(df['TRP Priority'], bins=20, kde=True)
   ```

3. **Average TRP by Team**:
   - A bar plot showing the average TRP scores for different teams.

   ```python
   df['Team'] = df[['Team A', 'Team B']].apply(lambda x: ' vs '.join(x), axis=1)
   team_trp = df.head(20).groupby('Team')['TRP Priority'].mean().sort_values()
   sns.barplot(x=team_trp, y=team_trp.index)
   ```

## Streamlit Application

### Uploading the Data

Users can upload an `.xlsx` file containing cricket match data. The app processes this file and displays the top 10 matches based on the calculated TRP priority.

### Top 10 Matches

The app lists the top 10 matches by TRP priority, allowing users to quickly identify the most important matches.

### Visualizations

The app includes several visualizations to help users explore the data, including:

- **Distribution of TRP Scores**
- **TRP Priority by Match Status**
- **Average TRP by Team**
- **Dates with Most High-Priority Matches**

These visualizations provide insights into which matches and factors are driving viewership.