from gui import GUI
from api import WorldState
from extra_widgets import *

from PyQt5.QtWidgets import QApplication, QMessageBox

import sys


class App(GUI):
    def __init__(self):
        super().__init__()
        self.ws = WorldState()
        while self.ws.ws == {}:
            self.network_error()
            sys.exit(1)
        del self.Fissure, self.Invasion, self.Alert, self.BaroItem, self.Event, self.NewsBlurb
        self.redraw_content()


        def redraw_content(self):
            self.redraw_content_dynamic()

        def redraw_content_dynamic(self):
            self.Fissure_list = [Fissure(self.scrollAreaWidgetContents, fissure_info, fissure_i) for (fissure_i, fissure_info) in enumerate(self.ws.fissures)]
            [self.verticalLayout_6.addWidget(i) for i in self.Fissure_list]
            self.Invasion_list = [Invasion(self.scrollAreaWidgetContents_2, invasion_info, invasion_i) for (invasion_i, invasion_info) in enumerate(self.ws.invasions)]
            [self.verticalLayout_8.addWidget(i) for i in self.Invasion_list]
            self.Alert_list = [Alert(self.scrollAreaWidgetContents_3, alerta_info, alert_i) for (alert_i, alert_info) in enumerate(self.ws.alerts)]
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
            pass
        
        
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
    
