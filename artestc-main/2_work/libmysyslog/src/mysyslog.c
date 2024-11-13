#include <stdio.h>
#include <time.h>
#include "mysyslog.h"

int mysyslog(const char* msg, int level, int driver, int format, const char* path) {
    FILE* log_file = fopen(path, "a");
    if (!log_file) return -1;

    time_t now = time(NULL);
    fprintf(log_file, "Timestamp: %ld Level: %d Message: %s\n", now, level, msg);
    
    fclose(log_file);
    return 0;
}
