import csv

from datetime import datetime


class DataExporter(object):

    def __init__(self):
        self.file_prefix = ''

    def write_to_csv(self, header, row_objects):
        values = self._get_rows_from_objects(row_objects)
        rows = [header]
        rows.extend(values)
        with open(self._get_file_name(), 'w') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    @staticmethod
    def _get_rows_from_objects(row_objects):
        rows = []
        for obj in row_objects:
            rows.append(obj.emit_row())
        return rows

    def _get_file_name(self):
        return '{0}{1:%Y-%m-%d}.csv'.format(self.file_prefix, datetime.now())
