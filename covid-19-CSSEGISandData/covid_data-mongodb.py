from github import Github 
import pymongo
import os
import sys

class Covid19Data:
    def __init__(self):
        self.mongo = pymongo.MongoClient(
                           host=os.environ['MHOST'],
                           port=int(os.environ['MPORT']),
                           username=os.environ['MUSER'],
                           password=os.environ['MPASS'],
                           authSource="admin") 
        self.db = self.mongo['covid']
        self.collection = self.db['csvdata']
        self.github = Github( os.environ['USER'], os.environ['PASS'] )
        self.github_repo = "CSSEGISandData/COVID-19"
        self.db_csv_filenames = None


    def __call__(self):
        self._get_data()


    def _get_data(self, path="csse_covid_19_data/csse_covid_19_daily_reports_us"):
        '''
        Gets new data from github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports_us
        '''
        self.repo = repo = self.github.get_repo( self.github_repo )
        repo_files_list = repo.get_contents(path)
        for repo_file in repo_files_list:
            if 'README.md' in repo_file.path:
                continue
            csv_filename = repo_file.path.split('/')[-1]
            if self._file_in_db( csv_filename ):
                continue
            content = repo.get_contents(repo_file.path).decoded_content.decode("UTF-8")
            self._add_csv_file( csv_filename, content )
            sys.exit()


    def _file_in_db(self,csv_filename):
        if not self.db_csv_filenames:
            docs = list(self.collection.find({},{"_id":0,"filename":1}))
            self.db_csv_filenames = [x['filename'] for x in docs] 
        return csv_filename in self.db_csv_filenames


    def _add_csv_file(self,csv_filename, csv_data):
        mongodoc = {"filename":csv_filename,"data":csv_data}
        ret = self.collection.insert_one(mongodoc)
        sys.stderr.write('add '+csv_filename+'\n')
        sys.stderr.write('ret '+str(ret)+'\n')
        

if __name__ == '__main__':
    Covid19Data()()

