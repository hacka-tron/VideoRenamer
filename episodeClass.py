import os
import re
#showPath = os.getcwd()
#showName = 'CHANGE THIS'
ext = ".mp4"
supportedTypes = ['.mkv', '.mp4']


class EpisodeFormatter:
    def __init__(self, path, showName):
        self.path = path
        self.showName = showName
        os.chdir(path)
    
    def getEpisode(self, filename):
        match = re.search("(?ix)(?:e|x|\-|episode|ep|^)\s*(\d+)", filename)
        if match:
            return int(match.group(1))

    def renameEpisodes(self):
        #Rename with standard name
        trackerFound = False
        for f in os.listdir():
            fName, fExt = os.path.splitext(f)
            if fExt == '.txt':
                if (fName == self.showName +" Tracker"): trackerFound =True
                continue
            elif fExt not in supportedTypes:
                continue
            ext = fExt
            newName = self.showName + " - " + str(self.getEpisode(fName)) + fExt
            os.rename(f, newName)
        """
        trackerEp = None
        trackerT = 0
        if not trackerFound:
            tracker = open(self.showName + " Tracker.txt","w+")
            tracker.write('1\n') #Episode Number
            trackerEp = "1"
            tracker.write('00:00\n') #Time
        else:
            tracker = open(self.showName + " Tracker.txt","r+")
            trackerEp = tracker.readline().rstrip('\n')
        os.startfile(self.showName + " - "+ trackerEp+ext)
        if tracker: tracker.close()
        """