#ifndef MYSYSLOG_H
#define MYSYSLOG_H

#define LOG_LEVEL_DEBUG 0
#define LOG_LEVEL_INFO 1
#define LOG_LEVEL_WARN 2
#define LOG_LEVEL_ERROR 3
#define LOG_LEVEL_CRITICAL 4

int mysyslog(const char* msg, int level, int driver, int format, const char* path);

#endif // MYSYSLOG_H
