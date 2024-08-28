import streamlit as st
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cricket Match TRP Prioritization", layout="wide")
st.title("Cricket Match TRP Prioritization")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df['Time (IST)'] = pd.to_datetime(df['Time (IST)'], format='%H:%M:%S').dt.time
    df['Finish Time (IST)'] = pd.to_datetime(df['Finish Time (IST)'], format='%H:%M:%S').dt.time
    df['Match Start'] = df.apply(lambda row: datetime.combine(row['Date'], row['Time (IST)']), axis=1)
    df['Match End'] = df.apply(lambda row: datetime.combine(row['Date'], row['Finish Time (IST)']) 
                            if pd.notna(row['Finish Time (IST)']) else pd.NaT, axis=1)

    current_time = datetime.now()

    def determine_status(row):
        if pd.isna(row['Match End']):
            if current_time < row['Match Start']:
                return 'Upcoming'
            else:
                return 'Completed'
        if current_time < row['Match Start']:
            return 'Upcoming'
        elif row['Match Start'] <= current_time <= row['Match End']:
            return 'Live'
        else:
            return 'Completed'

    df['Status'] = df.apply(determine_status, axis=1)
    df = df.drop(columns=['Match Start', 'Match End'])
    df = df.drop_duplicates(subset=['Date', 'Time (IST)', 'Team A', 'Team B', 'Gender', 'Match Type'], keep='first')

    priority = {
        'Series Type': {'World Cup': 1, 'Other': 2},
        'Rivalry': {'Ind vs Pak': 1, 'Ashes': 2, 'Other': 3},
        'Status': {'Live': 1, 'Upcoming': 2, 'Completed': 3, 'Special Match': 4, 'Final': 5, 'Semi-final': 6, 'Quarter-final': 7},
        'Teams': {'India': 1, 'England': 2, 'Australia': 3, 'South Africa': 4, 'Pakistan': 5, 'New Zealand': 6, 'Sri Lanka': 7, 'West Indies': 8, 'Afghanistan': 9, 'Others': 10},
        'Time (IST)': {('17:00', '20:30'): 1, ('12:00', '17:00'): 2, ('20:30', '23:00'): 3, ('09:00', '12:00'): 4, ('23:00', '01:00'): 5, ('01:00', '06:00'): 6, ('06:00', '09:00'): 7},
        'Match Category': {'International': 1, 'Domestic': 2},
        'Format': {'T20': 1, 'One Day': 2, 'Test': 3},
        'Is League': {'Yes': 1, 'No': 2},
        'Gender': {'Male': 1, 'Female': 2}
    }

    def calculate_trp(row):
        trp = 0
        trp += priority['Series Type'].get(row['Series Type'], 2)
        trp += priority['Rivalry'].get(row['Rivalry'], 3)
        trp += priority['Status'].get(row['Status'], 7)
        trp += min(priority['Teams'].get(row['Team A'], 10), priority['Teams'].get(row['Team B'], 10))

        match_time = row['Time (IST)']
        for time_range, score in priority['Time (IST)'].items():
            start_time = datetime.strptime(time_range[0], '%H:%M').time()
            end_time = datetime.strptime(time_range[1], '%H:%M').time()
            if start_time <= match_time <= end_time:
                trp += score
                break

        trp += priority['Match Category'].get(row['Match Category'], 2)
        trp += priority['Format'].get(row['Match Type'], 3)
        trp += priority['Is League'].get(row['League/Event'], 2)
        trp += priority['Gender'].get(row['Gender'], 2)
        trp += row['No. of Teams']

        return trp

    df['TRP Priority'] = df.apply(calculate_trp, axis=1)
    df = df.sort_values(by='TRP Priority')

    st.subheader("Top 10 Matches by TRP Priority")
    st.write(df.head(10)[['Date', 'Team A', 'Team B', 'Status', 'Series Type', 'TRP Priority']])

    df['High Priority'] = df['TRP Priority'] <= df['TRP Priority'].quantile(0.25)
    date_priority = df[df['High Priority']].groupby('Date').size().reset_index(name='High Priority Matches')

    date_priority = date_priority.sort_values(by='High Priority Matches', ascending=False)

    st.markdown("---")

    st.subheader("Dates with Most High-Priority Matches")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Date', y='High Priority Matches', data=date_priority, palette='viridis')
    plt.title('Dates with Most High-Priority Matches')
    plt.xlabel('Date')
    plt.ylabel('Number of High-Priority Matches')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.subheader("Distribution of TRP Priority Scores")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['TRP Priority'], bins=20, kde=True, color='blue')
    plt.title('Distribution of TRP Priority Scores')
    plt.xlabel('TRP Priority')
    plt.ylabel('Frequency')
    st.pyplot(plt)

