from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        result = ''
        for header in headers:
            result += f'<th>{header}</th>'
        print('<tr>' + result + '</tr>')

    def row(self, rowdata):
        result = ''
        for data in rowdata:
            result += f'<td>{data}</td>'
        print('<tr>' + result + '</tr>')

