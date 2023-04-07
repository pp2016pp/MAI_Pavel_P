from typing import Any





class DLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
    pass

    def create_doubly_linked_list(numbers: list) -> DLNode:
        head = DLNode(numbers[0])
        prev_node = head
        for i in range(1, len(numbers)):
            new_node = DLNode(numbers[i])
            prev_node.next = new_node
            new_node.prev = prev_node
            prev_node = new_node
        return head

    # Здесь создается головной узел списка на основе первого элемента во входном списке.
    # Затем цикл проходит по оставшимся элементам и создает новые узлы, связывая их с предыдущим
    # узлом и устанавливая ссылку на следующий узел предыдущего узла и ссылку на предыдущий узел нового узла.
    # В конце головной узел возвращается как результат выполнения функции.

    def get_values_from_doubly_linked_list(head: DLNode) -> list:
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    # Здесь начинаем с головной ноды и проходимся по списку, добавляя значения каждого узла в результирующий список.
    # Когда мы не можем перейти к следующей ноде (т.е., когда мы подошли к концу списка), мы возвращаем результирующий
    # список с соответствующими значениями.

    def remove_node(head: DLNode, nodenum: int) -> DLNode:
        if nodenum == 1:
            # Если узел, который нужно удалить, является началом списка
            head.next.prev = None
            return head.next
        else:
            # Если узел, который нужно удалить, не является началом списка
            current = head
            count = 1
            while current is not None and count < nodenum:
                current = current.next
                count += 1
            if current is None:
                return head
            current.prev.next = current.next
            if current.next is not None:
                current.next.prev = current.prev
            return head

    def add_node(head: DLNode, nodenum: int, value: Any) -> DLNode:
        new_node = DLNode(value)
        if nodenum == 1:
            # Если узел, который нужно добавить, должен стать началом списка
            new_node.next = head
            if head is not None:
                head.prev = new_node
            return new_node
        else:
            # Если узел, который нужно добавить, не должен стать началом списка
            current = head
            count = 1
            while current is not None and count < nodenum:
                current = current.next
                count += 1
            if current is None:
                current = head
                while current.next is not None:
                    current = current.next
                current.next = new_node
                new_node.prev = current
            else:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            return head

    def add_node(head: DLNode, nodenum: int, value: Any) -> DLNode:
        new_node = DLNode(value)
        if nodenum == 1:
            # Если узел, который нужно добавить, должен стать началом списка
            new_node.next = head
            if head is not None:
                head.prev = new_node
            return new_node
        else:
            # Если узел, который нужно добавить, не должен стать началом списка
            current = head
            count = 1
            while current is not None and count < nodenum:
                current = current.next
                count += 1
            if current is None:
                current = head
                while current.next is not None:
                    current = current.next
                current.next = new_node
                new_node.prev = current
            else:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
            return head

        # Чтобы добавить узел в двусвязанный список по его порядковому номеру, нужно сначала найти предыдущий узел,
        # который будет предшествовать новому узлу. Вы можете перебирать список, пока не найдете узел с номером, на 1 меньшим, чем заданный номер, или пока не достигнете конца списка. Затем вы можете создать новый узел и обновить связи "prev" и "next" предыдущего и следующего узлов, чтобы вставить новый узел в список.

    def inverse_list(head: DLNode) -> DLNode:
        current = head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            head = temp.prev
        return head

        # Чтобы развернуть двусвязанный список, нужно поменять местами связи "prev" и "next" каждого узла в списке.
        # Это позволит сделать первый узел последним, а последний узел первым. Здесь мы используем временную переменную
        # "temp", чтобы сохранить связь "prev" текущего узла, прежде чем
        # изменить ее. Затем мы меняем местами связи "prev" и "next" для текущего узла и переходим к следующему узлу.
        # После того, как мы перебрали весь список, мы обновляем начало списка, если оно было изменено в процессе разворота.