CREATE SCHEMA IF NOT EXISTS `client_data` DEFAULT CHARACTER SET utf8 ;
USE `client_data` ;

-- -----------------------------------------------------
-- Table `client_data`.`Client` contains data in 'Client Profile' template
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Client` (
  `Unique_ID_Type` VARCHAR(100) NOT NULL,
  `Unique_ID_Value` VARCHAR(45) NOT NULL,
  `Processing_Details` VARCHAR(100) NULL,
  `Date_Of_Birth` DATETIME NOT NULL,
  `Official_Language_Preference` VARCHAR(45) NOT NULL,
  `Email?` CHAR(1) NULL,
  `Email_Address` VARCHAR(100) NULL,
  `Street_Number` INT NULL,
  `Street_Name` VARCHAR(45) NULL,
  `Street_Type` VARCHAR(45) NULL,
  `Street_Direction` VARCHAR(45) NULL,
  `Unit` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `Province` VARCHAR(45) NULL,
  `Postal_Code` VARCHAR(45) NULL,
  `Consent_Future` VARCHAR(45) NULL,
  `Phone` VARCHAR(12) NULL,
  PRIMARY KEY (`Unique_ID_Value`));

-- -----------------------------------------------------
-- Table `client_data`.`Child`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Child` (
  `Number` INT NOT NULL,
  `Client_Unique_ID_Value` VARCHAR(45) NOT NULL,
  `Age` VARCHAR(45) NOT NULL,
  `Type of Care` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Number`, `Client_Unique_ID_Value`),
  INDEX `fk_Child_Client_idx` (`Client_Unique_ID_Value` ASC),
  CONSTRAINT `fk_Child_Client`
    FOREIGN KEY (`Client_Unique_ID_Value`)
    REFERENCES `client_data`.`Client` (`Unique_ID_Value`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Referral` contains client data in 'Needs Assessment and Referrals' template
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Referral` (
  `ID` INT NOT NULL,
  `Client_Unique_ID_Value` VARCHAR(45) NOT NULL UNIQUE,
  `Update_Record_ID` INT NULL,
  `Service_Postal_Code` VARCHAR(45) NOT NULL,
  `Assessment_Start_Date` DATETIME NOT NULL,
  `Assessment_End_Date` DATETIME NOT NULL,
  `Service_Language` VARCHAR(45) NOT NULL,
  `Where_Service_Received` VARCHAR(45) NOT NULL,
  `Referred_By` VARCHAR(45) NOT NULL,
  `Canadian_Citizen_Intention` CHAR(1) NOT NULL,
  `Support_Services_Required` CHAR(1) NOT NULL,
  `Care_Newcomer_Children` CHAR(1) NULL,
  `Support_Services_Received` CHAR(1) NOT NULL,
  `Settlement_Plan_Completed` CHAR(1) NOT NULL,
  `Find_Employment` CHAR(1) NULL,
  `Transportation` CHAR(1) NULL,
  `Provisions_For_Disabilities` CHAR(1) NULL,
  `Translation` CHAR(1) NULL,
  `Interpretation` CHAR(1) NULL,
  `Crisis_Counselling` CHAR(1) NULL,
  `Non_IRCC_Services` CHAR(1) NOT NULL,
  `Food_Clothing_Other` CHAR(1) NULL,
  `Food_Clothing_Other_R` CHAR(1) NULL,
  `Housing_Accomodation` CHAR(1) NULL,
  `Housing_Accomodation_R` CHAR(1) NULL,
  `Health_Mental` CHAR(1) NULL,
  `Health_Mental_R` CHAR(1) NULL,
  `Financial` CHAR(1) NULL,
  `Financial_R` CHAR(1) NULL,
  `Family_Support` CHAR(1) NULL,
  `Family_Support_R` CHAR(1) NULL,
  `Language_NonIRCC` CHAR(1) NULL,
  `Language_NonIRCC_R` CHAR(1) NULL,
  `Edu_Skills_Development` CHAR(1) NULL,
  `Edu_Skills_Development_R` CHAR(1) NULL,
  `Employment_Related` CHAR(1) NULL,
  `Employment_Related_R` CHAR(1) NULL,
  `Legal_Info_Services` CHAR(1) NULL,
  `Legal_Info_Services_R` CHAR(1) NULL,
  `Community_Services` CHAR(1) NULL,
  `Community_Services_R` CHAR(1) NULL,
  `Reason_For_Update` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Referral_Client1_idx` (`Client_Unique_ID_Value` ASC),
  CONSTRAINT `fk_Referral_Client1`
    FOREIGN KEY (`Client_Unique_ID_Value`)
    REFERENCES `client_data`.`Client` (`Unique_ID_Value`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Target_Group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Target_Group` (
  `ID` INT NOT NULL,
  `Children(0-14yrs)` CHAR(1) NULL,
  `Youth(15-24yrs)` CHAR(1) NULL,
  `Senior` CHAR(1) NULL,
  `Gender_Specific` CHAR(1) NULL,
  `Refugees` CHAR(1) NULL,
  `Ethnic_Cultural_Linguistic` CHAR(1) NULL,
  `Hearing_Difficulties` CHAR(1) NULL,
  `Vision_Difficulties` CHAR(1) NULL,
  `LGBTQ` CHAR(1) NULL,
  `Families_Parents` CHAR(1) NULL,
  `Other_Impairments` CHAR(1) NULL,
  `International_Training_Regulated_Profession` CHAR(1) NULL,
  `Internation_Training_Regulated_Trade` CHAR(1) NULL,
  `Official_Language_Minorities` CHAR(1) NULL,
  PRIMARY KEY (`ID`));


-- -----------------------------------------------------
-- Table `client_data`.`Language_Training_Course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Language_Training_Course` (
  `Course_Code` INT NOT NULL,
  `Notes` VARCHAR(100) NULL,
  `Ongoing_Basis` CHAR(1) NOT NULL,
  `Course_Official_Language` VARCHAR(45) NOT NULL,
  `Training_Format` VARCHAR(100) NOT NULL,
  `Location` VARCHAR(45) NULL,
  `In_Person_Percentage` INT NULL,
  `Online_Distance_Percentage` INT NULL,
  `Total_Num_Spots` INT NOT NULL,
  `Num_IRCC_Spots` INT NOT NULL,
  `New_Students_Enrol` VARCHAR(45) NOT NULL,
  `Support_Services_Available` CHAR(1) NOT NULL,
  `Start_Date` DATETIME NOT NULL,
  `End_Date` DATETIME NOT NULL,
  `Instructional_Hours_Per_Class` DECIMAL(4,2) NOT NULL,
  `Classes_Per_Week` INT NOT NULL,
  `Dominant_Focus` VARCHAR(100) NOT NULL,
  `Directed_Target_Group` CHAR(1) NOT NULL,
  `Materials_Used` CHAR(1) NOT NULL,
  `Morning` CHAR(1) NULL,
  `Afternoon` CHAR(1) NULL,
  `Evening` CHAR(1) NULL,
  `Weekend` CHAR(1) NULL,
  `Anytime` CHAR(1) NULL,
  `Online` CHAR(1) NULL,
  `Weeks_Of_Instruction` INT NULL,
  `Weeks_Of_Instruction_Per_Year` INT NULL,
  `Citizenship_Prep` CHAR(1) NULL,
  `PBLA_Language_Companion` CHAR(1) NULL,
  `Target_Group_ID` INT NULL,
  PRIMARY KEY (`Course_Code`),
  INDEX `fk_Language_Training_Course_Target_Group1_idx` (`Target_Group_ID` ASC),
  CONSTRAINT `fk_Language_Training_Course_Target_Group1`
    FOREIGN KEY (`Target_Group_ID`)
    REFERENCES `client_data`.`Target_Group` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Client_Enrolment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Client_Enrolment` (
  `Course_Code` INT NOT NULL,
  `Client_Unique_ID_Value` VARCHAR(45) NOT NULL,
  `Date_First_Class` DATETIME NOT NULL,
  PRIMARY KEY (`Course_Code`, `Client_Unique_ID_Value`),
  INDEX `fk_Course_has_Client_Client1_idx` (`Client_Unique_ID_Value` ASC),
  INDEX `fk_Course_has_Client_Course1_idx` (`Course_Code` ASC),
  CONSTRAINT `fk_Course_has_Client_Course1`
    FOREIGN KEY (`Course_Code`)
    REFERENCES `client_data`.`Language_Training_Course` (`Course_Code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Course_has_Client_Client1`
    FOREIGN KEY (`Client_Unique_ID_Value`)
    REFERENCES `client_data`.`Client` (`Unique_ID_Value`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Client_Exit`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Client_Exit` (
  `Course_Code` INT NOT NULL,
  `Client_Unique_ID_Value` VARCHAR(45) NOT NULL,
  `Training_Status` VARCHAR(45) NOT NULL,
  `Certificate` CHAR(1) NOT NULL,
  `Date_Exited` DATETIME NULL,
  `Reason` VARCHAR(45) NULL,
  `Listening_CLB_Level` VARCHAR(45) NULL,
  `Speaking_CLB_Level` VARCHAR(45) NULL,
  `Reading_CLB_Level` VARCHAR(45) NULL,
  `Writing_CLB_Level` VARCHAR(45) NULL,
  `Certificate_Listening_Level` VARCHAR(45) NULL,
  `Certificate_Speaking_Level` VARCHAR(45) NULL,
  PRIMARY KEY (`Course_Code`, `Client_Unique_ID_Value`, `Training_Status`),
  INDEX `fk_Client_Exit_Client_Enrolment1_idx` (`Course_Code` ASC, `Client_Unique_ID_Value` ASC),
  CONSTRAINT `fk_Client_Exit_Client_Enrolment1`
    FOREIGN KEY (`Course_Code` , `Client_Unique_ID_Value`)
    REFERENCES `client_data`.`Client_Enrolment` (`Course_Code` , `Client_Unique_ID_Value`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Skills`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Skills` (
  `ID` INT NOT NULL,
  `Computer_Skills` CHAR(1) NULL,
  `Document_Use` CHAR(1) NULL,
  `Interpersonal_Workplace` CHAR(1) NULL,
  `Leadership_Training` CHAR(1) NULL,
  `Life_Skills` CHAR(1) NULL,
  `Numeracy` CHAR(1) NULL,
  `Client_Unique_ID_Value` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Skills_Client1_idx` (`Client_Unique_ID_Value` ASC),
  CONSTRAINT `fk_Skills_Client1`
    FOREIGN KEY (`Client_Unique_ID_Value`)
    REFERENCES `client_data`.`Client` (`Unique_ID_Value`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Service` (
  `ID` INT NOT NULL,
  `Essential_Skills_Apitudes_Training` CHAR(1) NULL,
  `Service_Type` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));


-- -----------------------------------------------------
-- Table `client_data`.`Employment_Related_Service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Employment_Related_Service` (
  `Service_ID` INT NOT NULL,
  `Registration_Intervention` CHAR(1) NOT NULL,
  `Referral_To` VARCHAR(45) NULL,
  `Referral_Date` DATETIME NULL,
  `Employment_Status` VARCHAR(45) NULL,
  `Education_Status` VARCHAR(45) NULL,
  `Occupation` VARCHAR(100) NULL,
  `Intended_Occupation` VARCHAR(100) NULL,
  `Intervention_Type` VARCHAR(45) NULL,
  `Hours_Spent` INT NULL,
  `Minutes_Spent` INT NULL,
  INDEX `fk_Employment_Related_Service_Service1_idx` (`Service_ID` ASC),
  PRIMARY KEY (`Service_ID`),
  CONSTRAINT `fk_Employment_Related_Service_Service1`
    FOREIGN KEY (`Service_ID`)
    REFERENCES `client_data`.`Service` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Info_and_Orientation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Info_and_Orientation` (
  `Service_ID` INT NOT NULL,
  `Service_Start_Date` DATETIME NOT NULL,
  `Services_Received` VARCHAR(100) NOT NULL,
  `Total_Length` VARCHAR(45) NULL,
  `Total_Length_Hours` VARCHAR(45) NULL,
  `Total_Length_Minutes` VARCHAR(45) NULL,
  `Num_Clients` VARCHAR(45) NULL,
  `Target_Group` CHAR(1) NULL,
  `Overview_Of_Canada` CHAR(1) NULL,
  `Overview_Canada_Referrals` CHAR(1) NULL,
  `Sources_Information` CHAR(1) NULL,
  `Sources_Information_Referrals` CHAR(1) NULL,
  `Rights_Freedoms` CHAR(1) NULL,
  `Rights_Freedom_Referrals` CHAR(1) NULL,
  `Canadian_Law_Justice` CHAR(1) NULL,
  `Canadian_Law_Justice_Referrals` CHAR(1) NULL,
  `Important_Documents` CHAR(1) NULL,
  `Important_Document_Referrals` CHAR(1) NULL,
  `Improving_Eng_Fr` CHAR(1) NULL,
  `Improving_Eng_Fr_Referrals` CHAR(1) NULL,
  `Employment_Income` CHAR(1) NULL,
  `Employment_Income_Referrals` CHAR(1) NULL,
  `Education` CHAR(1) NULL,
  `Education_Referrals` CHAR(1) NULL,
  `Housing` CHAR(1) NULL,
  `Housing_Referrals` CHAR(1) NULL,
  `Health` CHAR(1) NULL,
  `Health_Referrals` CHAR(1) NULL,
  `Finance` CHAR(1) NULL,
  `Finance_Referrals` CHAR(1) NULL,
  `Transportation` CHAR(1) NULL,
  `Transportation_Referrals` CHAR(1) NULL,
  `Communications_Media` CHAR(1) NULL,
  `Communications_Media_Referrals` CHAR(1) NULL,
  `Community_Engagement` CHAR(1) NULL,
  `Community_Engagement_Referrals` CHAR(1) NULL,
  `Becoming_Canadian_Citizen` CHAR(1) NULL,
  `Becoming_Canadian_Citizen_R` CHAR(1) NULL,
  `Interpersonal_Conflict` CHAR(1) NULL,
  `Interpersonal_Conflict_R` CHAR(1) NULL,
  `Life_Skills_Responsibilites` CHAR(1) NOT NULL,
  `Citizenship_Rights_Responsibilities` CHAR(1) NULL,
  `Service_End_Date` DATETIME NOT NULL,
  `Target_Group_ID` INT NULL,
  PRIMARY KEY (`Service_ID`),
  INDEX `fk_Info_and_Orientation_Target_Group1_idx` (`Target_Group_ID` ASC),
  INDEX `fk_Info_and_Orientation_Service1_idx` (`Service_ID` ASC),
  CONSTRAINT `fk_Info_and_Orientation_Target_Group1`
    FOREIGN KEY (`Target_Group_ID`)
    REFERENCES `client_data`.`Target_Group` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Info_and_Orientation_Service1`
    FOREIGN KEY (`Service_ID`)
    REFERENCES `client_data`.`Service` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Community_Connections`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Community_Connections` (
  `Service_ID` INT NOT NULL,
  `Activity` VARCHAR(45) NOT NULL,
  `Type_of_Event` VARCHAR(45) NULL,
  `Type_of_Service` VARCHAR(45) NULL,
  `Main_Topic` VARCHAR(45) NOT NULL,
  `Service_Received` VARCHAR(45) NOT NULL,
  `Num_Unique_Participants` VARCHAR(45) NULL,
  `Host_Community_Volunteer_Participation` CHAR(1) NULL,
  `Directed_Target_Group` CHAR(1) NULL,
  `Service_Status` VARCHAR(100) NOT NULL,
  `Reason_Leaving_Service` VARCHAR(150) NULL,
  `Start_Date` DATETIME NOT NULL,
  `End_Date` DATETIME NULL,
  `Projected_End_Date` DATETIME NULL,
  `Total_Length_Hours` INT NULL,
  `Total_Length_Minutes` INT NULL,
  `Target_Group_ID` INT NULL,
  INDEX `fk_Community_Connections_Target_Group1_idx` (`Target_Group_ID` ASC),
  INDEX `fk_Community_Connections_Service1_idx` (`Service_ID` ASC),
  PRIMARY KEY (`Service_ID`),
  CONSTRAINT `fk_Community_Connections_Target_Group1`
    FOREIGN KEY (`Target_Group_ID`)
    REFERENCES `client_data`.`Target_Group` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Community_Connections_Service1`
    FOREIGN KEY (`Service_ID`)
    REFERENCES `client_data`.`Service` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Long_Term_Intervention`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Long_Term_Intervention` (
  `ID` INT NOT NULL,
  `Intervention_Received` VARCHAR(45) NULL,
  `Intervention_Status` VARCHAR(45) NULL,
  `Reason_Leaving` VARCHAR(45) NULL,
  `Intervention_Start_Date` DATETIME NULL,
  `Intervention_End_Date` DATETIME NULL,
  `Employer_Size` VARCHAR(100) NULL,
  `Placement_Was` VARCHAR(45) NULL,
  `Hours_Per_Week` VARCHAR(45) NULL,
  `Met_Mentor_Regularly_At` VARCHAR(45) NULL,
  `Avg_Hours_Per_Week` INT NULL,
  `Profession` VARCHAR(45) NULL,
  `Service_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Long_Term_Intervention_Employment_Related_Service1_idx` (`Service_ID` ASC),
  CONSTRAINT `fk_Long_Term_Intervention_Employment_Related_Service1`
    FOREIGN KEY (`Service_ID`)
    REFERENCES `client_data`.`Employment_Related_Service` (`Service_ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Short_Term_Intervention`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Short_Term_Intervention` (
  `ID` INT NOT NULL,
  `Service_Received` VARCHAR(45) NULL,
  `Date` DATETIME NULL,
  `Service_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Short_Term_Intervention_Employment_Related_Service1_idx` (`Service_ID` ASC),
  CONSTRAINT `fk_Short_Term_Intervention_Employment_Related_Service1`
    FOREIGN KEY (`Service_ID`)
    REFERENCES `client_data`.`Employment_Related_Service` (`Service_ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Increase_Knowledge`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Increase_Knowledge` (
  `ID` INT NOT NULL,
  `Referral_ID` INT NOT NULL,
  `Life_In_Canada` CHAR(1) NULL,
  `Life_In_Canada_R` CHAR(1) NULL,
  `Community_Government_Services` CHAR(1) NULL,
  `Community_Government_Services_R` CHAR(1) NULL,
  `Working_In_Canada` CHAR(1) NULL,
  `Working_In_Canada_R` CHAR(1) NULL,
  `Canada_Education` CHAR(1) NULL,
  `Canada_Education_R` CHAR(1) NULL,
  `Social_Networks` CHAR(1) NULL,
  `Social_Networks_R` CHAR(1) NULL,
  `Professional_Networks` CHAR(1) NULL,
  `Professional_Networks_R` CHAR(1) NULL,
  `Access_Community_Services` CHAR(1) NULL,
  `Access_Community_Services_R` CHAR(1) NULL,
  `Level_Community_Involvment` CHAR(1) NULL,
  `Level_Community_Involvement_R` CHAR(1) NULL,
  `Language_Skills` CHAR(1) NULL,
  `Language_Skills_R` CHAR(1) NULL,
  `Improve_Language_Skills_To` VARCHAR(45) NULL,
  `Other_Skills` CHAR(1) NULL,
  `Other_Skills_R` CHAR(1) NULL,
  `Improve_Other_Skills_To` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Increase_Knowledge_Referral1_idx` (`Referral_ID` ASC),
  CONSTRAINT `fk_Increase_Knowledge_Referral1`
    FOREIGN KEY (`Referral_ID`)
    REFERENCES `client_data`.`Referral` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Find_Employment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Find_Employment` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Referral_ID` INT NOT NULL,
  `Find_Employment_R` CHAR(1) NULL,
  `Timeframe` VARCHAR(45) NULL,
  `Min_One_Year_Experience` CHAR(1) NULL,
  `NOC_Level_Intnetion` VARCHAR(45) NULL,
  `Obtain_Credentials_License` CHAR(1) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Find_Employment_Referral1_idx` (`Referral_ID` ASC),
  CONSTRAINT `fk_Find_Employment_Referral1`
    FOREIGN KEY (`Referral_ID`)
    REFERENCES `client_data`.`Referral` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Translation_Interpretation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Translation_Interpretation` (
  `Type` VARCHAR(45) NOT NULL,
  `Referral_ID` INT NOT NULL,
  `Between` VARCHAR(45) NOT NULL,
  `And` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Type`, `Referral_ID`),
  INDEX `fk_Translation_Referral1_idx` (`Referral_ID` ASC),
  CONSTRAINT `fk_Translation_Referral1`
    FOREIGN KEY (`Referral_ID`)
    REFERENCES `client_data`.`Referral` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `client_data`.`Skill_Levels`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Skill_Levels` (
  `Type` VARCHAR(100) NOT NULL,
  `Course_Code` INT NOT NULL,
  `Level1` VARCHAR(45) NULL,
  `Level2` VARCHAR(45) NULL,
  `Level3` VARCHAR(45) NULL,
  `Level4` VARCHAR(45) NULL,
  `Level5` VARCHAR(45) NULL,
  `Level6` VARCHAR(45) NULL,
  `Level7` VARCHAR(45) NULL,
  `Level8` VARCHAR(45) NULL,
  `Level9` VARCHAR(45) NULL,
  `Level10` VARCHAR(45) NULL,
  `Level11` VARCHAR(45) NULL,
  `Level12` VARCHAR(45) NULL,
  `Level13` VARCHAR(45) NULL,
  `Level14` VARCHAR(45) NULL,
  `Level15` VARCHAR(45) NULL,
  `Level16` VARCHAR(45) NULL,
  `Level17` VARCHAR(45) NULL,
  PRIMARY KEY (`Type`, `Course_Code`),
  INDEX `fk_Listening_Skill_Levels_Language_Training_Course1_idx` (`Course_Code` ASC),
  CONSTRAINT `fk_Listening_Skill_Levels_Language_Training_Course1`
    FOREIGN KEY (`Course_Code`)
    REFERENCES `client_data`.`Language_Training_Course` (`Course_Code`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

-- -----------------------------------------------------
-- Table `client_data`.`Client_Attends_Service`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `client_data`.`Client_Attends_Service` (
  `Service_ID` INT NOT NULL,
  `Client_Unique_ID_Value` VARCHAR(45) NOT NULL,
  `Month` VARCHAR(45) NOT NULL,
  `Year` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Service_ID`, `Client_Unique_ID_Value`),
  INDEX `fk_Service_has_Client_Client1_idx` (`Client_Unique_ID_Value` ASC),
  INDEX `fk_Service_has_Client_Service1_idx` (`Service_ID` ASC),
  CONSTRAINT `fk_Service_has_Client_Service1`
    FOREIGN KEY (`Service_ID`)
    REFERENCES `client_data`.`Service` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Service_has_Client_Client1`
    FOREIGN KEY (`Client_Unique_ID_Value`)
    REFERENCES `client_data`.`Client` (`Unique_ID_Value`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);
