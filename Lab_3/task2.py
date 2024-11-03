# # TODO Напишите функцию find_common_participants
#
#
# participants_first_group = "Иванов|Петров|Сидоров"
# participants_second_group = "Петров|Сидоров|Смирнов"
#
# # TODO Провеьте работу функции с разделителем отличным от запятой


def find_common_participants(participants_first_group, participants_second_group, separator=','):

    participants1 = set(participants_first_group.split(separator))
    participants2 = set(participants_second_group.split(separator))

    common_participants = sorted(participants1.intersection(participants2))

    return  common_participants


participants_first_group = "Иванов, Петров, Сидоров"
participants_second_group = "Петров, Сидоров, Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))


