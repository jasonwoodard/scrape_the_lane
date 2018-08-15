import pystache


class DataExporter(object):
    def __init__(self):
        pass

    def export_to_csv(self, template, players):
        print pystache.render(template, players)
