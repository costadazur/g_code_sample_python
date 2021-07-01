"""A video playlist class."""
from .video_library import VideoLibrary
from .video import Video

class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self):
        self._video_library = VideoLibrary()
        self._videos = []
        self._current_video = Video("","","")

    def add_video_to_playlist(self, video_id):
        for vid in self._video_library.get_all_videos():
            if(vid.video_id):
               self._videos.append(vid)