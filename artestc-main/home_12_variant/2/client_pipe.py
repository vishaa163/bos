import win32file

# Open named pipe for reading
pipe_name = r'\\.\pipe\my_named_pipe'
pipe = win32file.CreateFile(
    pipe_name,
    win32file.GENERIC_READ,
    0,
    None,
    win32file.OPEN_EXISTING,
    0,
    None
)

# Read data from the pipe
print("Waiting for data from the server...")
data = win32file.ReadFile(pipe, 65536)[1]
print(f"Received data: {data.decode()}")

# Close the pipe
win32file.CloseHandle(pipe)
