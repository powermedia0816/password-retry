password = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('恭喜你成功登入')
		break
	else:
		i = i - 1
		print('密碼錯誤，剩下',i,'幾次機會')
		if i == 0:
			break
