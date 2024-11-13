# Домашнее задание #3

Реализовать клиент-серверное приложение средствами языка программирования `C / Java / Python / Go / Rust`, в котором клиент аргументами командной строки получает `ip адрес` сервера, `порт` и `команду bash`, которую должен выполнить сервер. Сервер получает строку с командой, выполняет ее, и возвращает результат выполнения клиенту. Клиент получает результат и прекращает работу. При получении сервером команды `exit` от клиента, его работа завершается. При обмене, оборачивать информацию в контейнер вида:

```
+-------------------+
| command | payload |
+-------------------+
```

Пример запросов с клиента: `exit | NULL`, `execute | ls -la \`, `execute | whoami`.

Пример ответов от сервера: `reponse | OK`, `response | .`, `response | fizzbuzz`.

Дизайн контейнера -- на усмотрение исполнителя.

Для успешного выполнения задания, файлы с исходным кодом должны быть выложены в этом репозитории ([в текущей директории](./)) по аналогии с предыдущими ДЗ. Результат выполнения программ должен быть зафиксирован на скриншоте и выложен в этом репозитории.

Полезные материалы:

* [socket - create an endpoint for communication](https://man7.org/linux/man-pages/man2/socket.2.html)
* [The getopt() function parses the command-line arguments](https://man7.org/linux/man-pages/man3/getopt.3.html)
* [bind - bind a name to a socket](https://man7.org/linux/man-pages/man2/bind.2.html)
* [ip - Linux IPv4 protocol implementation](https://man7.org/linux/man-pages/man7/ip.7.html)
* [accept - accept a connection on a socket](https://man7.org/linux/man-pages/man2/accept.2.html)
* [connect - initiate a connection on a socket](https://man7.org/linux/man-pages/man2/connect.2.html)
* [Структура sockaddr_in](https://www.opennet.ru/docs/RUS/socket/node4.html)
* [How to read the content of a file to a string in C? - Stack Overflow](https://stackoverflow.com/questions/174531/how-to-read-the-content-of-a-file-to-a-string-in-c/174552#174552)
* [Проект OpenNet: MAN recv (2) Системные вызовы (FreeBSD и Linux)](https://www.opennet.ru/man.shtml?topic=recv&category=2&russian=0)
* [Функция send](https://www.opennet.ru/docs/RUS/linux_base/node250.html)