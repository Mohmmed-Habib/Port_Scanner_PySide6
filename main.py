import sys
import time
import socket
from PySide6 import QtWidgets, QtCore, QtGui
from gui import Ui_Dialog
from tools import Worker, check_ip_address


class APP(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(APP, self).__init__()
        self.setupUi(self)
        self.btn_scan.clicked.connect(self.run)
        self.threadpool = QtCore.QThreadPool()
        self.threadpool.setMaxThreadCount(4)
        self.ip_address_txt.setInputMask("000.000.000.000;_")
        self.start_port_txt.setInputMask("00000;_")
        self.end_port_txt.setInputMask('00000;_')

    def run(self):
        worker = Worker(self.scanner)
        worker.signals.result.connect(self.show_result)
        worker.signals.finished.connect(self.thread_complete)
        self.threadpool.start(worker)


    def scanner(self, result):
        self.btn_scan.setEnabled(False)
        host = self.ip_address_txt.text()
        open_ports = []
        try:
            if check_ip_address(self.ip_address_txt.text()):
                host = self.ip_address_txt.text()
                
                for port in range(int(self.start_port_txt.text()), int(self.end_port_txt.text())):
                    try:
                        s = socket.socket()
                        s.connect((host, port))
                    except:
                        result.emit(f"{host:15}:{port:5} is closed ")

                    else:
                        result.emit(f"{host:15}:{port:5} is open")
                        open_ports.append(port)

                result.emit(f'{len(open_ports)} Ports Open  : {open_ports}')
            else:
                result.emit("[+] Not Valid Ip address.")

        except Exception as e:
            result.emit(str(f'[Error] : {e}'))
    
    def show_result(self, log):
        self.textBrowser.append(log)

    def thread_complete(self):
        self.textBrowser.append('[+] DONE')
        self.btn_scan.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = APP()
    window.show()
    app.exec()