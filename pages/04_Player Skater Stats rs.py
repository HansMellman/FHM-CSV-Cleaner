import streamlit as st
import pandas as pd

st.set_page_config(page_title="Player Skater Stats rs Cleaner", page_icon="📄")

st.title("FHM CSV Cleaner")

st.subheader("Player Skater Stats rs")

# Load in specific CSV and read them in.
rs_player_stats = st.file_uploader("Please select the 'Player Skater Stats rs' CSV")
if rs_player_stats is not None:
    if rs_player_stats.name != "player_skater_stats_rs.csv":
        st.write("Please upload the correct player_skater_stats_rs.csv")
    elif rs_player_stats.name == "player_skater_stats_rs.csv":
        rs_player_stats = pd.read_csv(rs_player_stats, sep=";")

        # Title original CSV and display in app.
        st.header("player_skater_stats_rs.csv")
        st.write(rs_player_stats)

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

        nhl_player_stats = rs_player_stats[rs_player_stats["TeamId"].isin(teamid)]

        # title this cleaned up CSV
        st.header("player_skater_stats_rs_CONVERTED.csv")
        st.write(nhl_player_stats)

        st.download_button(
            label="Download cleaned CSV",
            data=rs_player_stats.to_csv(index=False),
            file_name="player_skater_stats_rs_CONVERTED.csv",
            mime="text/csv",
            key="download-csv",
            help='Click to download the cleaned "player_skater_stats_rs" CSV',
        )
