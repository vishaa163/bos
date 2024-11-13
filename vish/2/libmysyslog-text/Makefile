CC = gcc
CFLAGS = -fPIC -Iinclude
LDFLAGS = -shared
TARGET = libmysyslog-text.so

SRC = src/mysyslog-text.c
OBJ = $(SRC:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET)

install:
	mkdir -p /usr/local/lib
	cp $(TARGET) /usr/local/lib
	mkdir -p /usr/local/include/mysyslog-text
	cp include/mysyslog-text.h /usr/local/include/mysyslog-text
