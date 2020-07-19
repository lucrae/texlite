import re


BANNER_LINE = r'% ' + '-'*78


class Meta:

    def __init__(self, title=None, author=None, date=None, margin='1.6in'):
        
        # document details
        self.title = title
        self.author = author
        self.date = date

        # document setup
        self.margin = margin

    def tex(self):

        # add meta preface
        lines = [
            r'% meta',
            r'\documentclass{article}',
        ]

        # add packages
        lines += [
            r'',
            r'% packages',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage' + f'[margin={self.margin}]' + r'{geometry}',
        ]

        # add optional title details
        lines += [
            r'',
            r'% document details',
        ]
        if self.title:
            lines.append(r'\title' + f'{{{self.title}}}')
        if self.author:
            lines.append(r'\author' + f'{{{self.author}}}')
        if self.date:
            lines.append(r'\date' + f'{{{self.date}}}'),
        else:
            lines.append(r'\date{}')

        # return joined string
        return '\n'.join(lines)


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
        return f'\{self.section_type}{{{self.content}}}'


class Text:

    def __init__(self, content):
        self.content = content

    def tex(self):

        # format content
        return self._format_encapsulations(self.content)

    def _format_encapsulations(self, text):

        # format bold
        for match in re.findall('\*\*(.*?)\*\*', text):
            text = text.replace(f'**{match}**', r'\textbf' + f'{{{match}}}')

        # format italics
        for match in re.findall('\*(.*?)\*', text):
            text = text.replace(f'*{match}*', r'\textit' + f'{{{match}}}')

        # format code
        for match in re.findall('`(.*?)`', text):
            text = text.replace(f'`{match}`', r'\texttt' + f'{{{match}}}')

        return text