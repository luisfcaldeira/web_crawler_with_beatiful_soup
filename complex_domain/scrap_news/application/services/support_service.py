

from complex_domain.scrap_news.infra.services.package_manager import PackageManager


class DependencesManager():

    def install_dependences(self):
        PackageManager.install('bs4')
        PackageManager.install('peewee')
        PackageManager.install('numpy')
        PackageManager.install('pandas')
        PackageManager.install('openpyxl')

    def install_pandas(self):
        PackageManager.install('pandas')
