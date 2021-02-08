from pytube import YouTube
import sqlite3

conn = sqlite3.connect('bazasearch.db')
cur = conn.cursor()
cur.execute("""SELECT link FROM vidos""")
vid_links = cur.fetchall()
for i in vid_links:
    yt = YouTube(i[0])
    yt.streams.get_by_itag(18).download()
    print(i[0])

# link = 'https://www.youtube.com/watch?v=Ydsmv5OjMRU'
#
# yt = YouTube('https://www.youtube.com/watch?v=oIh7YLqm_KQ')
# print(yt.streams.get_by_itag(18))
# yt.streams.get_by_itag(18).download()
