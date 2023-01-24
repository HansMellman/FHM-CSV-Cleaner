import streamlit as st
import pandas as pd

st.set_page_config(page_title="Player Ratings Cleaner", page_icon="📄")

st.title("FHM CSV Cleaner")

st.subheader("Player Ratings")

player_ratings = st.file_uploader("Please select the 'Player Ratings' CSV")
player_ids = st.file_uploader(
    "Please select the 'player_skater_stats_rs_CONVERTED.csv' CSV that you have just processed, this is necessary for the 'Player Ratings' calculations."
)

if player_ratings is not None and player_ids is not None:
    if (
        player_ratings.name != "player_ratings.csv"
        or player_ids.name != "player_skater_stats_rs_CONVERTED.csv"
    ):
        st.write(
            "Please upload the correct player_ratings.csv and player_skater_stats_rs_CONVERTED.csv"
        )
    elif (
        player_ratings.name == "player_ratings.csv"
        and player_ids.name == "player_skater_stats_rs_CONVERTED.csv"
    ):
        player_ratings = pd.read_csv(player_ratings, sep=";")
        player_ids = pd.read_csv(
            player_ids,
            usecols=[0, 1],
        )

        # Title original CSV and display in app.
        st.header("player_ratings.csv")
        st.write(player_ratings)

        # Isolate NHL players from the ratings CSV using the playerids from the CSV that was read in above
        nhl_player_ratings = player_ratings[
            player_ratings["PlayerId"].isin(player_ids["PlayerId"])
        ]

        # title this cleaned up CSV
        st.header("player_ratings_CONVERTED.csv")
        st.write(nhl_player_ratings)

        # Download button for user to download the amended CSV.
        st.download_button(
            label="Download cleaned CSV",
            data=nhl_player_ratings.to_csv(index=False),
            file_name="player_ratings_CONVERTED.csv",
            mime="text/csv",
            key="download-csv",
            help='Click to download the cleaned "player_ratings" CSV',
        )
