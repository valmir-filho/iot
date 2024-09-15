# Imports.
from machine import Pin, I2C
import ssd1306
import dht
import time

# Configuração do I2C para o display OLED.
i2c = I2C(0, scl=Pin(23), sda=Pin(22))  # Ajuste os pinos conforme necessário.
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuração do sensor DHT11.
sensor = dht.DHT11(Pin(13))  # Ajuste o pino conforme necessário.

# Função para atualizar o display com data, hora, temperatura e umidade.
def atualizar_display(data_atual, hora_atual, temperatura, umidade):
    display.fill(0)  # Limpa o display.
    display.text("Data: {}".format(data_atual), 0, 0)
    display.text("Hora: {}".format(hora_atual), 0, 10)
    display.text("Temp: {} Graus C".format(temperatura), 0, 20)
    display.text("Umidade: {}%".format(umidade), 0, 30)
    display.show()

# Loop de medição e exibição.
while True:
    try:
        sensor.measure()  # Faz a medição.
        temperatura = sensor.temperature()
        umidade = sensor.humidity()

        # Obtém a data e hora atuais.
        tempo_atual = time.localtime()  # Retorna uma tupla (ano, mês, dia, hora, minuto, segundo, dia da semana, dia do ano).
        data_atual = "{:02d}/{:02d}/{:04d}".format(tempo_atual[2], tempo_atual[1], tempo_atual[0])  # Formata a data como DD/MM/AAAA.
        hora_atual = "{:02d}:{:02d}:{:02d}".format(tempo_atual[3], tempo_atual[4], tempo_atual[5])  # Formata a hora como HH:MM:SS.
        
        # Atualiza o display com as informações na ordem correta.
        atualizar_display(data_atual, hora_atual, temperatura, umidade)
        
        # Exibe no console para referência.
        print("Data atual: {}".format(data_atual))
        print("Hora atual: {}".format(hora_atual))
        print("A temperatura atual é: {}°C.".format(temperatura))
        print("A umidade relativa do ar atual é: {}%.".format(umidade))
        
        # Aguarda 2 segundos antes da próxima medição.
        time.sleep(2)
        
    except Exception as e:
        print("Erro:", e)
        time.sleep(2)  # Aguarda antes de tentar novamente em caso de erro.
