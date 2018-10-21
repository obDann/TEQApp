CREATE SCHEMA IF NOT EXISTS `users`;
USE `users` ;

-- -----------------------------------------------------
-- Table `users`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users`.`User` (
  `Username` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Date_Created` DATETIME NOT NULL,
  PRIMARY KEY (`Username`));


-- -----------------------------------------------------
-- Table `users`.`Agency_User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users`.`Agency_User` (
  `Username` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Username`),
  INDEX `fk_Agency_User_User1_idx` (`Username` ASC),
  CONSTRAINT `fk_Agency_User_User1`
    FOREIGN KEY (`Username`)
    REFERENCES `users`.`User` (`Username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `users`.`Submission_History`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users`.`Submission_History` (
  `ID` INT NOT NULL,
  `Username` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Type` VARCHAR(45) NOT NULL,
  `Month_File` VARCHAR(45) NOT NULL,
  `Year_File` INT(4) NOT NULL,
  `Date_Submitted` DATETIME NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_iCare_File_Agency_User1_idx` (`Username` ASC),
  CONSTRAINT `fk_iCare_File_Agency_User1`
    FOREIGN KEY (`Username`)
    REFERENCES `users`.`Agency_User` (`Username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

-- -----------------------------------------------------
-- Table `users`.`Request`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `users`.`Request` (
  `ID` VARCHAR(45) NOT NULL,
  `Username` VARCHAR(45) NOT NULL,
  `Admin_Username` VARCHAR(45) NULL,
  `Description` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `Date_Submitted` VARCHAR(45) NOT NULL,
  `Date_Accepted` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_User_has_User_User2_idx` (`Admin_Username` ASC),
  INDEX `fk_User_has_User_User1_idx` (`Username` ASC),
  CONSTRAINT `fk_User_has_User_User1`
    FOREIGN KEY (`Username`)
    REFERENCES `users`.`User` (`Username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_User_User2`
    FOREIGN KEY (`Admin_Username`)
    REFERENCES `users`.`User` (`Username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
