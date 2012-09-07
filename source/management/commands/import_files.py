from optparse import make_option

from django.core.management.base import BaseCommand

from source.crawler import SourceCrawler


class Command(BaseCommand):
    args = '<root>'
    help = 'Imports the specified directory of files into the database.'
    option_list = BaseCommand.option_list + (
        make_option('--identifier',
            action='store',
            dest='identifier',
            help='The identifier for the revision that is being imported.'),
        make_option('--name',
            action='store',
            dest='name',
            default=None,
            help='The name of the revision that is being imported.'),
        )

    def handle(self, root, *args, **options):
        identifier = options['identifier']
        name = options['name']

        if identifier is None:
            identifier = root

        if name is None:
            name = identifier

        crawler = SourceCrawler(root, identifier, name)
        crawler.crawl_tree()
