CC = gcc
TARGET = mysyslog-daemon

SRC = src/mysyslog-daemon.c
OBJ = $(SRC:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET)

install:
	cp $(TARGET) /usr/local/bin
