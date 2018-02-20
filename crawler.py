import argparse

from db.db import CrawlerDb
from parser.parser import Parser


class Crawler:
    def __init__(self):
        self.db = CrawlerDb()
        self.parser = Parser()

    def parse_sitemap(self):
        sites = self.db.get_sites()
        for site in sites:
            urls = self.parser.get_all_links_from_sitemap(site["name"])
            self.db.add_pages(site["id"], urls)

    def parse_pages(self):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Crawler for GB internship", usage="%(prog)s [options]")
    parser.add_argument("-s", "--sitemap", action="store_true", dest="sitemap", help="Parse sitemap")
    parser.add_argument("-p", "--pages", action="store_true", dest="pages", help="Check unparsed URL")

    args = parser.parse_args()

    if not args.sitemap and not args.pages:
        parser.error("Set option sitemap or pages")

    crawler = Crawler()

    if args.sitemap:
        crawler.parse_sitemap()

    if args.pages:
        crawler.parse_pages()
