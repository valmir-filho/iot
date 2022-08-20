import dht
import machine
import network
import time
from conexao_internet import conexao
import urequests

sensor = dht.DHT11(machine.Pin(4)) 
rele = machine.Pin(2,machine.Pin.OUT)
rele.value(0)
contadorIf = contadorElse = contadorDados = 0

while True:
    sensor.measure()
    temperatura = (sensor.temperature())
    umidade = (sensor.humidity())
    print("Aluno: Valmir Moro Conque Filho")
    print("Turma: EAD ADS 2022 - Verão")
    print("Disciplina: IOT - Professor: Edson Kageyama")
    print()
    print("Estação Climática PUCPR")
    print()
    print("A temperatura atual é: {}°C.".format(temperatura))
    print("A umidade relativa do ar atual é: {}%.".format(umidade))
    print()
    print("Condições para acionamento do Relé: Temp. > 31°C ou Umid. Rel. do Ar > 70%.")
    print()
    time.sleep(2)
    if temperatura > 31 or umidade > 70:
        rele.value(1)
        contadorIf += 1
        print("Relé ligado.")
        print()
        print("Número de impressões no console: {}.".format(contadorIf))
        print()
        contadorElse = 0
    else:
        rele.value(0)
        contadorElse += 1 
        print("Relé desligado.")
        print()
        print("Número de impressões no console: {}.".format(contadorElse))
        print()
        contadorIf = 0
    print("Conectando com a rede WIFI...")
    time.sleep(2)
    print()
    print("Conexão com a rede WIFI realizada com sucesso!")
    print()
    station = conexao("NOKIA-3BE9", "2jLnqiCPNM")
    if not station.isconnected():
        print("Erro de conexão com a rede WIFI! Tente novamente.")
        print()
    else:
        contadorDados += 1
        print("Acessando a plataforma ThingSpeak...")
        time.sleep(2)
        print()
        print("Acesso a plataforma ThingSpeak realizada com sucesso!")
        print()
        print("Enviando os dados...")
        response = urequests.get("https://api.thingspeak.com/update?api_key=VASQJ2UP4CJB19R9&field1={}&field2={}".format(temperatura,umidade))
        time.sleep(2)
        print()
        print("Dados enviados com sucesso!")
        print()
        print("{} coleta(s) de dado(s) enviada(s) a plataforma ThingSpeak.".format(contadorDados))
        print()
        response.text
        station.disconnect()
        time.sleep(2)