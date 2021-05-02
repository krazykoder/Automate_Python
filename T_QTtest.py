import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from lxml import html
import time

#Take this class for granted.Just use result of rendering.
# 1. Call Back funtion to print the HTML source
# 2. show() will show PyQTGUI browser


class Render(QWebEngineView):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.app.exec_()

    def callback_function(self, html):
        print(html)

    def _loadFinished(self, result):
        self.page().runJavaScript("document.documentElement.outerHTML",
                                  self.callback_function)

        # self.frame = self.
        # time.sleep(5)
        # self.app.quit()
        # self.resize(640, 480)

        self.show()
        # return


url = 'https://zetcode.com/pyqt/qwebengineview/'
r = Render(url)
# r.show()
# result = r.app.toHtml()
# # This step is important.Converting QString to Ascii for lxml to process

# # The following returns an lxml element tree
# archive_links = html.fromstring(str(result.toAscii()))
# print(archive_links)

# # The following returns an array containing the URLs
# raw_links = archive_links.xpath('/a/@href')
# print(raw_links)
