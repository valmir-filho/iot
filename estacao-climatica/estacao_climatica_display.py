from machine import Pin, I2C
import ssd1306
import dht
import time

# Configuração do I2C para o display OLED.
i2c = I2C(0, scl=Pin(23), sda=Pin(22))  # Ajuste os pinos conforme necessário.
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuração do sensor DHT11.
sensor = dht.DHT11(Pin(13))  # Ajuste o pino conforme necessário.


# Função para atualizar o display com temperatura e umidade.
def atualizar_display(temperatura, umidade):
    display.fill(0)  # Limpa o display.
    display.text("Temp: {} Graus C".format(temperatura), 0, 0)
    display.text("", 0, 10)  # Linha em branco.
    display.text("Umidade: {}%".format(umidade), 0, 20)
    display.show()

# Loop de medição e exibição.
while True:
    try:
        sensor.measure()  # Faz a medição.
        temperatura = sensor.temperature()
        umidade = sensor.humidity()
        
        # Atualiza o display com as leituras.
        atualizar_display(temperatura, umidade)
        
        # Exibe no console para referência.
        print("A temperatura atual é: {}°C.".format(temperatura))
        print("A umidade relativa do ar atual é: {}%.".format(umidade))
        
        # Aguarda 5 segundos antes da próxima medição.
        time.sleep(5)
        
    except Exception as e:
        print("Erro:", e)
        time.sleep(5)  # Aguarda antes de tentar novamente em caso de erro.
