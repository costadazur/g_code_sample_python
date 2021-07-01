"""A video player class."""

from os import truncate
import random
from .video_library import VideoLibrary
from .video import Video
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""


    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = Video("","","")
        self._video_playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for vid in self._video_library.get_all_videos():
            print(vid.title +" "+ vid.video_id +" "+ str(vid.tags))

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if(self._current_video.title!=""):
           print("Stopping video: "+self._current_video.title)
           self._current_video.title=""
        isFound = False
        for vid in self._video_library.get_all_videos():
          if(vid.video_id):
             print("Playing video:"+vid.title)
             self._current_video = vid
             isFound = True
        if(isFound == False):
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if(self._current_video.title!=""):
           print("Stopping video: "+self._current_video.title)
           self._current_video.title=""
        else:
           print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if(self._current_video.title!=""):
           print("Stopping video: "+self._current_video.title)
           self._current_video.title=""
        current_video_list = self._video_library.get_all_videos()
        num_videos = len(current_video_list)
        random_number = random.randint(0,num_videos-1)
        video_selected = current_video_list[random_number]
        print("Playing video: "+ video_selected.title)
        self._current_video = video_selected


    def pause_video(self):
        """Pauses the current video."""

        if(self._current_video.title!=""):
            if self.current_video.paused != True:
                print("Pausing video: "+self._current_video.title)
                self._current_video.paused(True)
            else:
                print("Video already paused: "+ self._current_video.title)
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if(self._current_video.title!=""):
            if self._current_video.paused:
                print("Continuing video: "+self._current_video.title)
                self._current_video.paused(False)
                self._current_video.resumed(True)
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if(self._current_video.title!=""):
            print("Currently playing: "+self._current_video)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._video_playlist.update({playlist_name:Playlist()})
        print("Successfully created new playlist: "+playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        vid_title = ""
        for vid in self._video_library.get_all_videos():
            if(vid.video_id == video_id):
                vid_title= vid.title
        if vid_title == "":
            print("Cannot add video to "+playlist_name+": Video does not exist")
        else:
            ret_playlist = self._video_playlist.get(playlist_name)
            if ret_playlist == None:
                print("Cannot add video to "+playlist_name+": Playlist does not exist")
            else:
                ret_playlist.add_video_to_playlist(video_id)
                self._video_playlist.update({playlist_name:ret_playlist})
                print("Added video to "+playlist_name+": "+vid_title)

    def show_all_playlists(self):
        """Display all playlists."""

        print(self._video_playlist)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
