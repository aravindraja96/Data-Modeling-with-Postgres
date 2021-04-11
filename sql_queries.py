# DROP TABLES

songplay_table_drop = "drop table IF EXISTS songplays;"
user_table_drop = "drop table IF EXISTS users;"
song_table_drop = "drop table IF EXISTS songs;"
artist_table_drop = "drop table IF EXISTS artists;"
time_table_drop = "drop table IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""Create table songplays (songplay_id integer PRIMARY KEY ,start_time timestamp,user_id varchar,level varchar,song_id varchar ,artist_id varchar,session_id int,location varchar,user_agent varchar)  ;
""")

user_table_create = ("""Create table users (user_id integer,first_name varchar,last_name varchar,gender varchar,level varchar);
""")

song_table_create = ("""Create table songs (song_id varchar, title varchar,artist_id varchar, year integer,duration decimal);
""")

artist_table_create = ("""Create table artists (artist_id varchar,name varchar,location varchar,latitude decimal,longitude decimal);
""")

time_table_create = ("""Create table time(start_time timestamp,hour integer,day integer,week integer,month integer,year integer,weekday varchar);
""")

# INSERT RECORDS %s,

songplay_table_insert = ("""Insert into songplays (songplay_id,start_time ,user_id,level,song_id,artist_id ,session_id ,location ,user_agent) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (songplay_id) DO NOTHING;
""")

user_table_insert = ("""Insert into users (user_id ,first_name ,last_name ,gender ,level ) Values (%s,%s,%s,%s,%s);
""")

song_table_insert = ("""Insert into songs (song_id,title,artist_id,year,duration) Values (%s,%s,%s,%s,%s);
""")

artist_table_insert = ("""Insert into artists (artist_id ,name ,location ,latitude ,longitude) Values (%s,%s,%s,%s,%s);
""")


time_table_insert = ("""Insert into time (start_time ,hour ,day ,week ,month ,year ,weekday ) Values (%s,%s,%s,%s,%s,%s,%s);
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id,artists.artist_id FROM  songs INNER JOIN artists ON songs.artist_id = artists.artist_id WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [song_table_create,songplay_table_create, user_table_create,artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]