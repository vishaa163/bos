CC = gcc
CFLAGS = -I../libmysyslog/include -I../libmysyslog-text/include -I../libmysyslog-json/include
LDFLAGS = -L../libmysyslog -L../libmysyslog-text -L../libmysyslog-json
LIBS = -lmysyslog -lmysyslog-text -lmysyslog-json

TARGET = mysyslog-client

SRC = src/mysyslog-client.c
OBJ = $(SRC:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS) $(LIBS)

clean:
	rm -f $(OBJ) $(TARGET)

install:
	cp $(TARGET) /usr/local/bin
