class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, input_list):
        # Если список пуст, возвращаем 0, чтобы избежать деления на ноль
        if not input_list:
            return 0
        # Рассчитываем среднее значение списка
        return sum(input_list) / len(input_list)

    def compare_lists(self):
        # Рассчитываем среднее значение для обоих списков
        avg_list1 = self.calculate_average(self.list1)
        avg_list2 = self.calculate_average(self.list2)

        # Сравниваем средние значения и возвращаем соответствующий результат
        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        elif avg_list2 > avg_list1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
