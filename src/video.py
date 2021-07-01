"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._paused = False
        self._resumed = False

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    def setPaused(self, paused_val) -> bool:
        """Returns if video is paused."""
        self._paused = paused_val
    def setResumed(self, resumed_val) -> bool:
        """Returns if video is resumed."""
        self._resumed = resumed_val

    @property
    def isPaused(self) -> bool:
        """Returns if video is paused."""
        return self._paused
    @property
    def isResumed(self) -> bool:
        """Returns if video is resumed."""
        return self._resumed