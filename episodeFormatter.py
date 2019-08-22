from episodeClass import EpisodeFormatter
import os

os.chdir("..\\")
##EDIT THIS LINE##
e = EpisodeFormatter(os.getcwd(), "CHANGE NAME")
e.renameEpisodes()