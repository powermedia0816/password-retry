password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('恭喜你成功登入')
		break
	else:
		print('密碼錯誤')
		if i > 0 :
			print('還有幾',i,'次機會')
		else:
			print('已經三次錯誤了，帳號被鎖住了')