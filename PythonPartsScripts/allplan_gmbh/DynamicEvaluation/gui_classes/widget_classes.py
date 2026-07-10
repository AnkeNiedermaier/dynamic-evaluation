"""classes for different buttons."""

from pathlib import Path

import PySide6.QtGui as PyGui
import PySide6.QtWidgets as PyWidget

from PySide6.QtCore import Qt


#----------------- Different widget classes for the GUI window
#----------------- title bar widget
class TitleBar(PyWidget.QWidget):

    """ Definition of class TitleBar which is
        the custom title bar for the application window
    """

    def __init__(self
                 , title_height: int
                 , title_text:  str):

        """ Class for the title bar of the GUI window

        Args:
            title_height: the height of the title bar
            title_text: the app title

        """
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

#----------------- push button widget
class PushButton(PyWidget.QPushButton):

    """ Definition of class PushButton for
        buttons inside the GUI window
    """

    def __init__(self
                 , button_width: int
                 , button_height: int
                 , button_text: str):
        """ Class for the push buttons of the GUI window

        Args:
            button_width: the width of the button
            button_height: the height of the button
            button_text: the text on the button

        """
        super().__init__()
        self.setFixedSize(button_width, button_height)
        self.setText(button_text)

#----------------- input field widget
class InputField(PyWidget.QLineEdit):

    """ Definition of class InputField for
        input fields inside the GUI window
    """

    def __init__(self
                 , field_width:         int
                 , field_height:        int
                 , field_start_text:    str = "Material"):

        """ Class for the input fields of the GUI window

        Args:
            field_width: the width of the input field
            field_height: the height of the input field
            field_start_text: the placeholder text in the input field

        """

        super().__init__()
        self.setFixedSize(field_width, field_height)
        self.setPlaceholderText(field_start_text)

#----------------- pull down widget
class PullDown(PyWidget.QComboBox):

    """ Definition of class PullDown for
        pull down menus inside the GUI window
    """

    def __init__(self
                 , combo_width: int
                 , combo_height: int
                 , combo_items: list[str]
                 , combo_edit:  bool = True):

        """ Class for the pull down menus of the GUI window

        Args:
            combo_width: the width of the pull down menu
            combo_height: the height of the pull down menu
            combo_items: the list of items in the pull down menu
            combo_edit: whether the pull down menu is editable

        """
        super().__init__()
        self.setFixedSize(combo_width, combo_height)
        self.addItems(combo_items)
        self.setEditable(combo_edit)
        if combo_edit:
            self.setDuplicatesEnabled(False)

#----------------- check box widget
class CheckBox(PyWidget.QCheckBox):

    """ Definition of class CheckBox for
        check boxes inside the GUI window
    """
    def __init__(self
                 , box_width: int
                 , box_height: int):

        """ Class for the check boxes of the GUI window

        Args:
            box_width: the width of the check box
            box_height: the height of the check box

        """

        super().__init__()
        self.setFixedSize(box_width, box_height)

#----------------- label widget
class HeadlineText(PyWidget.QLabel):

    """ Definition of class HeadlineText for
        labels with fixed content inside the GUI window
    """

    def __init__(self
                 , headline_width: int
                 , headline_height: int
                 , headline_content: str = ""):

        """ Class for the labels of the GUI window

        Args:
            headline_width: the width of the label
            headline_height: the height of the label
            headline_content: the text on the label

        """

        super().__init__()
        self.setFixedSize(headline_width, headline_height)
        self.setText(headline_content)

#----------------- table view widget
class DataTable(PyWidget.QTableView):

    """ Definition of class DataTable for the table view
        based on and derived from the table model inside the GUI window
    """

    def __init__(self
                 , table_rows:      int
                 , table_columns:   int):
        """ Class for the table view of the GUI window

        Args:
            table_rows: the number of rows in the table
            table_columns: the number of columns in the table

        """

        super().__init__()
        self.setRowCount(table_rows)
        self.setColumnCount(table_columns)

#----------------- menu action widget
class MenuAction(PyGui.QAction):

    """ Definition of class MenuAction for a combined functionality
        of actions assignment to menu items in the GUI window
    """

    def __init__(self
                 , action_parent:   PyWidget.QWidget
                 , action_text:     str
                 , action_tip:      str = ""
                 , action_check:    bool = False):
        """ Class for the menu actions of the GUI window

        Args:
            action_parent: the parent widget of the action
            action_text: the text of the action
            action_tip: the tooltip of the action
            action_check: whether the action is checkable

        """

        super().__init__()
        self.action_parent = action_parent
        self.action_text = action_text
        self.action_tip = action_tip
        self.action_check = action_check
        self.setParent(action_parent)
        self.setText(action_text)
        self.setToolTip(action_tip)
        self.setCheckable(action_check)
