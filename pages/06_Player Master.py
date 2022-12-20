import streamlit as st
import pandas as pd

st.title('FHM CSV Cleaner')

st.subheader('Player Master')

player_master = st.file_uploader("Please select the 'Player Master' CSV")

if player_master is not None:
    if player_master.name != 'player_master.csv':
        st.write("Please upload the correct player_master.csv")
    elif player_master.name == 'player_master.csv':
        # player_master = pd.read_csv(player_master) # I'm using Pandas for the other CSV's on this web app but I know
        # pd cannot handle the non utf 8.


        def get_players(id, matching_col, filename):
            """

            :param id: The id or list of ids you wish to match against
            :param matching_col: The column you wish to check id against
            :param filename: filepath and name of file to open
            :return: csv of requested id to matching column
            """
            # Checks if id is a list or a single element, if its not a list it makes it one
            # This also makes sure to convert the id to a str as when reading the file in later it reads everything as a string
            if type(id) == list:
                id = [
                    str(x) for x in id
                ]  # This is called list comprehension, it turns a for loop into a single line
            else:
                id = [str(id)]

            players = ""  # This will end up being the new file to be written
            row_num = 0  # Just to keep track of row numbers
            match_col_index = (
                -1
            )  # This will hold the index of the column you want to check if id is in
            with open(
                    filename, "r", encoding="latin-1"
            ) as file:  # Opens the file in whats called a context manager

                for row in file:  # Loops through every row in the file
                    row = row.replace(";", ",")  # Replaces the ";" with a ","
                    if row_num == 0:  # Checks if the row is the header row
                        num_col = len(row.split(","))  # this gives you the number of columns
                        players += row  # Adds the row to the file to be written
                        # Column headers
                        match_col_index = row.split(",").index(
                            matching_col
                        )  # Gets the index of the column you wish to check id against

                    if len(row.split(",")) == num_col:  # check if row has enough elements
                        split_row = row.split(
                            ","
                        )  # This creates a list of elements that are split on ","
                        if (
                                split_row[match_col_index] in id
                        ):  # Checks if the id is in the current row, col pair
                            players += (
                                row  # if it is then it adds it to the file to be written.
                            )

                    row_num += 1  # once we are done with a row increment this to keep track
            file_name = filename.replace(
                ".csv", "_CONVERTED.csv"
            )  # This just adds the _fix to the filename
            with open(file_name, "w", encoding="latin-1") as file:  # writes file to memory
                file.write(players)

            return (
                players  # if you want to print the players this will return the string of players
            )


        if __name__ == "__main__":
            nhl_players = [
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
            p = get_players(nhl_players, "TeamId", player_master)



