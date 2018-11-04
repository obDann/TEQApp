import sqlite3

def create_tables():
    conn = sqlite3.connect('client_data.db')
    cur = conn.cursor()
    
    cur.execute("PRAGMA foreign_keys = ON")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Address (
                ID INT PRIMARY KEY NOT NULL,
                Street_Number INT,
                Street_Name text,
                Street_Type text,
                Street_Direction text,
                Unit text,
                City text,
                Province text,
                Postal_Code text NOT NULL);""")    
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Client (
                Processing_Details text,
                Unique_ID_Type text NOT NULL,
                Unique_ID_Value text PRIMARY KEY NOT NULL,
                Date_Of_Birth INT NOT NULL,
                Phone INT,
                Email INT,
                Email_Address text,
                Official_Language_Preference text NOT NULL,
                Consent_Future INT,
                Address_ID INT,
                Agency text,
                FOREIGN KEY (Address_ID) 
                REFERENCES Address(ID)
                );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Child (
                Client_Unique_ID_Value text NOT NULL,
                Child INT NOT NULL,
                Age text,
                Type_Of_Care text,
                PRIMARY KEY (Child, Client_Unique_ID_Value),
                FOREIGN KEY (Client_Unique_ID_Value) 
                REFERENCES Client(Unique_ID_Value));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Referral (
                 Client_Unique_ID_Value text PRIMARY KEY NOT NULL,
                 Update_Record_ID INT,
                 Service_Postal_Code text NOT NULL,                 
                 Assessment_Start_Date INT NOT NULL,              
                 Service_Language text NOT NULL,
                 Where_Service_Received text NOT NULL,
                 Referred_By text NOT NULL,
                 Canadian_Citizen_Intention INT NOT NULL,
                 Support_Services_Required INT NOT NULL,
                 Non_IRCC_Services INT NOT NULL,
                 Support_Services_Received INT NOT NULL,
                 Settlement_Plan_Completed INT NOT NULL,
                 Assessment_End_Date INT NOT NULL,
                 Reason_For_Update text,
                 FOREIGN KEY (Client_Unique_ID_Value)
                 REFERENCES Client(Unique_ID_Value));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Find_Employment (
                Client_Unique_ID_Value text PRIMARY KEY NOT NULL,
                Find_Employment_R INT,
                Timeframe text,
                Min_One_Year_Exp INT,
                NOC_Level_Intention text,
                Obtain_Credentials_License INT,
                FOREIGN KEY (Client_Unique_ID_Value)
                REFERENCES Referral(Client_Unique_ID_Value));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Improve_Skills (
                Client_Unique_ID_Value text NOT NULL,
                Improve text NOT NULL,
                Description text,
                PRIMARY KEY (Client_Unique_ID_Value, Improve),
                FOREIGN KEY (Client_Unique_ID_Value)
                REFERENCES Referral(Client_Unique_ID_Value));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Client_Needs (
                Client_Unique_ID_Value text NOT NULL,
                Type text NOT NULL,
                Value INT,
                PRIMARY KEY (Client_Unique_ID_Value, Type),
                FOREIGN KEY (Client_Unique_ID_Value)
                REFERENCES Referral(Client_Unique_ID_Value));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Translation_Interpretation (
                Client_Unique_ID_Value text NOT NULL,
                Type text NOT NULL,
                `Between` text NOT NULL,
                `And` text NOT NULL,
                PRIMARY KEY (Client_Unique_ID_Value, Type),
                FOREIGN KEY (Client_Unique_ID_Value)
                REFERENCES Referral(Client_Unique_ID_Value));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Skills (
                 Client_Unique_ID_Value text NOT NULL,
                 Skill text NOT NULL,
                 Value INT NOT NULL,
                 PRIMARY KEY(Client_Unique_ID_Value, Skill),
                 FOREIGN KEY (Client_Unique_ID_Value)
                 REFERENCES Client(Unique_ID_Value));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Target_Group (
                ID INT PRIMARY KEY NOT NULL,
                Children INT,
                Youth INT,
                Senior INT,
                Gender_Specific INT,
                Refugees INT,
                Ethnic_Cultural_Linguistic INT,
                Hearing_Difficulties INT,
                Vision_Difficulties INT,
                LGBTQ INT,
                Families_Parents INT,
                Other_Impairments INT,
                Iregulated_Profession INT,
                Regulated_Trade INT,
                Official_Language_Minorities INT);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS LT_Course (
                Course_Code text PRIMARY KEY NOT NULL,
                Notes text,
                Ongoing_Basis INT NOT NULL,
                Course_Official_Language text NOT NULL,
                Training_Format VARCHAR(100) NOT NULL,
                Location text,
                In_Person_Percentage INT NULL,
                Online_Distance_Percentage INT NULL,
                Total_Num_Spots INT NOT NULL,
                Num_IRCC_Spots INT NOT NULL,
                New_Students_Enrol text NOT NULL,
                Support_Services_Available INT NOT NULL,
                Start_Date INT NOT NULL,
                End_Date INT NOT NULL,
                Instructional_Hours_Per_Class REAL NOT NULL,
                Classes_Per_Week INT NOT NULL,
                Weeks_Of_Instruction INT NULL,
                Weeks_Of_Instruction_Per_Year INT NULL,
                Dominant_Focus text NOT NULL,
                Directed_Target_Group INT NOT NULL,
                Materials_Used INT NOT NULL,
                Citizenship_Prep INT NULL,
                PBLA_Language_Companion INT NULL,
                Target_Group_ID INT NULL,
                FOREIGN KEY (Target_Group_ID)
                REFERENCES Target_Group(ID));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Course_Schedule (
                Course_Code text PRIMARY KEY NOT NULL,
                Time text NOT NULL,
                Value INT NOT NULL,
                FOREIGN KEY (Course_Code)
                REFERENCES LT_Course(Course_Code))""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Instructor (
                Course_Code text NOT NULL,
                Address_ID INT NOT NULL,
                Name text NOT NULL,
                Telephone INT NOT NULL,
                Telephone_Ext INT,
                Email_Address text NOT NULL,
                FOREIGN KEY (Course_Code)
                REFERENCES LT_Course(Course_Code),
                FOREIGN KEY (Address_ID)
                REFERENCES Address(ID))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Client_Enrolment (
                Course_Code text NOT NULL,
                Client_Unique_ID_Value text NOT NULL,
                Date_First_Class INT NOT NULL,
                PRIMARY KEY (Course_Code, Client_Unique_ID_Value),
                FOREIGN KEY (Course_Code)
                REFERENCES LT_Course(Course_Code),
                FOREIGN KEY (Client_Unique_ID_Value)
                REFERENCES Client(Unique_ID_Value));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Client_Exit (
                Course_Code text NOT NULL,
                Client_Unique_ID_Value text NOT NULL,
                Training_Status text NOT NULL,
                Certificate INT NOT NULL,
                Date_Exited INT,
                Reason text,
                Certificate_Listening_Level text,
                Certificate_Speaking_Level text,
                PRIMARY KEY (Course_Code, Client_Unique_ID_Value),
                FOREIGN KEY (Course_Code, Client_Unique_ID_Value)
                REFERENCES 
                Client_Enrolment(Course_Code, Client_Unique_ID_Value));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Client_CLB_Level (
                Course_Code text NOT NULL,
                Client_Unique_ID_Value text NOT NULL,
                Type text NOT NULL,
                Level text NOT NULL,
                PRIMARY KEY (Course_Code, Client_Unique_ID_Value),
                FOREIGN KEY (Course_Code, Client_Unique_ID_Value)
                REFERENCES 
                Client_Exit(Course_Code, Client_Unique_ID_Value))""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Service (
                ID INT PRIMARY KEY NOT NULL,
                Essential_Skills_Apitudes_Training INT,
                Service_Type text NOT NULL);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Employment_Service (
                Service_ID INT PRIMARY KEY NOT NULL,
                Registration_Intervention INT NOT NULL,
                Referral_To text,
                Referral_Date INT,
                Employment_Status text,
                Education_Status text,
                Occupation text,
                Intended_Occupation text,
                Intervention_Type text,
                Hours_Spent INT,
                Minutes_Spent INT,
                FOREIGN KEY (Service_ID)
                REFERENCES Service(ID));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Info_and_Orientation (
                Service_ID INT PRIMARY KEY NOT NULL,
                Target_Group_ID INT,
                Service_Start_Date INT NOT NULL,
                Services_Received text NOT NULL,
                Total_Length text,
                Total_Length_Hours INT,
                Total_Length_Minutes INT,
                Num_Clients text,
                Life_Skills_Responsibilites INT NOT NULL,
                Service_End_Date INT NOT NULL,
                FOREIGN KEY (Target_Group_ID)
                REFERENCES Target_Group(ID)
                FOREIGN KEY (Service_ID)
                REFERENCES Service(ID));""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS Service_Needs (
                Service_ID INT NOT NULL,
                Type text NOT NULL,
                Value text NOT NULL,
                PRIMARY KEY (Service_ID, Type),
                FOREIGN KEY (Service_ID)
                REFERENCES Service(ID))""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Community_Connections (
                Service_ID INT NOT NULL,
                Target_Group_ID INT,
                Activity text NOT NULL,
                Type_of_Event text,
                Type_of_Service text,
                Main_Topic text NOT NULL,
                Service_Received text NOT NULL,
                Num_Unique_Participants text,
                Volunteer_Participation INT,
                Service_Status text NOT NULL,
                Reason_Leaving_Service text,
                Start_Date INT NOT NULL,
                End_Date INT,
                Projected_End_Date INT,
                Total_Length_Hours INT,
                Total_Length_Minutes INT,
                PRIMARY KEY (Service_ID),
                FOREIGN KEY (Target_Group_ID)
                REFERENCES Target_Group(ID)
                FOREIGN KEY (Service_ID)
                REFERENCES Service(ID));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Long_Term_Intervention (
                ID INT PRIMARY KEY NOT NULL,
                Service_ID INT NOT NULL,
                Intervention_Received text,
                Intervention_Status text,
                Reason_Leaving text,
                Intervention_Start_Date INT,
                Intervention_End_Date INT,
                Employer_Size text,
                Placement_Was text,
                Hours_Per_Week text,
                Met_Mentor_Regularly_At text,
                Avg_Hours_Per_Week INT,
                Profession text,
                FOREIGN KEY (Service_ID)
                REFERENCES Employment_Related_Service(Service_ID));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Short_Term_Intervention (
                ID INT PRIMARY KEY NOT NULL,
                Service_ID INT NOT NULL,
                Service_Received text NOT NULL,
                Date INT,
                FOREIGN KEY (Service_ID)
                REFERENCES Employment_Related_Service(Service_ID));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Skill_Levels (
                Course_Code text NOT NULL,
                Type text NOT NULL,
                Amount INT NOT NULL,
                PRIMARY KEY (Course_Code, Type),
                FOREIGN KEY (Course_Code)
                REFERENCES LT_Course(Course_Code));""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Client_Attends_Service (
                Service_ID INT NOT NULL,
                Client_Unique_ID_Value text NOT NULL,
                Month text NOT NULL,
                Year text NOT NULL,
                PRIMARY KEY (Service_ID, Client_Unique_ID_Value),
                FOREIGN KEY (Service_ID) REFERENCES Service(ID)
                FOREIGN KEY (Client_Unique_ID_Value)
                REFERENCES Client(Unique_ID_Value));""")