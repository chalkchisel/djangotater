import os

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from django.db.utils import DatabaseError

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

    def valid_file(self, filename):
        tests = [
            lambda x: x.startswith('.'),
            lambda x: x.endswith('.pyc'),
            lambda x: x.endswith('.mo'),
            lambda x: x.endswith('.gif'),
            lambda x: x.endswith('.png'),
        ]

        for test in tests:
            if test(filename):
                return False

        return True

    def import_files(self, path, filenames):
        for filename in filenames:
            if not self.valid_file(filename):
                continue
            full_path = os.path.join(path, filename)
            with open(full_path, 'r') as f:
                body = f.read()
            html = highlight(body, PythonLexer(), HtmlFormatter())
            try:
                SourceFile.objects.create(**{
                    'version': self.version,
                    'path': path,
                    'file_name': filename,
                    'body': body,
                    'rendered': html,
                    })
            except DatabaseError:
                continue

    def crawl_tree(self):
        directories = os.walk(self.root)
        for directory in directories:
            path = directory[0]
            filenames = directory[2]
            self.import_files(path, filenames)
