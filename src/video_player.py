"""A video player class."""

from os import truncate
import random
from re import S
from .video_library import VideoLibrary
from .video import Video
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""


    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = Video("","","")
        self._video_playlist = {}
        self._flagged_videos = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        for vid in self._video_library.get_all_videos():
            tags = " ".join(vid.tags)
            isFlaggedVid = self._flagged_videos.get(vid.video_id)
            if isFlaggedVid != None:
                print(vid.title +" ("+ vid.video_id +") ["+ tags+"] - FLAGGED (reason:"+isFlaggedVid+")")
            else:
                print(vid.title +" ("+ vid.video_id +") ["+ tags+"]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if self._current_video.title!="":
           print("Stopping video: "+self._current_video.title)
           self._current_video.title=""
        isFound = False
        for vid in self._video_library.get_all_videos():
          if vid.video_id == video_id:
              isFlaggedVid = self._flagged_videos.get(vid.video_id)
              if isFlaggedVid != None:
                print("Cannot play video: Video is currently flagged (reason: "+isFlaggedVid+ ") in 'Playing video: "+vid.title )
              else:
                print("Playing video: "+vid.title)
                self._current_video = vid
              isFound = True
        if isFound == False:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        if self._current_video.title!="":
           print("Stopping video: "+self._current_video.title)
           self._current_video.title=""
        else:
           print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        if self._current_video.title!="":
           print("Stopping video: "+self._current_video.title)
           self._current_video=Video("","","")
        current_video_list = self._video_library.get_all_videos()
        num_videos = len(current_video_list)
        random_number = random.randint(0,num_videos-1)
        video_selected = current_video_list[random_number]
        print("Playing video: "+ video_selected.title)
        self._current_video = video_selected


    def pause_video(self):
        """Pauses the current video."""

        if self._current_video.title!="":
            if self._current_video.isPaused != True:
                print("Pausing video: "+self._current_video.title)
                self._current_video.setPaused(True)
            else:
                print("Video already paused: "+ self._current_video.title)
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video.title!="":
            if self._current_video.isPaused:
                isFlaggedVid = self._flagged_videos.get(self._current_video.video_id)
                if isFlaggedVid != None:
                        print("Cannot continue video: Video is currently flagged "+isFlaggedVid+ "in 'Continuing video: "+self._current_video.title )
                else:
                    print("Continuing video: "+self._current_video.title)
                    self._current_video.setPaused(False)
                    self._current_video.setResumed(True)
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video.title!="" and self._current_video.isPaused==False:
            tags = " ".join(self._current_video.tags)
            print("Currently playing: "+self._current_video.title +" ("+ self._current_video.video_id +") ["+ tags+"]")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playList = self._video_playlist.get(playlist_name)
        if playList == None:
            self._video_playlist.update({playlist_name:Playlist()})
            print("Successfully created new playlist: "+playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        vid_title = ""
        for vid in self._video_library.get_all_videos():
            if vid.video_id == video_id:
                vid_title= vid.title
        if vid_title == "":
            print("Cannot add video to "+playlist_name+": Video does not exist")
        else:
            ret_playlist = self._video_playlist.get(playlist_name)
            if ret_playlist == None:
                print("Cannot add video to "+playlist_name+": Playlist does not exist")
            else:
                  isFlaggedVid = self._flagged_videos.get(vid.video_id)
                  if isFlaggedVid != None:
                        print("Cannot add video to "+playlist_name+": Video is currently flagged "+isFlaggedVid+ "in 'Added video to "+playlist_name+": "+vid.title )
                  else:
                      if vid in ret_playlist._videos:
                          print("Cannot add video to "+playlist_name+": Video already added")
                      else:
                         ret_playlist.add_video_to_playlist(video_id)
                         self._video_playlist.update({playlist_name:ret_playlist})
                         print("Added video to "+playlist_name+": "+vid_title)

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self._video_playlist)==0:
            print("No playlists exist yet")
        else:
            print(self._video_playlist)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        matched_playlist =  []
        matched_playlist = self._video_playlist.get(playlist_name)
        if matched_playlist==None:
            print("Cannot show playlist "+ playlist_name+": Playlist does not exist")
        else:
            print("Showing playlist: "+ str(matched_playlist._videos))

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")
        matched_playlist =  []
        matched_playlist = self._video_playlist.get(playlist_name)
        if matched_playlist==None:
            print("Cannot remove video from  "+ playlist_name+": Playlist does not exist")
        else:
            try:
               matched_playlist.delete_video_from_playlist(video_id)
               print(matched_playlist)
            except:
               print("Video is not in playlist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        matched_playlist = self._video_playlist.get(playlist_name)
        if matched_playlist==None:
            print("Cannot clear playlist "+ playlist_name+": Playlist does not exist")
        else:
            matched_playlist.clear_videos_from_playlist()
            print("Successfully removed all videos from "+playlist_name)


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        matched_playlist = self._video_playlist.get(playlist_name)
        if matched_playlist==None:
            print("Cannot delete playlist "+ playlist_name+": Playlist does not exist")
        else:
            self._video_playlist.pop(playlist_name)
            print("Deleted playlist: "+playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        isFound = False
        videos_that_match = []
        for vid in self._video_library.get_all_videos():
               if search_term.lower() in vid.title.lower():
                   videos_that_match.append(vid)
                   isFound = True
                   break
        if isFound == False:
            print("No search results for "+search_term)
        else:
            print("Here are the results for "+ search_term+":")
            i = 1
            for vid in videos_that_match:
                tags = " ".join(vid.tags)
                print(str(i)+") "+vid.title +"("+vid.video_id+") ["+ tags+"]")
                i = i + 1

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        isFound = False
        videos_that_match = []
        for vid in self._video_library.get_all_videos():
               if video_tag in vid.tags:
                   videos_that_match.append(vid)
                   isFound = True
                   break
        if isFound == False:
            print("No search results for "+ video_tag)
        else:
            print("Here are the results for "+ video_tag+":")
            i = 1
            for vid in videos_that_match:
                tags = " ".join(vid.tags)
                print(str(i)+") "+vid.title +"("+vid.video_id+") ["+ tags+"]")
                i = i + 1

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        isFound = False
        for vid in self._video_library.get_all_videos():
             if vid.video_id == video_id:
                if video_id in self._flagged_videos:
                    print("Cannot flag video: Video is already flagged")
                else:
                    self._flagged_videos.update({video_id:flag_reason})
                    print("Successfully flagged video: "+vid.title+" (reason: "+flag_reason+")")
                isFound = True
        if isFound == False :
            print("Cannot flag video: Video does not exist")


    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        isFound = False
        for vid in self._video_library.get_all_videos():
            if vid.video_id == video_id:
                if video_id in self._flagged_videos:
                    self._flagged_videos.pop(video_id)
                    print("Successfully removed flag from video: "+vid.title)
                else:
                    print("Cannot remove flag from video: Video is not flagged")
                isFound = True
        if isFound == False :
           print("Cannot remove flag from video: Video does not exist")
