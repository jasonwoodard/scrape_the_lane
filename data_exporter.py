import pystache


class DataExporter(object):

    # Rows pystache template. Braces are doubled so they remain literal
    # when string.format() is used.
    RowsTemplate = '''
        {{{{#rows}}}}{0}{{{{/rows}}}}
    '''

    def convert_to_csv(self, template, header, row_array):
        # Put the row array into a row's dictionary
        rows = {'rows': row_array}

        # Get the rows template
        row_template = header + DataExporter.RowsTemplate.format(template)
        return pystache.render(row_template, rows)
