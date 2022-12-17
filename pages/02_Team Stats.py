import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Team Stats Cleaner',
    page_icon="📄"
)

st.title('FHM CSV Cleaner')

st.subheader('Team Stats')

# Load in specific CSV and read them in.
team_stats = st.file_uploader("Please select the 'Team Stats' CSV")
if team_stats is not None:
    team_stats = pd.read_csv(team_stats, sep=';')

    # Title original CSV and display in app.
    st.header("team_stats.csv")
    st.write(team_stats)

    # NHL teamids
    teamid = [
        0,
        3,
        5,
        8,
        9,
        10,
        11,
        12,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        4182,
        4838,
    ]

    # select only the NHL teams from the CSV
    nhl_team_stats = team_stats[team_stats["TeamId"].isin(teamid)]

    # title this cleaned up CSV
    st.header("team_stats_CONVERTED.csv")
    st.write(nhl_team_stats)

    st.download_button(
        label='Download cleaned CSV',
        data=nhl_team_stats.to_csv(index=False),
        file_name='team_stats_CONVERTED.csv',
        mime='text/csv',
        key='download-csv',
        help='Click to download the cleaned "team_stats" CSV'
    )