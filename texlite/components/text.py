import re

from texlite.components.common import (
    BACKSLASH, NON_ENCAPSULATION_CHARS,
    ITALICS_RE, BOLD_RE, CODE_RE, QUOTES_RE, HYPERLINK_RE
)


class Text:
    '''Represents standard auto-formatted text'''

    def __init__(self, content: str):
        self.content = content

    def tex(self) -> str:
        '''Returns generated TeX from component'''

        # flow through formatting pipes
        formatted_content = self._format_encapsulations(self.content)
        formatted_content = self._format_replacements(formatted_content)
        formatted_content = self._format_hyperlinks(formatted_content)
        formatted_content = self._format_special_characters(formatted_content)

        return formatted_content

    def _is_encapsulatable(self, text,
                           bad_chars=NON_ENCAPSULATION_CHARS) -> bool:

        if len(text) == 0:
            return False

        # return if head and tail chars are acceptable for encapsulation
        return not text[0] in bad_chars and not text[-1] in bad_chars

    def _format_encapsulations(self, text: str) -> str:

        # format bold (**)
        for match in re.findall(BOLD_RE, text):
            if self._is_encapsulatable(match):
                text = text.replace(f'**{match}**',
                                    f'{BACKSLASH}textbf{{{match}}}')

        # format italics (*)
        for match in re.findall(ITALICS_RE, text):

            if self._is_encapsulatable(match):
                text = text.replace(f'*{match}*',
                                    f'{BACKSLASH}textit{{{match}}}')

        # format code (`)
        for match in re.findall(CODE_RE, text):
            if self._is_encapsulatable(match):
                text = text.replace(f'`{match}`',
                                    f'{BACKSLASH}texttt{{{match}}}')

        # format double quotes (")
        for match in re.findall(QUOTES_RE, text):
            if self._is_encapsulatable(text):
                text = text.replace(f'"{match}"', f'``{match}"')

        return text

    def _format_replacements(self, text: str) -> str:

        # replace horizontal bars with medskips
        if text == '---':
            return r'\medskip'

        return text

    def _format_hyperlinks(self, text: str) -> str:

        # format hyperlinks
        for m in re.finditer(HYPERLINK_RE, text):

            # get href info
            link_text = m.group(1)
            link_url = m.group(2)

            # form href and replace in text
            href = f'{BACKSLASH}href{{{link_url}}}{{{Text(link_text).tex()}}}'
            text = text.replace(f'[{link_text}]({link_url})', href)

        return text

    def _format_special_characters(self, text: str) -> str:

        # replace special characters with safe (backslashed) ones
        text = text.replace('&', r'\&')

        return text
