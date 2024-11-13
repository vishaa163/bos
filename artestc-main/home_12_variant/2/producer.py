import win32event
import win32con

# Создаем именованное событие
signal_name = "MySignal"
signal = win32event.CreateEvent(None, 0, 0, signal_name)

# Ждем сигнала от клиента
print("Сервер ожидает сигнала от клиента...")
win32event.WaitForSingleObject(signal, win32event.INFINITE)
print("Сервер получил сигнал от клиента.")

# Закрываем событие
signal.Close()
