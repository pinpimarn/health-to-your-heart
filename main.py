"""File to launch the Health To Your Heart application."""
from analyzer_ui import *

if __name__ == '__main__':
    data = DataAnalytic()
    ui = MyApp(data)
    ui.run()