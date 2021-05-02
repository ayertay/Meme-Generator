"""PDF Parser."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Parse PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file in the given path."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./{random.randint(0,1000000)}.txt'
        subprocess.call(['pdftotext', '-raw', path, tmp])

        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0].strip('"'),
                                       parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return quotes
