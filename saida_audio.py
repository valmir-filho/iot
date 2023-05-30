import machine
import time

# Configuração dos pinos do ESP WROOM-32.
left_audio_pin = machine.Pin(23, machine.Pin.OUT)  # Pino de saída de áudio lado esquerdo.
right_audio_pin = machine.Pin(22, machine.Pin.OUT)  # Pino de saída de áudio lado direito.

# Configuração dos objetos PWM.
left_pwm = machine.PWM(left_audio_pin)
right_pwm = machine.PWM(right_audio_pin)

# Função para reproduzir o áudio.
def play_audio(left_value, right_value):
    left_pwm.duty(left_value)
    right_pwm.duty(right_value)

# Configuração inicial dos objetos PWM.
left_pwm.freq(1000)  # Frequência de PWM para o pino esquerdo.
right_pwm.freq(1000)  # Frequência de PWM para o pino direito.

# Exemplo de reprodução de áudio.
while True:
    play_audio(512, 512)  # Valor médio para reproduzir áudio mono.
    # time.sleep(0.1)
    # play_audio(0, 1023)  # Valor máximo para reproduzir áudio estéreo.
    # time.sleep(0.1)
