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
        found_video = False
        for vid in self._video_library.get_all_videos():
            if(vid.video_id)==video_id:
               self._videos.append(vid)
               found_video = True
        if found_video == False:
            raise ValueError("Video is not in library")

    def delete_video_from_playlist(self, video_id):
        found_video = False
        video_found = []
        for vid in self._video_library.get_all_videos():
            if(vid.video_id)==video_id:
               video_found = vid
               found_video = True
        if found_video == False:
            raise ValueError("Video is not in playlist")
        else:
            self._videos.remove(video_found)

    def clear_videos_from_playlist(self):
        self._videos = []