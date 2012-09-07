import os

from .models import Version, SourceFile


class CrawlError(Exception):
    pass


class SourceCrawler(object):
    def __init__(self, root, identifier, name):
        self.root = root
        self.identifier = identifier
        self.name = name

        version, created = Version.objects.get_or_create(
            identifier=identifier, defaults={'name': name})

        if not created:
            error_message = \
                'A Version with identifier {} named {} already exists.'
            raise CrawlError(error_message.format(version.identifier,
                version.name))

        self.version = version

    def import_files(self, path, filenames):
        for filename in filenames:
            if filename.startswith('.') or filename.endswith('.pyc'):
                continue
            full_path = os.path.join(path, filename)
            with open(full_path, 'r') as f:
                body = f.read()
            SourceFile.objects.create(**{
                'version': self.version,
                'path': path,
                'file_name': filename,
                'body': body,
                })

    def crawl_tree(self):
        directories = os.walk(self.root)
        for directory in directories:
            path = directory[0]
            filenames = directory[2]
            self.import_files(path, filenames)
