import os
import shutil
# import re
from pytube import Playlist, YouTube
import threading
import time

class VideoDownloader:
	def __init__(self,url, download_dir) -> None:
		self.url = url
		self.video = YouTube(self.url)

		# if download_dir is None = > use CWD
		if download_dir==None:
			self.download_dir = os.getcwd()
		elif os.path.isdir(download_dir):
			self.download_dir = download_dir
		else:
			raise Exception(f'Error: {download_dir} does not exists!')



	def get_meta_data(self) -> dict():
		return {
			"author": self.video.author,
			"description":self.video.description,
			"keywords": self.video.keywords,
			"length": self.video.length,
			"publish_date":self.video.publish_date,
			"rating":self.video.rating,
			"title":self.video.title,
			"vid_info":self.video.vid_info,
			"views":self.video.views,
			"meta": self.video.metadata
		}

	def download(self, highest_res=False):
		print(f"Downloading: {self.video.title}...")

		if highest_res:
			stream = self.video.streams.get_highest_resolution()
		else:
			stream = self.video.streams.get_lowest_resolution()


		stream.download(self.download_dir)

		# print("Video Download complete!")


	def list_metadata(self):
		print(self.video.metadata.raw_metadata)
		print(self.video.metadata._metadata)


class PlaylistDownloader:
	def __init__(self, url, base_download_dir=None, n=None) -> None:
		self.url = url
		self.playlist = Playlist(self.url)

		# get all video URLs in the playlist
		self.video_urls = self.playlist.video_urls
		# get first n video URLs in the playlist

		if n:
			self.video_urls = self.video_urls[:n]


		# if base_download_dir is None = > use CWD
		if base_download_dir==None:
			self.base_download_dir = os.getcwd()
		elif os.path.isdir(base_download_dir):
			self.base_download_dir = base_download_dir
		else:
			print(f'{base_download_dir} will be created!')
			# create a directory to store the playlist videos
			self.base_download_dir = os.path.join(
				self.base_download_dir, self.playlist.title)

			try:
				os.mkdir(self.base_download_dir)
			except FileExistsError as fe:
				# empty base_download_dir
				shutil.rmtree(self.base_download_dir)
				os.mkdir(self.base_download_dir)


	def list_videos(self):
		for video in self.playlist.videos:
			print(video.title)

	def _download_video(self,video_url,highest_res):
		video = VideoDownloader(
			url=video_url,
			download_dir=self.base_download_dir)

		video.download(highest_res=highest_res)

	def sequential_download(self, highest_res=False):
		# Download each video in the playlist
		for video_url in self.video_urls:
			self._download_video(video_url, highest_res)

	def threaded_download(self, highest_res=False):
		# Download each video in the playlist in a thread
		threads = []
		for video_url in self.video_urls:
			tr = threading.Thread(target=self._download_video, args=(video_url, highest_res))
			tr.start()
			threads.append(tr)

		# make sure that all threads are finish their job
		for tr in threads:
			tr.join()

		print("Playlist download complete!")



PLAYLIST_URL = 'https://www.youtube.com/watch?v=M04E_Wr6dG4&list=PLS1QulWo1RIb5zGRu6GEej9odbh90hfM6&ab_channel=ProgrammingKnowledge'

pl1 = PlaylistDownloader(
	url=PLAYLIST_URL,
	base_download_dir='./downloads/',
	n=3
)

# pl1.list_videos()
start_time = time.time()
pl1.sequential_download()
sequential_time = time.time() - start_time

start_time = time.time()
pl1.threaded_download()
threaded_time = time.time() - start_time


# Display results
print(f'\nSequential download {sequential_time:.2f} seconds')
print(f'\nThreaded download {threaded_time:.2f} seconds')

