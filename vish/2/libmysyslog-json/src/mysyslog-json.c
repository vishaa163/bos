#include <stdio.h>
#include <time.h>
#include "mysyslog-json.h"

int log_json(const char* msg, int level, const char* path) {
    FILE* log_file = fopen(path, "a");
    if (!log_file) return -1;

    time_t now = time(NULL);
    fprintf(log_file, "{\"timestamp\":%ld,\"level\":%d,\"message\":\"%s\"}\n", now, level, msg);
    
    fclose(log_file);
    return 0;
}
