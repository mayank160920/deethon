"""This module contains tests for the [session][deethon.session] module."""
from pathlib import Path

import pytest

import deethon


def test_session():
    """
    Test if the [Session][deethon.session.Session] class raises a
    [DeezerLoginError][deethon.types.DeezerLoginError] when an invalid
    arl token is passed.
    """
    with pytest.raises(deethon.errors.DeezerLoginError):
        session = deethon.Session('wrongarltoken')
        session._refresh_session()


def test_download():
    """Test if the download method returns a Path object."""
    deezer = deethon.Session(
        'a77016e49be3ec2a03200a73d773a62dcd0eb5605c037b8194965aafe2c41d2276204368aa266407ba774dc54bde701ed4f8248eeac235fde26edea1af77dfaa0caac259b8e16ad01bee9514d79e234966714177f490b3d6e848686feea8840e')
    assert isinstance(
        deezer.download('https://www.deezer.com/track/2104162', 'MP3_320'), Path)
    assert isinstance(
        deezer.download('https://www.deezer.com/track/2104162'), Path)

    with pytest.raises(deethon.errors.InvalidUrlError):
        deezer.download('https://www.google.com')

    with pytest.raises(deethon.errors.ActionNotSupported):
        deezer.download('https://www.deezer.com/unsuppoted/123456')

    with pytest.raises(deethon.errors.DownloadError):
        deezer.download('https://www.deezer.com/track/101399924')
