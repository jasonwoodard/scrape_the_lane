import pystache


class DataExporter:
    def __init__(self):
        self.templates ={}

    def export_to_csv(self, template, players):
        print pystache.render(template, players)
