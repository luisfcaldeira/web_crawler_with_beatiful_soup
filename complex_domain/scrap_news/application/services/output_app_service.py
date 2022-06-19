
import pandas as pd
from complex_domain.scrap_news.domain.dal.repositories.entities_repositories import ArticlesRepository
import os
import inspect

class OutputAppService():

    def __init__(self, articles_repository: ArticlesRepository) -> None:
        if not isinstance(articles_repository, ArticlesRepository):
            raise Exception("Make sure you are passing the right types thorough parameters.")

        self.__articles_repository = articles_repository

    def save_xlsx(self, path=None):

        if path == None or path == '':
            print('using default path.')
            abs_path = os.path.abspath((inspect.stack()[1])[1])
            path = os.path.dirname(abs_path)

        path = f'{path}/articles.xlsx'

        print('depending on information\'s size, this proccess can take a long. Please, be patient')
        print('data is being taken from database')
        articles = self.__articles_repository.get_all_join_url()
        counter = 0
        xlsx_line = []
        print('loading data in memory')
        for article in articles:
            counter += 1
            xlsx_line.append(article.to_dict())
        
        print(f'\nsaving {counter} records in the file: "{path}"...')

        df_articles = pd.DataFrame(xlsx_line)
        df_articles.to_excel(path)

        print('done.')
