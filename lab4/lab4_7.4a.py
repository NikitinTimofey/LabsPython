ignore = ['duplex', 'alias', 'Current configuration']

def check_ignore(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    return any(word in command for word in ignore)

def config_to_dict(config_filename):
    """
    config_filename - имя конфигурационного файла
    Возвращает словарь:
    - Все команды верхнего уровня будут ключами.
    - Если у команды верхнего уровня есть подкоманды, они будут в значении у соответствующего ключа.
    - Значение может быть списком (если один уровень вложенности) или словарем (если два уровня вложенности).
    """
    config_dict = {}
    with open(config_filename) as conf_file:
        for command in conf_file:
            if check_ignore(command, ignore) or command.startswith('!'):
                continue
            if not command.startswith(' '):
                current_command = command.strip()
                config_dict[current_command] = {}
            elif command.startswith(' ') and not command.startswith('  '):
                sub_command = command.strip()
                config_dict[current_command][sub_command] = []
            elif command.startswith('  '):
                sub_sub_command = command.strip()
                last_key = list(config_dict[current_command].keys())[-1]
                config_dict[current_command][last_key].append(sub_sub_command)

    return config_dict

config_dict = config_to_dict("config_r1.txt")
for command, subcommands in config_dict.items():
    print(f"{command}: {subcommands}")