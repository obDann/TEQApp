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

**November 12 2018**: Sprint 4 completed. GUI and Terminal have been merged and some additional features have also been added. Unittests have been automated using travis and manual tests have READMEs included in their respective folders in [src/tests](./src/tests). Features included in the GUI are, user creation, logging in with a created user, appropriate page will be displayed based on creation, agency users can upload an excel file, and if it has multiple sheets, can choose which sheet to upload. Setup for this sprint is presented below.

    Within the  [src/main](./src/main) folder, run 'python3 main.py' in your terminal and a GUI will pop up. This is the main page, where you can choose to login or create an account.

**November 26 2018**: Last sprint completed. Final user stories and personas are found [here](./teamOverview/productBacklog). Code reviews are found [here](./teamOverview/code_review). Running the application: after installing all of the pip installations, within the  [src/main](./src/main) folder, run `python3 main.py` in your terminal. Refer to the user manual in [userGuide](./userGuide) for help with how to use our application.

## Setup

**Python 3** is the minimum requirement in order to run and install everything properly.

**Pip installations required**:
- `pip3 install pandas`
- `pip3 install sendgrid`
- `pip3 install xlrd`
- `pip3 install passlib`
- `pip3 install scipy`
- `pip3 install matplotlib`
- `pip3 install passlib`
 
>>>>>>> master
**Dependencies used**:
- [sqlite3](https://www.sqlite.org/download.html)
- tkinter (Should be pre-installed with Python3)
- ABC (Abstract Base Class, should be pre-installed with Python3)
- sys
- os
- re
- NumPy (Pre-installed on Python3)
