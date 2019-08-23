import os
import re
from episodeClass import EpisodeFormatter

class SeasonFormatter:
    def __init__(self, path, showName):
        self.path = path
        self.showName = showName
        os.chdir(path)
    
    def getSeason(self, filename):
        match = re.search("(?ix)(?:s|x|\-|season|^)\s*(\d+)", filename)
        if match:
            return int(match.group(1))
    def renameSeasons(self):
        #Rename with standard name
        trackerFound = False
        for f in os.listdir(self.path):
            if not os.path.isdir(f) or not self.getSeason(f):
                continue
            newName = self.showName + " - " + "S" + str(self.getSeason(f))
            os.rename(f, newName)
            episodeFormatter = EpisodeFormatter(self.path+"\\"+newName, self.showName)
            episodeFormatter.renameEpisodes()
            os.chdir(self.path)
