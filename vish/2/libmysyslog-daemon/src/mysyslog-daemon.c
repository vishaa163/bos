#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

void handle_signal(int sig) {
    if (sig == SIGTERM || sig == SIGINT) {
        printf("Daemon is stopping...\n");
        exit(0);
    }
}

int main() {
    signal(SIGTERM, handle_signal);
    signal(SIGINT, handle_signal);

    while (1) {
        printf("Daemon is running...\n");
        sleep(5);
    }

    return 0;
}
