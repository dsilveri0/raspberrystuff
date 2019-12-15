import requests
from datetime import datetime 

def post(auxInput):
	# configurações do serviço Web (alterar para URL correta)
	paramUrl = 'http://10.42.0.151/api/lab04_api_post_json_switch.php'
	paramAuth = 'irsotesppsi'
	paramKey = 'switch'
	paramNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	paramJSON = {'auth':paramAuth, 'key':paramKey, 'value':auxInput, 'date':paramNow}
	paramHeaders = {'content-type': 'application/json'}
	# enviar dados para o serviço Web (formato: json)
	print("a enviar para o serviço Web...")
	r = requests.post(paramUrl, json=paramJSON, headers=paramHeaders)
	# mostrar resultados
	print(r)
	print(r.text)
	
	#print("Fim do programa.")
	return;


try:  
	print("CTRL+C para terminar.")
	while True:
		led = input('Escreva 0 para apagar o Led ou 1 para acender o Led no seu site!\n')
		print ('valor %s \n' % (led))
		post(led)
		print("\nPressione as teclas CTRL+C para terminar.")
except KeyboardInterrupt:
	print("\nPrograma terminado pelo utilizador.")		
except:
	print("\nErro!!!")
finally:
	print("ok.")
print("Fim do programa.")

