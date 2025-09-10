# 1 intuito é trabalhar com try e except e função open 

try: 
    info= open('arquivo.txt', 'r')
    print(info.read())

except:
    print('nao foi possivel fazer uma leitura')     