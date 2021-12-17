ans = 'a123456' 
i = 3 #密碼驗證次數
while True:
	password = input('請輸入密碼')
	if password == ans:
		print('恭喜登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤！', i , '次機會')
		if i == 0:
			break