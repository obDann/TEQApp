import sys
sys.path.insert(0, "../../database")
from beautiful_uploader import *

class BeautifulUploaderTest():
    def test_upload_client_profile(self):
        df = pd.read_excel('client_profile.xlsx')
        b = BeautifulUploader()
        b.upload_client_profile(df, "XYZ")
    
    def test_upload_needs_referrals(self):
        df = pd.read_excel('needs_referrals.xlsx')
        b = BeautifulUploader()
        b.upload_needs_referrals(df, "XYZ")

    def test_upload_community_connections(self):
        df = pd.read_excel('community_connections.xlsx')
        b = BeautifulUploader()
        b.upload_community_connections(df, "November", "2018")

    def test_upload_info_ori(self):
        df = pd.read_excel('info_ori.xlsx')
        b = BeautifulUploader()
        b.upload_info_ori(df, "October", "2018")

    def test_upload_employment_service(self):
        df = pd.read_excel('employment.xlsx')
        b = BeautifulUploader()
        b.upload_employment_service(df, "July", "2018")

    def test_upload_LT_client_enrol(self):
        df = pd.read_excel('client_enrol.xlsx')
        b = BeautifulUploader()
        b.upload_LT_client_enrol(df)

    def test_upload_LT_course_setup(self):
        df = pd.read_excel('course.xlsx')
        b = BeautifulUploader()
        b.upload_LT_course_setup(df)
    
    def test_upload_LT_client_exit(self):
        df = pd.read_excel('exit.xlsx')
        b = BeautifulUploader()
        b.upload_LT_client_exit(df)        

if __name__ == "__main__":
    bt = BeautifulUploaderTest()
    bt.test_upload_client_profile()
    bt.test_upload_needs_referrals()
    bt.test_upload_community_connections()
    bt.test_upload_info_ori()
    bt.test_upload_employment_service()
    bt.test_upload_LT_course_setup()
    bt.test_upload_LT_client_enrol()
    bt.test_upload_LT_client_exit()
    