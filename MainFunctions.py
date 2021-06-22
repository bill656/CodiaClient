from datetime import datetime, timedelta
from re import search

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QListWidget
from PyQt5.QtWidgets import QMessageBox

import functionWindow
from codiaclientgui.utils import Font, Palette
from codiaclient.network import get_pack, show_pack

pages = 0


def functionWindow_init(ui: functionWindow.Ui_functionWindow, nickname="UNDEFINED", verified=True):
    global pages
    pack_list = get_pack()
    ui.exerciseFrame.hide()
    ui.packFrame.show()
    if verified:
        status_bar_label = QLabel("当前用户: {}".format(nickname))
    else:
        status_bar_label = QLabel("当前用户: {}(未验证)".format(nickname))
        QMessageBox.information(None, "消息", "当前账号功能受限，请尽快完成联系方式验证。", QMessageBox.Ok)
    status_bar_label.setFont(Font["status"])
    ui.statusbar.addWidget(status_bar_label)
    for dic in pack_list:
        add_item_to_pack_list(ui.listWidget_packs, dic)
    pages = 1
    ui.pushButton_last.setEnabled(False)
    ui.pushButton_next.clicked.connect(nextPage)
    ui.pushButton_last.clicked.connect(lastPage)


def nextPage():
    pass


def lastPage():
    global pages
    pages -= 1


def get_pack_widget(data: dict):
    widget = QWidget()
    layout_main = QHBoxLayout()
    layout_right = QVBoxLayout()
    layout_right_up = QHBoxLayout()
    layout_right_down = QHBoxLayout()
    if data["codingExercises"]:
        total = data["codingExercises"]["totalCount"]
        has_done = data["codingExercises"]["viewerPassedCount"]
        if total == has_done:
            label_finish = QLabel("已完成")
            label_finish.setPalette(Palette["green"])
        else:
            label_finish = QLabel("未完成")
            label_finish.setPalette(Palette["red"])
        label_has_done_total = QLabel("已完成/总计: {}/{}".format(has_done, total))
        if data["due"]:
            end = (datetime.strptime(search(r"^[^.]*", data["due"].replace("T", " ")).group(), "%Y-%m-%d %H:%M:%S")
                   + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            end = "无限制"

        if data["createdAt"]:
            start = (datetime.strptime(search(r"^[^.]*", data["createdAt"].replace("T", " ")).group(),
                                       "%Y-%m-%d %H:%M:%S")
                     + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            start = "无限制"
    else:
        end = ""
        start = ""
        label_finish = QLabel("无权限")
        label_finish.setPalette(Palette["gray"])
        label_has_done_total = QLabel("")
        widget.setEnabled(False)

    label_name = QLabel(data["name"])
    label_start = QLabel("开始时间")
    label_end = QLabel("截止时间")
    label_start_time = QLabel(start)
    label_end_time = QLabel(end)

    layout_right_up.addWidget(label_name)
    layout_right_up.addWidget(label_start)
    layout_right_up.addWidget(label_end)
    layout_right_up.setStretchFactor(label_name, 4)
    layout_right_up.setStretchFactor(label_start, 4)
    layout_right_up.setStretchFactor(label_end, 4)

    layout_right_down.addWidget(label_has_done_total)
    layout_right_down.addWidget(label_start_time)
    layout_right_down.addWidget(label_end_time)
    layout_right_down.setStretchFactor(label_has_done_total, 4)
    layout_right_down.setStretchFactor(label_start_time, 4)
    layout_right_down.setStretchFactor(label_end_time, 4)

    layout_right.addLayout(layout_right_up)
    layout_right.addLayout(layout_right_down)
    layout_right.setStretchFactor(layout_right_up, 12)
    layout_right.setStretchFactor(layout_right_down, 12)

    layout_main.addWidget(label_finish)
    layout_main.addLayout(layout_right)
    layout_main.setStretchFactor(label_finish, 1)
    layout_main.setStretchFactor(layout_right, 12)

    widget.setLayout(layout_main)
    return widget


def add_item_to_pack_list(pack_list: QListWidget, data: dict):
    item = QListWidgetItem()
    item.setSizeHint(QSize(651, 68))
    widget = get_pack_widget(data)
    pack_list.addItem(item)
    pack_list.setItemWidget(item, widget)