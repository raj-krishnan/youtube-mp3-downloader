# Youtube Audio Download
This is a small script to download mp3 audio files from Youtube

### Requirements

* Python
* Firefox
* Selenium for Python

### Installation

1. Download and install [Python 2.7](https://www.python.org/downloads/) and [Firefox](https://www.mozilla.org/en-US/firefox/new/) for your OS
2. Install [pip](https://pip.pypa.io/en/stable/installing/) for your OS (Included in windows installation of python so windows users can skip this step)
3. Run the following command in terminal or command prompt:

        pip install selenium

4. Open Download_MP3.py and edit the download path on line 7

        download_path = 'Path_to_downloads_folder/'

5. Also, change the Firefox profile path on line 9

        firefox_profile = 'Path_to_youtube_mp3_downloader/firefox_profile.default'

**Note to windows users:**

- In case you encounter formatting errors while editing the file, use [Notepad++](https://notepad-plus-plus.org/download/) instead
- Use \\\\ instead of / in your path

### Usage

1. Delete all contents of Youtube_Links.txt
2. Paste the links of the required Youtube videos in Youtube_Links.txt
3. Run Download_Songs.bat or Download_Songs.sh based on your operating system
4. *Optional* You can also create a shortcut to these files for easy access

### To Do

- Add support for playlists

