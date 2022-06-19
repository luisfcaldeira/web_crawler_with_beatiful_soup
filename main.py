import os
from complex_domain.scrap_news.application.services.domain_app_service import DomainAppService
from complex_domain.scrap_news.application.services.exceptions.exceptions import UrlNotFoundException
from complex_domain.scrap_news.application.services.support_service import DependencesManager
from complex_domain.scrap_news.application.services.scraper_app_service import ScrapAppService
from complex_domain.scrap_news.application.services.urls_app_service import UrlsAppService
from complex_domain.scrap_news.application.services.urls_targets_app_service import UrlsTargetsAppService
from complex_domain.scrap_news.infra.data.repositories.entities_repositories import IgnoredDomainRepositoryImpl, TargetsUrlRepositoryImpl, UrlRepositoryImpl
from complex_domain.scrap_news.infra.services.terminal_services import ConsoleLogger


first_execution = True
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if first_execution:
        print('======================= Web Scrapper ==========================')
        first_execution = False

    print(" 1 - scrap!\n 2 - list of urls\n 3 - insert new url\n 4 - ignore domain\n 5 - install dependences \n Or just type 'exit' or '0' for application ends up execution")
    typed = input()

    if typed.lower == 'exit' or typed == "0":
        break

    if typed == '1':
        scrap = ScrapAppService(UrlRepositoryImpl(), TargetsUrlRepositoryImpl(), ConsoleLogger(), IgnoredDomainRepositoryImpl())
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
        print("Write the domain below:")
        url = input()
        domain_app_service = DomainAppService(IgnoredDomainRepositoryImpl())

        try:
            domain_app_service.ignore_domain(url)
        except UrlNotFoundException as e:
            print(e)

    elif typed == '5':
        manager = DependencesManager()
        manager.install_dependences()        

    input("Press ENTER to continue...")