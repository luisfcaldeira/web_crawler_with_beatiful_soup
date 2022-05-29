# https://www.geeksforgeeks.org/beautifulsoup-scraping-link-from-html/#:~:text=Use%20the%20a%20tag%20to,passing%20title%20argument%20to%20it.

from application.services.scraper_app_service import ScrapAppService
from application.services.support_service import DependencesManager
from domain.entities.urls import Url
from infra.services.package_manager import PackageManager

manager = DependencesManager()
manager.install_dependences()

scrap = ScrapAppService()
url = Url("https://www1.folha.uol.com.br/poder/2022/05/bolsonaro-dobra-numero-de-viagens-em-2022-e-acumula-eventos-com-perfil-eleitoral.shtml")
scrap.run(url)

'''

    Criar application service para retornar urls 
    Regra para preparar URL para analise 
    Regra para avaliar se o URL deve ser analisada novamente 

'''