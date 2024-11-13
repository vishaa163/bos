
#!/bin/bash

# Переменные для логов
log_file=""
error_file=""

# Функция для вывода пользователей и их домашних директорий
list_users() {
    cat /etc/passwd | awk -F: '{print $1 ": " $6}' | sort
}

# Функция для вывода запущенных процессов
list_processes() {
    ps -e —sort=pid
}

# Функция для вывода справки
show_help() {
    echo "Usage: $0 [options]"
    echo "-u, —users         Show a list of users and their home directories"
    echo "-p, —processes     Show a list of running processes sorted by PID"
    echo "-h, —help          Display this help and exit"
    echo "-l, —log PATH      Log output to specified file"
    echo "-e, —errors PATH   Log errors to specified file"
}

# Функция для проверки доступа к файлу
check_path() {
    local path="$1"
    if [ ! -e "$path" ]; then
        echo "Error: Path $path does not exist." >&2
        return 1
    fi
    if [ ! -w "$path" ]; then
        echo "Error: Path $path is not writable." >&2
        return 1
    fi
    return 0
}

# Обработка аргументов командной строки
ARGS=$(getopt -o uphl:e: —long users,processes,help,log:,errors: — "$@")
if [ $? -ne 0 ]; then
    echo "Invalid arguments"
    exit 1
fi

eval set — "$ARGS"

# Логирование ошибок в stderr, если указано
if [ -n "$error_file" ]; then
    exec 2»"$error_file"
fi

output=$(ps -e --sort=pid | cat )  # Инициализируем переменную output

while true; do
    case "$1" in
        -u|--users)
            output=$(list_users)
            shift
            ;;
        -p|--processes)
           output=$(ps -e --sort=pid | cat)
            echo "Processes command executed" >&2
	    echo "Process output: $output" >&2
	    shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -l|--log)
            log_file="$2"
            if check_path "$log_file"; then
                echo "Logging output to $log_file"
            else
                exit 1
            fi
            shift 2
            ;;
        -e|--errors)
            error_file="$2"
            if check_path "$error_file"; then
                echo "Logging errors to $error_file"
            else
                exit 1
            fi
            shift 2
            ;;
        —)
            shift
            break
            ;;
        *)
            echo "Invalid option"
            exit 1
            ;;
    esac
done

# Проверка, пуст ли output
if [ -z "$output" ]; then
    echo "No data to output."
    exit 1
fi

# Логирование или вывод данных
if [ -n "$log_file" ]; then
    echo "$output" » "$log_file"
else
    echo "$output"
fi


