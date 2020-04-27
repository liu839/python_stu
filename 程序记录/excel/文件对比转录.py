import openpyxl
wb1=openpyxl.load_workbook(r'C:\Users\71037\Desktop\周考五(日.xlsx')
wb2=openpyxl.load_workbook(r'C:\Users/71037/Desktop/日语周考5成绩.xlsx')
ws1=wb1["年级"]
ws2=wb2["Sheet1"]
for i_1 in range(2,420):
    name_1_sign='C'+str(i_1)
    name_1=ws1[name_1_sign].value
    score_1_sign='F'+str(i_1)
    score_1=ws1[score_1_sign].value
    for i_2 in range(3,62):
        name_2_sign='A'+str(i_2)
        name_2=ws2[name_2_sign].value
        score_2_sign='C'+str(i_2)
        score_2=ws2[score_2_sign].value
        if name_1==name_2:
            ws1[score_1_sign].value=ws2[score_2_sign].value
wb1.save(r'C:\Users\71037\Desktop\777.xlsx')