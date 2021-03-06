from ..source import URLSource
from ..package import Package
from ..util import target_arch


class SQLite(Package):
    @property
    def source(self):
        _vernum = list(map(int, self.version.split('.')))
        return URLSource(f'https://www.sqlite.org/2019/sqlite-autoconf-{_vernum[0] * 10000 + _vernum[1] * 100 + _vernum[2]}00.tar.gz')

    def build(self):
        self.run_with_env([
            './configure',
            '--prefix=/usr',
            '--host=' + target_arch().ANDROID_TARGET,
            '--disable-shared',
        ])

        self.run(['make'])
        self.run(['make', 'install', f'DESTDIR={self.destdir()}'])
