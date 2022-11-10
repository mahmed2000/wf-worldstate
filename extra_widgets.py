from PyQt5 import QtWidgets, QtGui, QtCore

from datetime import datetime, timedelta

class Fissure(QtWidgets.QWidget):
    def __init__(self, parent, fissure_info, i):
        super().__init__(parent)
        self.i = str(i)
        self.fissure_info = fissure_info
        self.create_gui()
        self.update_gui()


    def create_gui(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setObjectName("Fissure_" + self.i)
        self.gridLayout_3 = QtWidgets.QGridLayout(self)
        self.gridLayout_3.setObjectName("gridLayout_3_" + self.i)
        self.FissureTier = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FissureTier.setFont(font)
        self.FissureTier.setObjectName("FissureTier_" + self.i)
        self.gridLayout_3.addWidget(self.FissureTier, 0, 0, 1, 1)
        self.FissureTimer = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FissureTimer.setFont(font)
        self.FissureTimer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FissureTimer.setObjectName("FissureTimer_" + self.i)
        self.gridLayout_3.addWidget(self.FissureTimer, 0, 1, 1, 1)
        self.FissureNode = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FissureNode.setFont(font)
        self.FissureNode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.FissureNode.setObjectName("FissureNode_" + self.i)
        self.gridLayout_3.addWidget(self.FissureNode, 1, 0, 1, 1)
        self.FissureType = QtWidgets.QLabel(Fissure)
        self.FissureType.setAlignment(QtCore.Qt.AlignCenter)
        self.FissureType.setObjectName("FissureType_" + self.i)
        self.gridLayout_3.addWidget(self.FissureType, 1, 1, 1, 1)

    def update_gui(self):
        self.FissureTier.setText(f"{self.fissure_info['tier']} - T{self.fissure_info['tierNum']}")
        self.update_timer(self)
        self.FissureNode.setText(f"{self.fissure_info['node']}")
        self.FissureType.setText(f"{'Steel Path' if self.fissure_info['isHard'] else ('Storm' if self.fissure_info['isStorm'] else '')}")

    def udpdate_timer(self):
        eta = datetime.strptime(self.fissure_info['expiry'], '%Y-%m-%dT%H:%M:%SZ') - datetime.now()
        eta -= timedelta(microseconds=eta.microseconds)

        self.FissureTimer.setText(f"{eta.seconds // 3600}h {(eta.seconds // 60) % 60}m {eta.seconds % 60}s")


class Invasion(QtWidgets.QWidget):
    def __init__(self, parent, invasion_info, i):
        super().__init__(parent)
        self.i = str(i)
        self.invasion_info = invasion_info
        self.create_gui()
        self.update_gui()

    def create_gui(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setObjectName("Invasion_" + self.i)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Invasion)
        self.gridLayout_4.setObjectName("gridLayout_4_" + self.i)
        self.Reward2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Reward2.setFont(font)
        self.Reward2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Reward2.setWordWrap(True)
        self.Reward2.setObjectName("Reward2_" + self.i)
        self.gridLayout_4.addWidget(self.Reward2, 0, 1, 1, 1)
        self.InvasionProgress = QtWidgets.QProgressBar(self)
        self.InvasionProgress.setStyleSheet("QProgressBar {background-color:red;;border-color:red; border:0px}\n"
"QProgressBar::chunk {background-color:blue;}")
        self.InvasionProgress.setProperty("value", 24)
        self.InvasionProgress.setTextVisible(False)
        self.InvasionProgress.setObjectName("InvasionProgress_" + self.i)
        self.gridLayout_4.addWidget(self.InvasionProgress, 1, 0, 1, 2)
        self.Reward1 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Reward1.setFont(font)
        self.Reward1.setWordWrap(True)
        self.Reward1.setObjectName("Reward1_" + self.i)
        self.gridLayout_4.addWidget(self.Reward1, 0, 0, 1, 1)

    def update_gui(self):
        faction_colors = {'Gineer': 'red', 'Corpus': 'blue', 'Infested': 'green'}
        self.Reward1.setText(f"{self.invasion_info['attackerReward']['itemString']}")
        self.Reward2.setText(f"{self.invasion_info['defenderReward']['itemString']}")
        self.InvasionProgress.setStyleSheet(f'QProgressBar {{background-color:{faction_colors.get(self.invasion_info["defendingFaction"])};border-color:red; border:0px}}\nQProgressBar::chunk {{background-color:{faction_colors.get(self.invasion_info["attackingFaction"])};}}')

    def update_progress(self):
        self.InvasionProgress.setProperty('value', self.invasion_info['completion'])

class Alert(QtWidgets.QWidget):
    def __init__(self, parent, alert_info, i):
        super().__init__(parent)
        self.i = str(i)
        self.alert_info = alert_info
        self.create_gui()
        self.update_gui()

    def create_gui(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setObjectName("Alert_" + self.i)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.AlertReward = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.AlertReward.setFont(font)
        self.AlertReward.setWordWrap(True)
        self.AlertReward.setObjectName("AlertReward_" + self.i)
        self.horizontalLayout_6.addWidget(self.AlertReward)
        self.AlertTimer = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AlertTimer.setFont(font)
        self.AlertTimer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AlertTimer.setObjectName("AlertTimer_" + self.i)
        self.horizontalLayout_6.addWidget(self.AlertTimer)

    def update_gui(self):
        self.AlertReward.setText(self.alert_info['mission']['reward']['itemString'])
        self.update_timer()

    def update_timer(self):
        eta = datetime.strptime(self.alert_info['expiry'], '%Y-%m-%dT%H:%M:%SZ') - datetime.now()
        eta -= deltatime(microseconds=eta.microseconds)
        self.AlertTimer.setText(f'{eta.days}d {eta.seconds // 3600}h {(eta.seconds // 60) % 60}m {eta.seconds % 60}s')

class BaroItem(QtWidgets.QWidget):
    def __init__(self, parent, item_info, i):
        super().__init__(parent)
        self.item_info = item_info
        self.i = str(i)
        self.create_gui()
        self.update_gui()

    def create_gui(self):
        self.setMaximumSize(QtCore.QSize(250, 250))
        self.setObjectName("BaroItem_" + self.i)
        self.gridLayout_7 = QtWidgets.QGridLayout(self)
        self.gridLayout_7.setObjectName("gridLayout_7_" + self.i)
        self.ItemName = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ItemName.setFont(font)
        self.ItemName.setAlignment(QtCore.Qt.AlignCenter)
        self.ItemName.setObjectName("ItemName_" + self.i)
        self.gridLayout_7.addWidget(self.ItemName, 0, 0, 1, 1)

    def update_gui(self):
        self.ItemName.setText(self.item_info['item'])

class Event(QtWidgets.QWidget):
    def __init__(self, parent, event_info, i):
        super().__init__(parent)
        self.event_info = event_info
        self.i = str(i)
        self.create_gui()
        self.update_gui()

    def create_gui(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setObjectName("Event_" + self.i)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11_" + self.i)
        self.EventName = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EventName.setFont(font)
        self.EventName.setObjectName("EventName_" + self.i)
        self.horizontalLayout_11.addWidget(self.EventName)
        self.EventTimer = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EventTimer.setFont(font)
        self.EventTimer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EventTimer.setObjectName("EventTimer_" + self.i)
        self.horizontalLayout_11.addWidget(self.EventTimer)

    def update_gui(self):
        self.EventName.setText(self.event_info['description'])
        self.update_timer()

    def update_timer(self):
        eta = datetime.strptime(self.event_info['expiry'], '%Y-%m-%dT%H:%M:%SZ') - datetime.now()
        eta -= deltatime(microseconds=eta.microseconds)
        self.EventTimer.setText(f'{eta.days}d {eta.seconds // 3600}h {(eta.seconds // 60) % 60}m {eta.seconds % 60}s')

class NewsBlurb(QtWidgets.QWidget):
    def __init__(self, parent, news_info, i):
        super().__init__(parent)
        self.i = str(i)
        self.news_info = news_info
        self.create_gui()
        self.update_gui()

    def create_gui(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setObjectName("NewsBlurb_" + self.i)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12_" + self.i)
        self.NewsBlurbHyperLink = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewsBlurbHyperLink.sizePolicy().hasHeightForWidth())
        self.NewsBlurbHyperLink.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.NewsBlurbHyperLink.setFont(font)
        self.NewsBlurbHyperLink.setWordWrap(True)
        self.NewsBlurbHyperLink.setOpenExternalLinks(True)
        self.NewsBlurbHyperLink.setObjectName("NewsBlurbHyperLink")
        self.horizontalLayout_12.addWidget(self.NewsBlurbHyperLink)
        self.NewsBlurbRelTimer = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewsBlurbRelTimer.sizePolicy().hasHeightForWidth())
        self.NewsBlurbRelTimer.setSizePolicy(sizePolicy)
        self.NewsBlurbRelTimer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NewsBlurbRelTimer.setObjectName("NewsBlurbRelTimer")
        self.horizontalLayout_12.addWidget(self.NewsBlurbRelTimer)

    def update_gui(self):
        self.NewsBlurbHyperLink.setText(f'<a href=\"{self.news_info["link"]}\">{self.news_info["message"]}</a>')
        self.update_timer()

    def update_timer(self):
        eta = datetime.strptime(self.news_info['expiry'], '%Y-%m-%dT%H:%M:%SZ') - datetime.now()
        eta -= deltatime(microseconds=eta.microseconds)
        if abs(eta.days) >= 1:
            self.NewsBlurbRelTimer.setText(f'{"Starts in " if eta.days > 0 else ""}{abs(eta.days)}')
        else:
            self.NewsBlurbRelTimer.setText(f'{"Starts in " if eta.seconds > 0 else ""}{abs(eta.seconds) // 3600}h {(abs(eta.seconds) // 60) % 60}m')

