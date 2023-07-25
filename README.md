# calendar-icon
A simple python project to create a calendar icon for the current date.

Dependencies are: 
- datetime
- os
- subprocess
  - used to run imagemagick installed in the local environment to convert the pngs
 
So far, this has only been tested and confirmed to work on Linux (debian). 

TODO  
[ ] Test on macOS
[ ] Add directions for setting the image file as the calendar app icon
[ ] Create shell script to install the file, and ensure the file is store in $PATH
[ ] Add instructions or shell script for adding script to cron to run at set interval of choice

Running the file creates an svg file with the current day name at the top of the image and the current date number on the bottome.
The app then converts the svg to a png in several different sizes.

Example svg: 

![calendar](https://github.com/jamie-c/calendar-icon/assets/5421944/e4bd863b-d854-4799-bb1b-db24dc2ecee6)

Example png: 

![calendar-128x128](https://github.com/jamie-c/calendar-icon/assets/5421944/e7a1578d-ed94-42db-a45d-e995cf040d10)
