# https://binhduong.edu.vn/tra-cuu-diem-thi-thpt-quoc-gia.html?action=submitScore&token=03ANYolqtvc-Sg_ylJ5osHIP_0bMBlhg0h1EQGmIrKkSGz955BrPK-GenLfYk8mMzbYa_ySGIeHMK80Ciev3lIw-j5q-T96dw3k-yjeThp1ZiF7AkoXnKj6hA8Nvk66jjB7AEYcRxQbc1Ru7dpRS0z43s6WA4Pc8c7gNIOjbVbka94ibHazphNZznUSYvwZCcVFkZYK-oeezJu1NZ1fkh5RlvL9AzieGEBWZizj47oGU0Z6wMPhq5WeCB25mfgt_J0TZi-Lt8BJldtmU7HchC_2sYLQRHw4qrOchOHkOjlywOkFcuStFp7hAOIgZ7VA3rEfSDOrinETodwfR82S0VoXUNuv1gA7E_BbCpj7jUSTNmt5Mgb4ZsniY11_PiwtXFDRPmkLeNuK6WewBpjcKNCHxAwkn6fl1fPtQG9zaao15_KwPSRBlKnAbHM4oeSTPpoQWWtVZqXFLqFGpIDcyoRdeEdJ5di-oPaDfZ74331FosEHr4ayKrbgc21Iw782Y8A1KHVO2E2BzroF4YjbF60_iHwItg8n-E9gg&ky-thi=thpt_qg_2022&tu-khoa=44002519

from multiprocessing.dummy import current_process
import requests
import multiprocessing as mp


def meo(reID, nstudent):
    filename = f"{reID}.txt"
    # global lst
    with open(filename, "w") as k:
        pass
    lst = ['studentCode', 'TOAN', 'VAN', 'LY', 'HOA', 'SINH', 'SU', 'DIA',
        'GDCD', 'NGOAINGU', 'CODE_NGOAINGU', 'groupCode', 'groupName']
    for j in range(1, nstudent+1):
        # print(55)
        id = "%.2d" % (reID) + "%.6d" % (j)
        url = f"https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/{id}.json"
        respone = requests.get(url)
        # print(respone.json())
        try:
            results = respone.json()
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(",".join([results[i] if results[i] !='' else "-1" for i in lst]) + "\n")
                # f.write("1564165465")
        except:
            pass


# if __name__ == "__main__":
#     # lst = ['studentCode', 'TOAN', 'VAN', 'LY', 'HOA', 'SINH', 'SU', 'DIA',
#     #        'GDCD', 'NGOAINGU', 'CODE_NGOAINGU', 'groupCode', 'groupName']

#     number_of_stu = [0, 90658, 81249, 21423, 11838, 0, 4524, 0, 0, 0, 8162, 2613, 13868, 0, 0, 0, 10853,
#                      14210, 17823, 0, 0, 18776, 11982, 8621, 0, 0, 0, 0, 0, 32478, 15898, 11536, 8251, 12801,
#                      0, 12216, 0, 17658, 13494, 10673, 18699, 12764, 13883, 9812, 11521, 5681, 9225, 11691,
#                      26252, 15058, 14285, 16353, 12060, 15676, 12629, 11324, 11905, 10360, 0, 9271, 0, 0, 0, 6513, 6638]

#     # Start first process
#     pce = [mp.Process(target=meo, args=(i, number_of_stu[i]))
#            for i in range(65)]
#     next = 19

#     cur_pro = set(range(3, 19))
#     for i in range(3, 19):
#         pce[i].start()
#     # for i in range(1, 17):
#     #     pce[i].join()
#     while next <= 64:
#         for i in cur_pro:
#             if not pce[i].is_alive():
#                 pce[i].terminate()
#                 cur_pro.discard(i)

#                 pce[next].start()
#                 cur_pro.add(next)
#                 next += 1

url = f"https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/03000307.json"
respone = requests.get(url)
print(respone.status_code)
print(respone.json())
