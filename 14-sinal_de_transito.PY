# SINAL DE TRANSITO
from pyfirmata import Arduino, util, OUTPUT
import lcd
import time

board=Arduino ('COM5')
verm = 7
amar = 6
verd = 5
lcd.escrever(board, 0, 0, 'SINAL DE TRANSITO')
board.digital[verm].mode = OUTPUT
board.digital[amar].mode = OUTPUT
board.digital[verd].mode = OUTPUT

while True:
    board.digital[verm].write(1)
    lcd.escrever(board, 0, 1, 'VERMELHO = PARE  ')
    time.sleep(5)
    board.digital[verm].write(0)
    board.digital[amar].write(1)
    lcd.escrever(board, 0, 1, 'AMARELO = ATENCAO')
    time.sleep(3)
    board.digital[amar].write(0)
    board.digital[verd].write(1)
    lcd.escrever(board, 0, 1, 'VERDE = SIGA    ')
    time.sleep(5)
    board.digital[verd].write(0)