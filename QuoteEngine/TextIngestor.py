"""Txt Parser."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Parse Txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file in the given path."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        file_ref = open(path, "r", encoding='utf-8')
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0],
                                       parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        return quotes
