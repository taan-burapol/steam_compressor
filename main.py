import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtUiTools import QUiLoader


def load_ui_file(ui_file):
    loader = QUiLoader()
    ui = loader.load(ui_file)
    return ui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Qt Designer UI Example")

        # Load the UI file
        ui_file = "main.ui"
        ui = load_ui_file(ui_file)

        # Set the UI as the central widget
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(ui)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set the window size based on the size defined in the UI
        self.setGeometry(ui.geometry())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the main window
    main_window = MainWindow()
    main_window.show()

    # Run the application
    sys.exit(app.exec())
