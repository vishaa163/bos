CC = gcc
CFLAGS = -fPIC -Iinclude
LDFLAGS = -shared
TARGET = libmysyslog-json.so

SRC = src/mysyslog-json.c
OBJ = $(SRC:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET)

install:
	mkdir -p /usr/local/lib
	cp $(TARGET) /usr/local/lib
	mkdir -p /usr/local/include/mysyslog-json
	cp include/mysyslog-json.h /usr/local/include/mysyslog-json
