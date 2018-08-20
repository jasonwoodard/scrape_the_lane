import pystache
import csv


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

    def write_to_csv(self, header, row_objects):
        filename = 'output.csv'
        values = self._get_rows_from_objects(row_objects)
        rows = [header]
        rows.extend(values)
        with open(filename, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    @staticmethod
    def _get_rows_from_objects(row_objects):
        rows = []
        for obj in row_objects:
            rows.append(obj.emit_row())
        return rows
