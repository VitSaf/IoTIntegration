1. Открываем консоль и переходим в директорию, в которую вы разархивировали содержимое .ZIPa

2. Вводим команду “pip3 install pyinstaller” и ждем завершение установки

3. Вводим команду "sudo apt-get install python3-tk" далее спросят наше согласие ("y/n?") - соглашаемся(вводим "y")

4. Вводим команду “pyinstaller iiot_client_gui.py --noconsole --onefile” и опять ждем

5. В данной директории сгенерируется набор папок и файлов. Нам интересна только папка “dist”. Переходим в неё

6. Видим файл “iiot_client_gui.exe”(Вполне возможно, что и не .exe вовсе. Особенности ОС, но суть та же). Это он и есть# IoTIntegration
