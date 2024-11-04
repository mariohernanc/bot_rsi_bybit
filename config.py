API_KEY = ""
SECRET_KEY = ""
TIMEFRAME = '1m'    # 3m, 5m
SOURCE = 'close'  # close

RSI_PERIOD = 7
RSI_UPPER = 75
RSI_LOWER = 25
ACTIVATE_LONG = True   # True: activa la apertura de ordenes LONG, False: desactiva la apertura de posiciones LONG
ACTIVATE_SHORT = True   # True: activa la apertura de ordenesSHORT, False: desactiva la apertura de posiciones SHORT
CLOSE_LONG = True   # True: activa el cierre de posiciones LONG, False: desactiva el cierre de posiciones LONG
CLOSE_SHORT = True   # True: activa el cierre de posiciones LONG, False: desactiva el cierre de posiciones SHORT

SYMBOLS = ['/USDT:USDT']    # BTC/USDT:USDT, ADA/USDT:USDT
COST = [8]   # ESTABLECER VALOR MINIMO DE PRIMERA ENTRADA EN DOLARES
TRADE_COUNT_LIMIT = [0] #Cantidad de recompras, en 0 significa sin limite de recompras
STOPLOSS_PERCENT = [100]  # 2% == 2/100 ej 1 = 100% cuenta
INCREMENTAL_ORDER = True  # True/False means to not use incremental order
INCREMENTAL_PRICE_PERCENT_LONG = [0.03]     # 0.2%  set % value distancia entre recompras
INCREMENTAL_PRICE_PERCENT_SHORT = [0.03]
INCREMENTAL_AMT_PERCENT_LONG = [2.5]     # 0.2%  set % value, va a sumar la recompra el monto minimo AMMOUNTS x INCREMENTAL_AMT_PERCENT
INCREMENTAL_AMT_PERCENT_SHORT = [1.5]     # 0.2%  set % value, va a sumar la recompra el monto minimo AMMOUNTS x INCREMENTAL_AMT_PERCENT
TAKEPROFIT_PERCENT = [0.01]  # ej. 0.01 = 1% distancia activa trailing stop, modificar en las lineas 292 a 300 BotRSI
BREAKEVEN_CLOSE = [0.005] # ej. 0.005 = 0.5% distancia a la que cierra la posicion luego de alcanzar el maximo mas alto despues del 1% anterior
