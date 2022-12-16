import streamlit as st
import pandas as pd

st.title('FHM CSV Cleaner')

st.subheader('Team Lines')

# Load in specific CSV and read them in.
team_lines = st.file_uploader("Please select the 'Team Lines' CSV")
if team_lines is not None:
    team_lines = pd.read_csv(team_lines, sep=';')

    # Title original CSV and display in app.
    st.header("team_lines.csv")
    st.write(team_lines)

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

    # Isolate just the NHL team lines
    nhl_team_lines = team_lines[team_lines["TeamId"].isin(teamid)]

    # title this cleaned up CSV
    st.header("team_lines_CONVERTED.csv")
    st.write(nhl_team_lines)

    st.download_button(
        label='Download cleaned CSV',
        data=nhl_team_lines.to_csv(index=False),
        file_name='team_lines_CONVERTED.csv',
        mime='text/csv',
        key='download-csv',
        help='Click to download the cleaned "team_lines" CSV'
    )