# Team Bits
---

## Milestones

**September 30, 2018**: Added deliverable 1 in the [teamOverview](./teamOverview) directory. Its subdirectories may later include the team's product backlog, user stories, scrum meetings, sprint backlog, kanban, and any high-level administrative items.

**October 14, 2018**: Added deliverable 2 files in the [deliverable_2](./teamOverview/deliverable_2) directory. It includes personas_v0.pdf and user_stories_v0.pdf.

**October 17, 2018**: Sprints begin! All scripts should be going into the [src](./src) directory

**October 29, 2018**: As we are preparing for the end of deliverable 3, there are two different ways to run our program (this is tentative and will change in the future). The setup (for now) is presented below.
  1. GUI version: Within the [src/main](./src/main) folder, run `python3 main.py` in your terminal and a GUI should be popping up; no active features are been embedded into it other than account creation and login.

  2. Terminal version: Within the [src/console](./src/console) folder, run `python3 MainConsole.py` in your terminal. This sequentially runs an agency console, and then a TEQ console. The only available feature in this terminal version is for an agency to have their selected excel file on our application (data handling will come later).

Within the next few sprints, it will be expected of us to be tying the GUI with more features.

## Setup

**Python 3** is the minimum requirement in order to run and install everything properly.

**Pip installations required**:
- pip install pandas
 
**Dependencies used**:
- [sqlite3](https://www.sqlite.org/download.html)
- tkinter (Should be pre-installed with Python3)
- ABC (Abstract Base Class, should be pre-installed with Python3)
- sys
- os
- re
- NumPy (Pre-installed on Python3)