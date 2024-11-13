import win32pipe
import win32file

# Create named pipe
pipe_name = r'\\.\pipe\my_named_pipe'
pipe = win32pipe.CreateNamedPipe(
    pipe_name,
    win32pipe.PIPE_ACCESS_OUTBOUND,
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
    1,
    65536,
    65536,
    0,
    None
)

# Wait for client connection
print("Waiting for client connection...")
win32pipe.ConnectNamedPipe(pipe, None)

# Send data to the client
data = "Привет, клиент!"
print(f"Sending data: {data}")
win32file.WriteFile(pipe, data.encode())

# Close the pipe
win32pipe.DisconnectNamedPipe(pipe)
win32file.CloseHandle(pipe)
