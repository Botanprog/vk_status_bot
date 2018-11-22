import time, vk_api

log_and_pass, start_time = ['Ваш логин','Ваш пароль'],  datetime.datetime.now()


try:		
	vk = vk_api.VkApi(login=log_and_pass[0], password=log_and_pass[1])
	vk.auth()
	print('Авторизация прошла успешно')
except:
	print('Ошибка авторизации')
	exit(0)


def set_status():
	time = datetime.datetime.now()
	uptime = (datetime.datetime.now() - start_time).total_seconds()
	hours, remainder = divmod(uptime,3600)
	minutes, seconds = divmod(remainder,60)
	text = f"💻 PC | 📅 {str(time).split()[0]} | ⌚ {str(time).split()[1][:5]} | ♻ Вечный онлайн: {'%02d:%02d:%02d'%(hours, minutes, seconds)}"
	
	try:
		vk.method('status.set',{'text':text})
	except:
		print('Problem :)')


def friends_remove():
	requests = vk.method('friends.getRequests',{'extended':0, 'need_mutual':0, 'out':1})
	if not requests:
		return
	for user_id in requests["items"]:
		vk.method('account.ban',{'owner_id':user_id})


def friends_accept():
	requests = vk.method('friends.getRequests',{'out':0,'need_viewed':0})
	if not requests:
		return
	for user_id in requests["items"]:
		vk.method('friends.add',{'user_id':user_id})


def online():
	try:
		vk.method('account.setOnline')
	except:
		print('Problem :)')


while True:
	set_status()
	friends_remove()
	friends_accept()
	online()
	time.sleep(60)
