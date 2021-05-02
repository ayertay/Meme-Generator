"""Define the quote class."""


class QuoteModel():
    """Set quote a body and author."""

    def __init__(self, body, author):
        """Initialize a quote."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent a quote."""
        return f'<{self.body}, {self.author}>'
