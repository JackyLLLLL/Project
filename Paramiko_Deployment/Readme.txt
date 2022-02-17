透過Python實現批量檔案部屬、指令部屬
2021/12~2022/1
此專案使用Python語言以及paramiko模組、threading模組實現
1.批量傳輸檔案到Clinet端
2.批量下達指令到Clinet端
===================================
主要是為了解決下述情形而撰寫。

1.自主檢電腦有目錄及檔案內容不統一情形。
2.因應send_UDP 需回傳多個Server端時、Server端ip位址變更時。
3.改進了udp_client.py，config檔只需放入目錄內即會send udp至Server端。
-
程式語言：Python 
Ｍodule：paramiko、threading
開發平台：Windows 10、Linux Raspbian