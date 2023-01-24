import streamlit as st
import pandas as pd
import html

st.set_page_config(page_title="Player Master Cleaner", page_icon="📄")

st.title("FHM CSV Cleaner")

st.subheader("Player Master")

player_master = st.file_uploader("Please select the 'Player Master' CSV")
if player_master is not None:
    if player_master.name != "player_master.csv":
        st.write("Please upload the correct player_master.csv")
    elif player_master.name == "player_master.csv":
        player_master = pd.read_csv(
            player_master,
            sep=";",
            encoding="cp437",
            on_bad_lines="skip",
            low_memory=False,
        )

        # Title original CSV and display in app.
        st.header("player_master.csv")
        st.write(player_master)

        # Isolate the NHL players using the team ID's.
        nhl_players = player_master[
            player_master["TeamId"].isin(
                [
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
            )
        ]

        # title this cleaned up CSV
        st.header("player_master_CONVERTED.csv")
        st.write(nhl_players)

        # Download button for user to download the amended CSV.
        st.download_button(
            label="Download cleaned CSV",
            data=nhl_players.to_csv(index=False),
            file_name="player_master_CONVERTED.csv",
            mime="text/csv",
            key="download-csv",
            help='Click to download the cleaned "player_master" CSV',
        )
