data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完畢，共有',len(data),'筆留言')

sumlen = 0
for d in data:
	len(d)
	sumlen = sumlen + len(d)

print('平均留言字數長度":', sumlen/len(data))

new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new),'筆資料字數小於100')

good=[]
for d in data:
	if 'good' in d:
		good.append(d)
print('共有',len(good),'筆留言提到good')

