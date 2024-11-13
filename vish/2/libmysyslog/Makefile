CC = gcc
CFLAGS = -fPIC -Iinclude
LDFLAGS = -shared
TARGET = libmysyslog.so

SRC = src/mysyslog.c
OBJ = $(SRC:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(OBJ) $(TARGET)

install:
	mkdir -p /usr/local/lib
	cp $(TARGET) /usr/local/lib
	mkdir -p /usr/local/include/mysyslog
	cp include/mysyslog.h /usr/local/include/mysyslog
