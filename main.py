import webbrowser
import threading
import time


def baixar_arquivos_site(site):
    print(f'navegando ate o {site}')
    webbrowser.open(site)
    for i in range(1, 20):
        print(f'Processando dados - {i}/19')
        time.sleep(1)
    print('finlizando extração')


def baixar_arq():
    for i in range(1, 10):
        print(f'Baixando Arquivos - {i}/10')
        time.sleep(1)
    print('Arquivos baixados')


nova_thread = threading.Thread(
    target=baixar_arquivos_site, args=('https:www.mercadolivre.com.br/',), daemon=True)
nova_thread.start()
baixar_arq()
nova_thread.join()