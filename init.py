#import fxcmpy and check the imported version
import fxcmpy

#con = fxcmpy.fxcmpy(access_token = token)
con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')

# CONECT
print("Conected : ",con.is_connected())

# INSCREVE NO CANAL 
con.subscribe_market_data('EUR/USD')
print(" Inscreve no Canal : ", con.is_subscribed('EUR/USD'))

count = 10

for i in range(count):
    print(con.get_last_price('EUR/USD'))
    
# CLOSE CONNECTION
con.close()
