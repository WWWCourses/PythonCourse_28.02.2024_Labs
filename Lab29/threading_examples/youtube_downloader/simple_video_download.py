from pytube import YouTube,Playlist

# ------------------------ Download Video = Example 1 ------------------------ #
# YouTube('https://youtu.be/M04E_Wr6dG4?list=PLS1QulWo1RIb5zGRu6GEej9odbh90hfM6').streams.first().download()


# ------------------------ Download Video = Example 2 ------------------------ #
# yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
# yt.streams\
# .filter(progressive=True, file_extension='mp4')\
# .order_by('resolution')\
# .desc()\
# .first()\
# .download()


# --------------------------------- Using API -------------------------------- #
# yt = YouTube('https://youtu.be/O3JXHUe5RWI')
# print(f'author: {yt.author}')
# print(f'fmt_streams: {yt.fmt_streams}')


pl = Playlist('https://www.youtube.com/watch?v=M04E_Wr6dG4&list=PLS1QulWo1RIb5zGRu6GEej9odbh90hfM6&ab_channel=ProgrammingKnowledge')
print(f'Videos count: {pl.length}')

for video_url in pl.video_urls:
    print(video_url)