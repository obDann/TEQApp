# Code Review

Within Team 10, code reviews are typically informal. However, given the requirements in Deliverable 4, documentation of our code review is provided. The video for the November 8 code review is found [here](https://drive.google.com/file/d/1QWhTOe7yiAyrI3t_L7N8U35C5dqXjaRP/view).

## Review Strategy

Within our team agreement (which can be found [here](../deliverable_1)) there exists a section called "Submission". In this section, a buddy/infinite linked list system is in place. Analogously, the system is in place where "A->B" means A reviews B's work:

`Dann -> Philip -> Riaz -> Susan -> David -> Dann`

The general strategy is to pick out any code that does "stink" off of scripts that are typically 100 to 200 lines of code. Examples of such include:

* Duplicate code
* Long methods
* Big ("God") classes
* Long list of switch/if statements
* Lots of checking for null objects
* Unencapsulated fields/methods
* Dead code
* Hardcoded code

Note that the stinks above is not limited to the above as members are able to make professional judgement on other's code. Positive feedback is also encouraged.

## Code Review Summary (November 8, 2018)

### Dann to Philip
* Noticed that there is at least some injection within the "AggregateValueChecker"; it's great that there is because Philip can make mock objects off of abstract classes.
* Found a potential "stink" in his code where he checks a column name like a "postal code". It can be possible that he could expand this list of if statements; the tradeoff is that he may potentially duplicate code.
    * I recommended Philip to research on the concept of reflection; the idea that you can call methods or instantiate objects with strings (this goes into functional programming territory).
* I recommended a "hard coded" list of constants at the top of his class for checking column names. If someone were to revisit his code, that person would easily know which column names are "aggregated".
* This was not discussed in the video, but I noticed that there was an unencapsulated method in his class. Just a small reminder that a single underscore means "private".

### Philip to Riaz
* Code is easy to follow and understand, also by Riaz's design, it makes things easier when working with the GUI
* Since MissingValueChecker and the function (DataAggregator) I was working on are similar, we have to agree and unify our ideas on how the methods should function
* Only concern about his MissingValueChecker is that, it returns a list of tuples, but it is probably better to return the DataFrame object instead

### Riaz to Susan
* Code is well seperated into classes and imports are clear making it easy to trace code
* Biggest concern was that Observer pattern wasn't implemented, this means changes to button functionality not relating to the view requires changing the view page for the button
	* but I refactored this, this also makes the code easier to follow as button functionality is in its own class and makes adding functionality to buttons easier

### Susan to David

### David to Dann
* Noticed that in is_dropdown_value_mandatory for the true template handler, there are two dummy variables that are being used in order to take up all indexes of a tuple. Instead only the first index should be returned in order to be more efficient.
* In the same function, is_dropdown_value_mandatory, I mentioned that there is a conversion of a string into an integer and then into a boolean right after. Python allows 0's and 1's to act as booleans so the second conversion can be removed so I suggested to just keep it as an integer for conditional statements.
* In handle_template, there is a hardcoded True value returned which is taking memory unnecessarily.
* Otherwise, the rest of the quality of code is sufficient and no further comments could be made.
