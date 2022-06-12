# https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/#:~:text=Use%20the%20a%20tag%20to,passing%20title%20argument%20to%20it.
import os
from complex_domain.scrap_news.application.services.support_service import DependencesManager
from complex_domain.scrap_news.application.services.scraper_app_service import ScrapAppService
from complex_domain.scrap_news.application.services.urls_targets_app_service import UrlsTargetsAppService

manager = DependencesManager()
manager.install_dependences()



'''

    Criar application service para retornar urls 
    Regra para preparar URL para analise 
    Regra para avaliar se o URL deve ser analisada novamente 

'''

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" 1 - insert new url\n 2 - list of urls\n 3 - scrap urls\n Or just type 'exit' for application ends up execution")
    typed = input()

    if typed == 'exit':
        break

    if typed == '1':
        print('Write the url below:')
        url = input()

        urls_targets_app_service = UrlsTargetsAppService()
        try:
            urls_targets_app_service.add_new_target(url)
        except Exception as e:
            print(f"It was not possible to insert URL due a error.\n :{e}")

    elif typed == '2':
        urls_targets_app_service = UrlsTargetsAppService()
        print(urls_targets_app_service.get_all())

    elif typed == '3':
        scrap = ScrapAppService()
        print('running...')
        scrap.run()

    input("Press ENTER to continue...")