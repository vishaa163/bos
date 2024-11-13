#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
#include "mysyslog.h"

int main(int argc, char *argv[]) {
    int level = LOG_LEVEL_INFO;
    int driver = 1;  // 1 - text, 2 - json
    char *msg = NULL;
    char *path = "logfile.txt";

    int opt;
    while ((opt = getopt(argc, argv, "m:l:d:p:")) != -1) {
        switch (opt) {
            case 'm':
                msg = optarg;
                break;
            case 'l':
                level = atoi(optarg);
                break;
            case 'd':
                driver = atoi(optarg);
                break;
            case 'p':
                path = optarg;
                break;
            default:
                fprintf(stderr, "Usage: %s -m message -l log_level -d driver -p path\n", argv[0]);
                exit(EXIT_FAILURE);
        }
    }

    if (!msg) {
        fprintf(stderr, "Message is required!\n");
        exit(EXIT_FAILURE);
    }

    mysyslog(msg, level, driver, 0, path);
    return 0;
}
