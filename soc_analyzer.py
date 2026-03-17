eventos = [
    {"ip": "192.168.0.10", "evento": "login_sucesso"},
    {"ip": "192.168.0.11", "evento": "login_falha"},
    {"ip": "192.168.0.11", "evento": "login_falha"},
    {"ip": "192.168.0.11", "evento": "login_falha"},
    {"ip": "10.0.0.5",     "evento": "scan_porta"},
    {"ip": "10.0.0.5",     "evento": "scan_porta"},
    {"ip": "172.16.0.7",   "evento": "login_sucesso"},
    {"ip": "8.8.8.8",      "evento": "acesso_externo"},
]

def contar_eventos(lista_eventos):
    pass

def identificar_bruteforce(lista_eventos):
    falhas = {}
    for evento in lista_eventos:
        if evento['evento'] == 'login_falha':
            ip = evento['ip']


def identificar_scanners(lista_eventos):
    pass

def listar_ips_unicos(lista_eventos):
    pass

def gerar_relatorio(lista_eventos):
    pass

if __name__ == "__main__":
    gerar_relatorio(eventos)

