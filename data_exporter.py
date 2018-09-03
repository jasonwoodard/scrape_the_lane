import csv

# [AMS] ADD THE FOLLOWING CODE TO NAME OUTPUT FILES BASED ON DATE.
import glob2
from datetime import datetime


class DataExporter(object):

    def write_to_csv(self, header, row_objects):
        # filename = 'output.csv'
        values = self._get_rows_from_objects(row_objects)
        rows = [header]
        rows.extend(values)
        with open(datetime.now().strftime("%Y-%m-%d")+".csv", 'w') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    @staticmethod
    def _get_rows_from_objects(row_objects):
        rows = []
        for obj in row_objects:
            rows.append(obj.emit_row())
        return rows
