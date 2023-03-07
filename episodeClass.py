import os
import re
supportedTypes = ['.mkv', '.mp4', '.avi']


class EpisodeFormatter:
    def __init__(self, path):
        self.path = path
        os.chdir(path)
    
    def getEpisode(self, filename):
        match = re.search("(?ix)(?:e|x|\-|\_|episode|ep|session|^)\s*(\d+)", filename)
        if match:
            return int(match.group(1))

    def renameEpisodes(self):
        # Rename with standard name
        for f in os.listdir():
            fName, fExt = os.path.splitext(f)
            if fExt not in supportedTypes:
                print(f'{fName}{fExt} is not a supported video file type!')
                continue
            newName = f'Episode {str(self.getEpisode(fName)) + fExt}'
            os.rename(f, newName)