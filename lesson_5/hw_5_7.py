# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме
import json

with open("hw_5_7.json", "w") as j_f_o:
    with open("hw_5_7_file.txt", "r") as f_o:
        client = {}
        info = {}
        total, client_1 = 0, 0
        lines = f_o.read().split("\n")
        for client_info in lines:
            client_info = client_info.split()
            prib = int(client_info[2]) - int(client_info[3])
            client[client_info[0]] = prib
            if prib > 0:
                total += prib
                client_1 += 1
            info["средняя прибыль"] = total / client_1
        list_company = [client, info]
    json.dump(list_company, j_f_o)
