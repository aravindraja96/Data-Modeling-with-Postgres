import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
    Load Song Json file as Dataframe and Inserts data into Tables Songs and Artist.

            Parameters:
                    cur : Cursor for Database
                    filepath: Path of the Source file

            Returns:
                    None
    '''
    # open song file
    df = pd.read_json(filepath, lines=True) 

    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']].values.tolist()
    song_data=  song_data[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']].values.tolist()
    artist_data=artist_data[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
        '''
    Load Log Json file as Dataframe and Inserts data into Tables Time , Users and Songplays.

            Parameters:
                    cur : Cursor for Database
                    filepath: Path of the Source file

            Returns:
                    None
    '''
    # open log file
    df = pd.read_json(filepath, lines=True) 

    # filter by NextSong action
    time_data = df.loc[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t =pd.to_datetime(df.ts, unit='ms') 
    
    # insert time data records
    time_data =  [t.tolist(),t.dt.hour.tolist(),t.dt.day.tolist(),t.dt.week.tolist(),t.dt.month.tolist(),t.dt.year.tolist(),t.dt.weekday.tolist()]
    column_labels = ['start_time' ,'hour' ,'day' ,'week' ,'month' ,'year' ,'weekday']
    time_df = pd.DataFrame(time_data).transpose()
    time_df.columns = column_labels

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        if row.userId == ''  or not row.userId:
            continue
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index,row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        
        start_time = pd.to_datetime(row.ts)
        
        # insert songplay record
        songplay_data = (start_time,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
        '''
   It retrives all the json files and Inserts all data using Function Call.

            Parameters:
                    cur     : Cursor for Database
                    conn    : Connection to the Database
                    filepath: Path of the Source file
                    func    : Function to be invoked

            Returns:
                    None
    '''
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    '''
   The Main function etablishes connection to database and invokes other functions in order of execution .

            Parameters:
                    None
            Returns:
                    None
    '''
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()