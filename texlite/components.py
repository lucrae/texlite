import re


BACKSLASH = r'\_'[0]
BANNER_LINE = r'% ' + '-'*78


class Meta:

    def __init__(self, title=None, author=None, date=None,
                 fontsize='10pt', margin='1.6in'):

        # document details
        self.title = title # document title
        self.author = author # document author
        self.date = date # document date

        # document setup
        self.fontsize = fontsize # font size (default: 10pt)
        # extarticle fontsize options: 8, 9, 10, 11, 12, 14, 17, 20pt
        self.margin = margin # margin (default: 1.6in)

    def tex(self):

        # add meta preface
        lines = [
            r'% meta',
            f'{BACKSLASH}documentclass[{self.fontsize}]{{extarticle}}',
        ]

        # add packages
        lines += [
            r'',
            r'% packages',
            *self._packages(),
        ]

        # add optional title details
        lines += [
            r'',
            r'% document details',
            *self._document_details()
        ]

        # return joined string
        return '\n'.join(lines)

    def _packages(self):

        lines = []

        # add encoding specification
        lines.append(f'{BACKSLASH}usepackage[utf8]{{inputenc}}')

        # add margins
        lines.append(f'{BACKSLASH}usepackage[margin={self.margin}]{{geometry}}')
        
        return lines

    def _document_details(self):

        lines = []

        # add title if applicable
        if self.title:
            lines.append(f'{BACKSLASH}title{{{BACKSLASH}textbf{{{self.title}}}}}')

        # add author if applicable
        if self.author:
            lines.append(f'{BACKSLASH}author{{{self.author}}}')

        # add date, defaulting an empty (unshown) date 
        if self.date:
            lines.append(f'{BACKSLASH}date{{{self.date}}}'),
        else:
            lines.append(f'{BACKSLASH}date{{}}')

        return lines


class DocumentBegin:

    def tex(self):
        return '\n'.join([
            BANNER_LINE,
            r'\begin{document}',
            BANNER_LINE,
        ])


class DocumentEnd:

    def tex(self):
        return '\n'.join([
            BANNER_LINE,
            r'\end{document}',
            BANNER_LINE,
        ])


class MakeTitle:

    def tex(self):
        return r'\maketitle'


class Section:

    def __init__(self, content, section_type='section'):
        self.section_type = section_type
        self.content = content

    def tex(self):
        return f'{BACKSLASH}{self.section_type}{{{self.content}}}'


class Text:

    def __init__(self, content):
        self.content = content

    def tex(self):

        formatted_content = self._format_encapsulations(self.content)
        formatted_content = self._format_replacements(formatted_content)

        return formatted_content

    def _format_encapsulations(self, text):

        # format bold (**)
        for match in re.findall(r'\*\*(.*?)\*\*', text):
            text = text.replace(f'**{match}**', f'{BACKSLASH}textbf{{{match}}}')

        # format italics (*)
        for match in re.findall(r'\*(.*?)\*', text):
            text = text.replace(f'*{match}*', f'{BACKSLASH}textit{{{match}}}')

        # format code (`)
        for match in re.findall(r'`(.*?)`', text):
            text = text.replace(f'`{match}`', f'{BACKSLASH}texttt{{{match}}}')

        # format double quotes (")
        for match in re.findall(r'"(.*?)"', text):
            text = text.replace(f'"{match}"', f'``{match}"')

        return text

    def _format_replacements(self, text):

        # replace horizontal bars with medskips
        text = text.replace('---', '\medskip')

        return text
