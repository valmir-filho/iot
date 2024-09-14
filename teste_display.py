from machine import Pin, I2C
import ssd1306

# Inicializa o I2C
i2c = I2C(0, scl=Pin(23), sda=Pin(22))

# Inicializa o display
try:
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
    display.fill(0)
    display.text("Hello World!)", 0, 0)
    display.show()
except Exception as e:
    print("Error:", e)
