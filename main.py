from gui import GUI
from api import WorldState
from extra_widgets import *

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer

import sys


class App(GUI):
    def __init__(self):
        super().__init__()
        self.ws = WorldState()
        while self.ws.ws == {}:
            self.network_error()
            sys.exit(1)
        [widget.setParent(None) for widget in [self.Fissure, self.Invasion, self.Alert, self.BaroItem, self.Event, self.NewsBlurb]]
        
        self.timers_timer = QTimer(self)
        self.timers_timer.timeout.connect(self.update_timers)
        self.timers_timer.start(1000)

        self.ws_update_timer = QTimer(self)
        self.ws_update_timer.timeout.connect(self.update_world_state)
        self.ws_update_timer.start(1000 * 60 * 5)

        self.redraw_content()

    def redraw_content(self):
        self.redraw_content_dynamic()
        self.redraw_content_static()

    def redraw_content_dynamic(self):
        self.Fissure_list = [Fissure(self.scrollAreaWidgetContents, fissure_info, fissure_i) for (fissure_i, fissure_info) in enumerate(self.ws.fissures)]
        [self.verticalLayout_6.addWidget(i) for i in self.Fissure_list]

        self.Invasion_list = [Invasion(self.scrollAreaWidgetContents_2, invasion_info, invasion_i) for (invasion_i, invasion_info) in enumerate(self.ws.invasions)]
        [self.verticalLayout_8.addWidget(i) for i in self.Invasion_list]

        self.Alert_list = [Alert(self.scrollAreaWidgetContents_3, alert_info, alert_i) for (alert_i, alert_info) in enumerate(self.ws.alerts)]
        [self.verticalLayout_16.addWidget(i) for i in self.Alert_list]

        if len(self.ws.baro_items) == 0:
            self.stackedWidget_2.setCurrentIndex(0)
        else:
            self.stackedWidget_2.setCurrentIndex(1)
            self.baro_items_list = [BaroItem(self.BaroData, item_info, item_i) for (item_i, item_info) in enumerate(self.ws.baro_items)]
            [self.gridLayout_6.addWidget(i, index // 7, index % 7, 1, 1) for (index, i) in enumerate(self.baro_items_list)]

        self.events_list = [Event(self.scrollAreaWidgetContents_4, event_info, event_i) for (event_i, event_info) in enumerate(self.ws.events)]
        [self.verticalLayout_31.addWidget(i) for i in self.events_list]

        self.newsblurb_list = [NewsBlurb(self.scrollAreaWidgetContents_5, newsblurb_info, newsblurb_i) for (newsblurb_i, newsblurb_info) in enumerate(self.ws.news)]
        [self.verticalLayout_33.addWidget(i) for i in self.newsblurb_list]

    def redraw_content_static(self):
        for i in range(1, 4):
            getattr(self, 'SortieM'+str(i)).setText(self.ws.sorties['variants'][i - 1]['missionType'])
            getattr(self, 'SortieM' + str(i) + 'Mod').setText(self.ws.sorties['variants'][i-1]['modifier'])

        self.ArchonHuntStr.setText('Archon Hunt: ' + self.ws.archon_hunt['boss'])
        for i in range(1, 4):
            getattr(self, 'ArchonHuntM' + str(i)).setText(self.ws.archon_hunt['missions'][i - 1]['type'])

        if not self.ws.arbitration:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.ArbitrationMT.setText(self.ws.arbitration['type'])
            self.ArbitrationFaction.setText(self.ws.arbitration['enemy'])

        daily_i = 1
        weekly_i = 1
        elite_i = 1
        if self.ws.nightwave:
            self.stackedWidget_3.setCurrentIndex(1)
            for challenge in self.ws.nightwave['activeChallenges']:
                if challenge.get('isDaily'):
                    challenge_type = 'Daily'
                    challenge_i = daily_i
                    daily_i += 1
                elif challenge.get('isElite'):
                    challenge_type = 'Elite'
                    challenge_i = weekly_i
                    weekly_i += 1
                else:
                    challenge_type = 'Weekly'
                    challenge_i = elite_i
                    elite_i += 1
                getattr(self, challenge_type + str(challenge_i) + 'Name').setText(challenge['title'])
                getattr(self, challenge_type + str(challenge_i) + 'Desc').setText(challenge['desc'])
        else:
            self.stackedWidget_3.setCurrentIndex(0)

    def update_timers(self):
        [i.update_timer() for i in self.Fissure_list]
        [i.update_progress() for i in self.Invasion_list]
        [i.update_timer() for i in self.Alert_list]
        [i.update_timer() for i in self.events_list]
        [i.update_timer() for i in self.newsblurb_list]

        sortie_eta = round(time.mktime(time.strptime(self.ws.sorties['expiry'], '%Y-%m-%dT%H:%M:%S.%fZ')) - time.mktime(time.gmtime()))
        if sortie_eta >= 0:
            self.SortieResetTimer.setText(f'{str(sortie_eta // 3600) + "h " if sortie_eta // 3600 > 0 else ""}{(sortie_eta // 60) % 60}m {sortie_eta % 60}s')
        else:
            self.SortieResetTimer.setText('Expired')

        weekly_eta = round(time.mktime(time.strptime('1970-1-1T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')) - time.mktime(time.gmtime()) - 3 * 86400) % (7 * 86400)
        self.WeeklyResetTimeDayStr.setText(str(weekly_eta // 86400) + 'd')
        self.WeeklyResetTimeStr.setText(f'{(weekly_eta // 3600) % 24}h {(weekly_eta // 60) % 60}m {weekly_eta % 60}s')

        bounty_eta = round(time.mktime(time.strptime('1970-1-1T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')) - time.mktime(time.gmtime()) + 120) % (9000)
        self.BountyTimeStr.setText(f'{bounty_eta // 3600}h {(bounty_eta // 60) % 60}m {bounty_eta % 60}s')

        baro_eta = round(time.mktime(time.strptime('1970-1-1T00:00:00.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')) - time.mktime(time.gmtime()) + (10*86400 + 13 * 3600)) % (14 * 86400)
        if baro_eta >= 2 * 86400:
            self.BaroStateStr.setText('Baro Arrives in:')
            baro_eta = baro_eta - 2 * 86400
        else:
            self.BaroStateStr.setText('Baro Leaves in:')
        self.BaroTimeStr.setText(f'{str(baro_eta // 86400) + "d " if baro_eta // 86400 > 0 else ""}{(baro_eta // 3600) % 24}h {(baro_eta // 60) % 60}m {baro_eta % 60}s')


    def update_world_state(self):
        if self.ws.get_ws():
            self.redraw_content()
        else:
            self.network_error()
        
    def network_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText('Network Error')
        msg.setInformativeText('Could not connect to api.warframestat.us')
        msg.setWindowTitle('Error')
        msg.exec_()


if __name__ == '__main__':
    app_handle = QApplication(sys.argv)
    app = App()
    app.show()
    app_handle.exec_()
    
