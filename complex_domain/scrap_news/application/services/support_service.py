

from complex_domain.scrap_news.infra.services.package_manager import PackageManager


class DependencesManager():

    def install_dependences(self):
        PackageManager.install('bs4')
        PackageManager.install('peewee')