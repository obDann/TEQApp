from beautiful_uploader_abstract import BeautifulUploaderAbstract
import database_methods
import insert_client_profile
import insert_community_connections
import insert_course_setup
import insert_employment
import insert_info_ori
import insert_needs_assessment
import insert_client_enrol
import insert_client_exit
import pandas as pd

class BeautifulUploader(BeautifulUploaderAbstract):
    def upload_client_profile(self, df, agency):
        '''
        (BeautifulUploaderAbstract, Dataframe, str) -> None
        Uploads template Client Profile into the database. Agency refers to
        the clients agency.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            row = df.iloc[i]
            address_id = insert_client_profile.insert_address(column, row)
            insert_client_profile.insert_client(column, row, address_id, agency)
            i += 1
    
    def upload_needs_referrals(self, df, agency):
        '''
        (BeautifulUploaderAbstract, Dataframe, str) -> None
        Uploads template Needs Assessment & Referrals into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            # get client id
            client_id = df.iloc[i][3]
            row = df.iloc[i]
            inserted = insert_needs_assessment.insert_referral(column, row, 
                                                               client_id, 
                                                               agency)
            insert_needs_assessment.insert_child(row, client_id)
            insert_needs_assessment.insert_trans_int(row, client_id)
            insert_needs_assessment.insert_find_employment(row, client_id)
            insert_needs_assessment.insert_improve_skills(column, row, 
                                                          client_id)
            insert_needs_assessment.insert_client_needs(column, row, client_id)
            i += 1

    def upload_community_connections(self, df, month, year):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template Community Connections into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            # get client id
            client_id = df.iloc[i][3]
            row = df.iloc[i]
            insert_community_connections.update_client_profile(client_id, row)
            target_id = insert_community_connections.insert_target(row)
            service_id = insert_community_connections.insert_service(row)
            insert_community_connections.insert_community_conn(row, service_id,
                                                               target_id)
            insert_community_connections.client_attends_service(service_id,
                                                                client_id,
                                                                month, year)
            insert_community_connections.insert_skills(column, row, client_id)
            insert_community_connections.update_child(row, client_id)
            i += 1

    def upload_info_ori(self, df, month, year):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template Info & Orientation into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            # get client id
            client_id = df.iloc[i][3]            
            row = df.iloc[i]
            target_id = insert_info_ori.insert_target(row)
            service_id = insert_info_ori.insert_service(row)
            insert_info_ori.insert_info_and_ori(row, service_id, target_id)
            insert_info_ori.client_attends_service(service_id, client_id, month,
                                                   year)            
            insert_info_ori.insert_service_needs(column, row, service_id)
            insert_info_ori.update_client_profile(row, client_id)
            i += 1
    
    def upload_employment_service(self, df, month, year):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template Employment Related Service into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            # get client id
            client_id = df.iloc[i][3]
            row = df.iloc[i]
            service_id = insert_employment.insert_service(row)
            insert_employment.insert_employment(row, service_id)
            insert_employment.insert_long_term(row, service_id)
            insert_employment.insert_short_term(row, service_id)
            insert_employment.client_attends_service(service_id, client_id, 
                                                     month, year)
            insert_employment.update_client_profile(client_id, row)
            insert_employment.update_child(row, client_id)
            i += 1
    
    def upload_LT_client_enrol(self, df):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template LT Client Enrolment into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        while (i < total_rows):
            # get client id
            client_id = df.iloc[i][3]
            # get course code
            course_code = df.iloc[i][6]
            row = df.iloc[i]
            insert_client_enrol.insert_client_enrol(row, client_id, course_code)
            insert_client_enrol.update_client_profile(client_id, row)
            insert_client_enrol.update_child(row, client_id)
            i += 1

    def upload_LT_course_setup(self, df):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template LT Course Setup into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            # get course code
            course_code = df.iloc[i][2]
            row = df.iloc[i]
            # if course was not already inserted into the database
            if (not(database_methods.check_course(course_code, 
                                                  'client_data.db'))):            
                target_id = insert_course_setup.insert_target_group(row)
                address_id = insert_course_setup.insert_instructor_address(row)
                insert_course_setup.insert_course(row, target_id)
                insert_course_setup.insert_instructor(row, course_code, 
                                                      address_id)
                insert_course_setup.insert_skill_levels(column, row, 
                                                        course_code)
                insert_course_setup.insert_course_schedule(column, row, 
                                                           course_code)
            i += 1
    
    def upload_LT_client_exit(self, df):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template LT Client Exit into the database.
        '''
        # get the number of rows in the dataframe
        total_rows = df.shape[0]
        # data starts at row 2
        i = 2
        column = df.iloc[1]
        while (i < total_rows):
            # get client id
            client_id = df.iloc[i][3]
            # get course code
            course_code = df.iloc[i][5]
            # check client_id and course_code exists in tables
            key = (course_code, client_id)
            row = df.iloc[i]
            if (database_methods.check_id(key, 'client_data.db', "Client_Exit",
                                          ("(Course_Code, " + 
                                          "Client_Unique_ID_Value)"))):
                insert_client_exit.insert_client_exit(row, client_id, 
                                                      course_code)
                insert_client_exit.insert_CLB_level(column, row, client_id,
                                                    course_code)
                insert_client_exit.insert_client_enrol.update_child(row, 
                                                                    client_id)
            insert_client_exit.update_client_profile(client_id, row)
            i += 1