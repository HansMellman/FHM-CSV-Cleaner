import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Team Records Cleaner',
    page_icon="📃"
)

st.title('FHM CSV Cleaner')

st.subheader('Team Records')

# Load in specific CSV and read them in.
team_records = st.file_uploader("Please select the 'Team Records' CSV")
if team_records is not None:
    team_records = pd.read_csv(team_records, sep=';')

    # Title original CSV and display in app.
    st.header("team_records.csv")
    st.write(team_records)


    # Isolate NHL teams ONLY, by their leagueid.
    nhl = team_records[team_records["League Id"] == 0]

    # title this cleaned up CSV
    st.header("team_records_CONVERTED.csv")
    st.write(nhl)

    st.download_button(
        label='Download cleaned CSV',
        data=nhl.to_csv(index=False),
        file_name='team_records_CONVERTED.csv',
        mime='text/csv',
        key='download-csv',
        help='Click to download the cleaned "team_records" CSV'
    )



