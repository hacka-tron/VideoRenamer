# SeasonEpisodeRenamer

SeasonEpisodeRenamer is a tool to help rename show series with just 1 click.

## Installation

Just download the file and make sure you have python installed

## Usage

This tool has two major usages: 

1. Rename Entire Season

2. Rename individual season

Entire Season
---
To do this, insert the folder in the file directory which contains directories of every season, like so:

```
SHOW NAME\
└───Season 1\
│   │   Episode 1
│   │   Episode 2
│   
└───Season 2\
│   │   Episode 1
│   │   Episode 2
│   
└───SeasonEpisodeRenamer\  <--the folder goes right here 
    │   episodeClass.py
    │   episodeFormatter.py
    │   seasonFormatter.py
```

At this point, open the seasonFormatter.py file and make sure to change the name of the show. Click on seasonFormatter.py and your show should now be nicely named

Individual Season
---
To do this, insert the folder in the folder which contains the episodes of a certain season, like so:

```
SHOW NAME\
└───Season 1\
│   │   Episode 1
│   │   Episode 2
│   
└───Season 2\
    │   Episode 1
    │   Episode 2
    └───SeasonEpisodeRenamer\  <--the folder goes right here 
            |episodeClass.py
            |episodeFormatter.py
            |seasonFormatter.py
```

At this point, open the episodeFormatter.py file and make sure to change the name of the show . Click on episodeFormatter.py and your season should now be nicely named