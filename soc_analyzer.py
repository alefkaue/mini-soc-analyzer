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
    contagem = {}
    for evento in lista_eventos:
        tipo = evento['evento']
        if tipo in contagem:
            contagem[tipo] += 1
        else:
            contagem[tipo] = 1
    return contagem


def identificar_bruteforce(lista_eventos):
    falhas = {}
    for evento in lista_eventos:
        if evento['evento'] == 'login_falha':
            ip = evento['ip']


def identificar_scanners(lista_eventos):
    scans = {}
    for evento in lista_eventos:
        if evento['evento'] == 'scan_porta':
            ip = evento['ip']
            scans[ip] = scans.get(ip, 0) + 1
    return [ip for ip, qtd in scans.items() if qtd >= 2]


def listar_ips_unicos(lista_eventos):
    pass

def gerar_relatorio(lista_eventos):
    pass

if __name__ == "__main__":
    gerar_relatorio(eventos)

