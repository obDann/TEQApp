from abc import ABC, abstractmethod

class BeautifulUploaderAbstract(ABC):
    '''
    An abstract representation of BeautifulUploader
    '''

    @abstractmethod
    def upload_client_profile(self, df, agency):
        '''
        (BeautifulUploaderAbstract, Dataframe, str) -> None
        Uploads template Client Profile into the database.
        '''
    
    @abstractmethod
    def upload_needs_referrals(self, df, agency):
        '''
        (BeautifulUploaderAbstract, Dataframe, str) -> None
        Uploads template Needs Assessment & Referrals into the database.
        '''
    
    @abstractmethod
    def upload_community_connections(self, df, month, year):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template Community Connections into the database.
        '''
    
    @abstractmethod
    def upload_info_ori(self, df, month, year):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template Info & Orientation into the database.
        '''
    
    @abstractmethod
    def upload_employment_service(self, df, month, year):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template Employment Related Service into the database.
        '''
    
    @abstractmethod
    def upload_LT_client_enrol(self, df):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template LT Client Enrolment into the database.
        '''
    
    @abstractmethod
    def upload_LT_course_setup(self, df):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template LT Course Setup into the database.
        '''
    
    @abstractmethod
    def upload_LT_client_exit(self, df):
        '''
        (BeautifulUploaderAbstract, Dataframe) -> None
        Uploads template LT Client Exit into the database.
        '''