class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers_cames = [0]
        customers_not_cames = [0]
        clients_comming = 0
        clients_not_comming = 0

        for at_hour in customers:
            if at_hour == 'Y':
                clients_comming += 1
            else:
                clients_not_comming += 1

            customers_cames.append(clients_comming)
            customers_not_cames.append(clients_not_comming)

        all_entries = customers_cames[-1] + customers_not_cames[-1]
        result = 0
        min_value = all_entries
        for index, (c, nc) in enumerate(zip(customers_cames, customers_not_cames), 1):
            tmp = (customers_cames[-1] - customers_cames[index - 1]) + customers_not_cames[index - 1]
            if tmp < min_value:
                result = index - 1
                min_value = tmp

        return result
