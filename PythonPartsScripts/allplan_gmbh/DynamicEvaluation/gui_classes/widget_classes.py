"""classes for different buttons."""

from pathlib import Path

import PySide6.QtGui as PyGui
import PySide6.QtWidgets as PyWidget

from PySide6.QtCore import Qt


class TitleBar(PyWidget.QWidget):

    def __init__(self
                 , title_height: int
                 , title_text:  str):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName("title_bar")
        self.setFixedHeight(title_height)

        title_label = PyWidget.QLabel(title_text)
        title_label.setObjectName("title_label")
        title_icon = PyWidget.QLabel()
        icon_path = Path(__file__).parent / "icons" / "allplan_logo.png"
        icon_picture = PyGui.QPixmap(str(icon_path))
        title_icon.setPixmap(icon_picture)
        title_icon.resize(icon_picture.width(), icon_picture.height())

        title_bar_layout = PyWidget.QHBoxLayout()
        title_bar_layout.setContentsMargins(10, 4, 10, 4)
        title_bar_layout.setSpacing(8)
        title_bar_layout.addWidget(title_icon)
        title_bar_layout.addWidget(title_label)
        title_bar_layout.addStretch(1)   # pushes future buttons to the right

        self.setLayout(title_bar_layout)


class PushButton(PyWidget.QPushButton):

    def __init__(self
                 , button_width: int
                 , button_height: int
                 , button_text: str):
        super().__init__()
        self.setFixedSize(button_width, button_height)
        self.setText(button_text)

class InputField(PyWidget.QLineEdit):

    def __init__(self
                 , field_width:         int
                 , field_height:        int
                 , field_start_text:    str = "Material"):
        super().__init__()
        self.setFixedSize(field_width, field_height)
        self.setPlaceholderText(field_start_text)

class PullDown(PyWidget.QComboBox):

    def __init__(self
                 , combo_width: int
                 , combo_height: int
                 , combo_items: list[str]
                 , combo_edit:  bool = True):
        super().__init__()
        self.setFixedSize(combo_width, combo_height)
        self.addItems(combo_items)
        self.setEditable(combo_edit)
        if combo_edit:
            self.setDuplicatesEnabled(False)
            
class CheckBox(PyWidget.QCheckBox):

    def __init__(self
                 , box_width: int
                 , box_height: int):
        super().__init__()
        self.setFixedSize(box_width, box_height)


class HeadlineText(PyWidget.QLabel):

    def __init__(self
                 , headline_width: int
                 , headline_height: int
                 , headline_content: str = ""):
        super().__init__()
        self.setFixedSize(headline_width, headline_height)
        self.setText(headline_content)


class DataTable(PyWidget.QTableView):

    def __init__(self
                 , table_rows:      int
                 , table_columns:   int):
        super().__init__()
        self.setRowCount(table_rows)
        self.setColumnCount(table_columns)
        
class MenuAction(PyGui.QAction):

    def __init__(self
                 , action_parent:   PyWidget.QWidget
                 , action_text:     str
                 , action_tip:      str = ""
                 , action_check:    bool = False):
        super().__init__()
        self.action_parent = action_parent
        self.action_text = action_text
        self.action_tip = action_tip
        self.action_check = action_check
        self.setParent(action_parent)
        self.setText(action_text)
        self.setToolTip(action_tip)
        self.setCheckable(action_check)
