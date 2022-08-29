import os
import re
from episodeClass import EpisodeFormatter

class SeasonFormatter:
    def __init__(self, path):
        self.path = path
        os.chdir(path)
    
    def getSeason(self, filename):
        match = re.search("(?ix)(?:s|x|\-|\_|season|^)\s*(\d+)", filename)
        if match:
            return int(match.group(1))
        
    def renameSeasons(self):
        # Rename with standard name
        for f in os.listdir(self.path):
            if not os.path.isdir(f) or not self.getSeason(f):
                continue
            season = self.getSeason(f)
            newName = "Season " + str(season)
            os.rename(f, newName)
            episodeFormatter = EpisodeFormatter(self.path+"\\"+newName)
            episodeFormatter.renameEpisodes()
            os.chdir(self.path)
