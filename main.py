import psutil

while True:
    menu = int(input(
        '''O que você quer fazer:
        [1] Monitoramento do uso da CPU
        [2] Monitoramento do uso da memória
        [3] Monitoramento de disco
        [4] Gerenciamento de rede
        [5] Gerenciamento de processos
        [6] Verificação do status da bateria
        [0] Sair
        '''))

    # 1 Monitoramento do uso da CPU
    if menu == 1: 
        print("Monitoramento do uso da CPU")
        cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
        print("Porcentagem de uso da CPU por núcleo: ")
        for i, usage in enumerate(cpu_usage_per_core):
            print(f"Núcleo {i + 1}: {usage:.1f}%")


    # 2 Monitoramento do uso da memória
    elif menu == 2:
        print("Monitoramento do uso da memória")
        memory_info = psutil.virtual_memory()
        print(f"Memória Total: {memory_info.total / (1024 ** 3):.2f} GB")
        print(f"Memória Disponível: {memory_info.available / (1024 ** 3):.2f} GB")
        print(f"Porcentagem de uso da memória: {memory_info.percent:.2f}%")


    # 3 Monitoramento de disco 
    elif menu == 3: 
        print("Monitoramento de disco")
        disk_usage = psutil.disk_usage('/')
        print("Uso do disco na partição raiz:")
        print(f"Total: {disk_usage.total / (1024 ** 3):.2f} GB")
        print(f"Usado: {disk_usage.used / (1024 ** 3):.2f} GB")
        print(f"Livre: {disk_usage.free / (1024 ** 3):.2f} GB")
        print(f"Porcetagem de uso: {disk_usage.percent:.2f}%")

    # 4 Gerenciamento de rede
    elif menu == 4: 
        print("Gerenciamento de rede")
        net_io = psutil.net_io_counters()
        print(f"Bytes enviados: {net_io.bytes_sent / (1024 ** 3):.2f} GB")
        print(f"Bytes recebidos: {net_io.bytes_recv / (1024 ** 3):.2f} GB")


    # 5 Gerenciamento de processos
    elif menu == 5:  
        print("Gerenciamento de processos")
        for proc in psutil.process_iter(['pid', 'name', 'username'], 1):
            print(proc.info)
            i = 0
            if i % 10 == 0:
                if input("Presione ENTER para continuar ou 'x' para sair: ").lower() == 'x':
                    break


    # 6 Verificação do status da bateria
    elif menu == 6: 
        print("Verificação do status da bateria")
        battery = psutil.sensors_battery()
        if battery:
            print(f"Percentual de bateria: {battery.percent:.2f}%")
            print("Carregando: ", battery.power_plugged)
        else:
            print("Nenhuma bateria detectada.")
        
    elif menu == 0:
        print("Você escolheu a opção sair!")
        break

    else:
        print("Opção inválida.")