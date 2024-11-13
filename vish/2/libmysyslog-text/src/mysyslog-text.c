#include <stdio.h>
#include <time.h>
#include "mysyslog-text.h"

int log_text(const char* msg, int level, const char* path) {
    FILE* log_file = fopen(path, "a");
    if (!log_file) return -1;

    time_t now = time(NULL);
    fprintf(log_file, "%ld %d %s\n", now, level, msg);
    
    fclose(log_file);
    return 0;
}
