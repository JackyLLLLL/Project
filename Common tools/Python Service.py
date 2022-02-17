# encoding=utf-8
import win32serviceutil
import win32service
import win32event
import os
import logging
import inspect

class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonService" #這會顯示在服務的名稱
    _svc_display_name_ = "這是一串描述"#這會顯示在服務的描述/他原本是描述..
    _svc_description_ = "這一段原本該顯示在描述的，但是實際上卻沒有..."#這原本該顯示在描述可是卻不見了
    
    #初始化我們的服務
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True
    
    #這個Functin負責紀錄Log
    def _getLogger(self):
        logger = logging.getLogger('[PythonService]')

        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))
        #Log的檔案名稱在這裡，預設是Service的相對位置。

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger
    
    #此Function在服務啟動後將會自動執行Function內的程式碼
    def SvcDoRun(self):
        import time
        self.logger.info("service is run....")
        
##        #set auto reboot
##        os.system("python C:\\python_auto\\auto_reboot\\auto_reboot.py")
##
        
        while self.run:
            self.logger.info("I am runing....")
            time.sleep(60)#這裡每60秒迴圈，並紀錄一次log，請視需求調整頻率。
    
    #此Function在Service下"stop"指令或是"Restart時才會執行！
    #注意！當service Crash時並不會執行到此Function!
    def SvcStop(self):
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)
