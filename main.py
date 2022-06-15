# https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/#:~:text=Use%20the%20a%20tag%20to,passing%20title%20argument%20to%20it.
import os
from complex_domain.scrap_news.application.services.support_service import DependencesManager
from complex_domain.scrap_news.application.services.scraper_app_service import ScrapAppService
from complex_domain.scrap_news.application.services.urls_app_service import UrlsAppService
from complex_domain.scrap_news.application.services.urls_targets_app_service import UrlsTargetsAppService


first_execution = True
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if first_execution:
        print('======================= Web Scrapper ==========================')
        first_execution = False

    print(" 1 - scrap!\n 2 - list of urls\n 3 - insert new url\n 4 - for dependence installation\n Or just type 'exit' or '0' for application ends up execution")
    typed = input()

    if typed.lower == 'exit' or typed == "0":
        break

    if typed == '1':
        scrap = ScrapAppService()
        print('running...')
        scrap.run()
        
    elif typed == '2':
        urls_targets_app_service = UrlsTargetsAppService()
        urls_app_service = UrlsAppService()
        print('Targets: \n')
        targets = urls_targets_app_service.get_all_str_domain()
        if len(targets) == 0:
            print("none")

        for target in targets:
            print(target.domain)
        
        print('----------------------------------------------------')
        print('Urls discovered:\n')
        urls = urls_app_service.get_urls()
        if len(urls) == 0:
            print("none")

        for url in urls:
            print(url.url_str, ' - ignored: ', url.ignored)
        print('----------------------------------------------------')

    elif typed == '3':
        print('Write the url below:')
        url = input()

        urls_targets_app_service = UrlsTargetsAppService()
        try:
            urls_targets_app_service.add_new_target(url)
        except Exception as e:
            print(f"It was not possible to insert URL due a error.\n :{e}")
    
    elif typed == '4':
        manager = DependencesManager()
        manager.install_dependences()

    input("Press ENTER to continue...")