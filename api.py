import requests, json

class WorldState():
    def __init__(self):
        self.client = requests.Session()
        self.ws = {}
        self.get_ws()

    def get_ws(self):
        try:
            self.ws = json.loads(self.client.get('https://api.warframestat.us/pc?language=en').text)
        except requests.exceptions.ConnectionError:
            return False

        self.fissures = self.ws.get('fissures')
        self.invasions = self.ws.get('invasions')
        self.sorties = self.ws.get('sortie')
        self.archon_hunt = self.ws.get('archonHunt')
        self.arbitration = self.ws.get('arbitration')
        self.alerts = self.ws.get('alerts')
        self.baro_items = self.ws.get('voidTrader').get('inventory')
        self.nightwave = self.ws.get('nightwave')
        self.events = self.ws.get('events')
        self.news = self.ws.get('news')

        return True
