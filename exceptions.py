class SubtitleSyncError(Exception):
    """Base exception class for SubtitleSync-CLI."""
    pass

class FileAccessError(SubtitleSyncError):
    """Raised when the input file cannot be read or output cannot be written."""
    pass

class ParsingError(SubtitleSyncError):
    """Raised when the .srt file format is invalid or cannot be parsed."""
    pass

class InvalidOffsetError(SubtitleSyncError):
    """Raised when the provided offset value is invalid."""
    pass

class TimestampError(SubtitleSyncError):
    """Raised when a calculated timestamp results in an invalid time (e.g., negative)."""
    pass