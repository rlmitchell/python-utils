from github import Github 
import sqlite3
import os
import sys


class Covid19Data:
    def __init__(self, db_file='covid_data.sql'):
        self.github = Github( os.environ['USER'], os.environ['PASS'] )
        self.github_repo = "CSSEGISandData/COVID-19"
        self.db = sqlite3.connect(db_file)
        self.db_csv_filenames = None


    def __call__(self):
        self._get_data()


    def _file_in_db(self,csv_filename):
        if not self.db_csv_filenames:
            cur = self.db.cursor()
            cur.execute("select filename from covid_data") 
            rows = cur.fetchall()
            self.db_csv_filenames = [x[0] for x in rows]

        return csv_filename in self.db_csv_filenames


    def _add_csv_file(self,csv_filename, csv_data):
        sql = '''insert into covid_data(filename,csv_data) values(?,?)'''
        cur = self.db.cursor()
        cur.execute(sql, (csv_filename,csv_data))
        self.db.commit()
        sys.stderr.write('add '+csv_filename+'\n')
        return cur.lastrowid
        

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


if __name__ == '__main__':
    Covid19Data()()

