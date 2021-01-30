# coding_LUJINGJING
import pandas as pd

# Action 1求2+4+6+。。。。100的求和
sum = 0
for i in range(2, 102, 2):
    sum = sum + i
print(sum)
# Action2 ,统计全班的成绩
data = pd.DataFrame({'姓名': ['张飞', '关羽', '刘备', '典韦', '许褚'], '语文': [68, 95, 98, 90, 80], '数学': [65, 76, 86, 88, 90],
                     '英语': [30, 98, 88, 77, 90]})
print(data)


def result(a):
    print(a + '的平均分：%d' % data[a].mean())
    print(a + '的最大分：%d' % data[a].max())
    print(a + '的最小分：%d' % data[a].min())
    print(a + '的方差：%f' % data[a].var())
    print(a + '的标准差：%f' % data[a].std())


result('语文')
result('数学')
result('英语')
print("==========================================")

# Action3.对汽车质量数据进行统计,品牌投诉总数，车型投诉总数，那个品牌的平均车型投诉最多
data2 = pd.read_csv(r'D:\黑马课程\第一课\L1\car_data_analyze\car_complain.csv')
# data2=data2_fz[data2_fz['brand'].str.replace('-','')]
data2['brand'] = data2['brand'].str.replace('-', '').str.replace('奥迪', '')
print(data2)
# data2['complain_nr']=len(data2['problem'].str.split(','))
complain_nr_list = []
for i1 in range(0, len(data2.index.tolist())):
    # print(len(data2['problem'][i].split(','))-1)
    complain_nr_list.append(len(data2['problem'][i1].split(',')) - 1)
    # data2['complain_nr'][i]=len(data2['problem'][i].split(','))
data2['complain_nr'] = complain_nr_list

carplant1 = pd.DataFrame(data2.groupby(['brand'])['complain_nr'].sum())\
    .loc[pd.DataFrame(data2.groupby(['brand'])['complain_nr'].sum())['complain_nr']==\
         pd.DataFrame(data2.groupby(['brand'])['complain_nr'].sum())['complain_nr'].max(),:]
carplant2 =pd.DataFrame(data2.groupby(['brand', 'car_model'])['complain_nr'].sum())\
    .loc[pd.DataFrame(data2.groupby(['brand', 'car_model'])['complain_nr'].sum())['complain_nr']==\
    pd.DataFrame(data2.groupby(['brand', 'car_model'])['complain_nr'].sum())['complain_nr'].max()]
carplant3 = pd.DataFrame(round(data2.groupby(['brand', 'car_model'])['complain_nr'].mean(), 2))
carplant3_max = round(data2.groupby(['brand', 'car_model'])['complain_nr'].mean(), 2).max()
carplant4 = carplant3.loc[carplant3['complain_nr'] == carplant3_max, :]
print("品牌投诉总数，车型投诉总数:\n")
print(carplant1)  # 品牌投诉总数，车型投诉总数
print("======================================================\n车型投诉总数:\n")
print(carplant2)  # 车型投诉总数
print("======================================================\n车型平均投诉,小数点2位:\n")
print(carplant4)  # 车型平均投诉,小数点2位
