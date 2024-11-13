import win32event

# Открываем именованное событие, созданное сервером
signal_name = "MySignal"
signal = win32event.OpenEvent(win32event.EVENT_ALL_ACCESS, False, signal_name)

# Отправляем сигнал серверу
win32event.SetEvent(signal)
print("Клиент отправил сигнал серверу.")

# Закрываем событие
signal.Close()
