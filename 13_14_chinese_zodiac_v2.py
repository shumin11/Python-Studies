#记录生肖，根据年份来判断生肖

# chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马牛羊'


# year = int(input('请用户输入年份'))

#  if (chinese_zodiac[year % 12]) == '狗':
#      print('狗年运势')
# for cz in chinese_zodiac:
#     print(cz)
# for i in range(12):
#     print(i)

# for year in range(2000, 2019):
#      print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

num =5
while True: # while normally connect with break or continue 
   num = num + 1
   if num == 10:
      break    #stop the recursion
   #continue to skip this step and move to next
print(num)
 