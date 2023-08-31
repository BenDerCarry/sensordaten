import requests
import time
import pandas as pd
import keyboard

IP_ADDRESS = '192.168.5.11:8080'
PP_CHANNELS = ['acc_time', 'accX', 'accY', 'accZ', 'gyr_time', 'gyrX', 'gyrY', 'gyrZ', 'mag_time', 'magX',
               'magY', 'magZ']
PP_CHANNELS_COUNT = len(PP_CHANNELS)


def start_recording(clear: bool = True):
    if clear:
        clear_recording()
    requests.get(f'http://{IP_ADDRESS}/control?cmd=start')
    time.sleep(0.5)


def stop_recording():
    requests.get(f'http://{IP_ADDRESS}/control?cmd=stop')


def clear_recording():
    requests.get(f'http://{IP_ADDRESS}/control?cmd=clear')


def record_sample():
    print('Recording sample...')
    start_recording(clear=True)
    start_time = time.time()

    stop_recording()
    # Get data
    req = [stat + '=full' for stat in PP_CHANNELS]
    data = requests.get(f'http://{IP_ADDRESS}/get?{"&".join(req)}')
    print(data.json())

    print(f'Recording sample finished. Took {time.time() - start_time} seconds.')

    print('Recording stopped.')
    time.sleep(1)


def main():
    record_sample()


if __name__ == '__main__':
    pass

print('Recording sample...')
start_recording(clear=True)
start_time = time.time()

# labeling
labelTime = start_time
labelList = []

# Unsere Label:
# Treppe3 -> stockwerk 3 Vor der Treppe
# Treppe3T -> stockwerk 3 Vor der Treppe bei den Toiletten
# C321/C317
# C320/C316
# C319/C314

# Labels für die Aufnahme 13.07.2023
#
# Erdgeschoss:
# Eingang, Erdgeschoss, VorDamenWC0, VorC013, C011/C012/C022, C023/C023a,
# VorC026, VorC042, VorHerrenWC0
# 1. Stock
# Stock1, VorC133, VorHerrenWC1, VorC109, VorC124, VorDamenWC1
# 2. Stock
# Stock2, VorC223, VorC225a, C225a, VorC203, VorHerrenWC2, VorC218, VorDamenWC2
# 3. Stock
# Treppe3, C321/C317, C321, C316, C320/C316, Treppe3T, C320, C317

# q ist stopp
#             w,          e,         r,       t,        z,        u,       i,       o,      p
layout1 = ['Treppe3', 'C321/C317', 'C321', 'C317', 'C320/C316', 'C320', 'C316', 'Treppe3T',
           'p']
#             a,        s,          d,              f,          g,          h,      j,k,l
layout2 = ['Stock1', 'VorC133', 'VorHerrenWC1', 'VorC109', 'VorC124', 'VorDamenWC1',
           'Stock2', 'VorC223', 'VorC225a']
#            j          k           l
# y,x,c,v,b,n,m
layout3 = ['C225a', 'VorC203', 'VorHerrenWC2', 'VorC218', 'VorDamenWC2', 'n', 'm']
#             y         x           c               v           b

# Handler für die Keyboard inputs

quitLoop = False


def keyq(event):
    global quitLoop
    print('You stopped the Recording')
    quitLoop = True


def keyw(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[0]])


def keye(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[1]])


def keyr(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[2]])


def keyt(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[3]])


def keyz(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[4]])


def keyu(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[5]])


def keyi(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[6]])


def keyo(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[7]])


def keyp(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout1[8]])


def keya(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[0]])


def keys(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[1]])


def keyd(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[2]])


def keyf(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[3]])


def keyg(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[4]])


def keyh(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[5]])


def keyj(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[6]])


def keyk(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[7]])


def keyl(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout2[8]])


def keyy(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[0]])


def keyx(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[1]])


def keyc(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[2]])


def keyv(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[3]])


def keyb(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[4]])


def keyn(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[5]])


def keym(event):
    global labelTime
    labelTime = time.time() - start_time
    labelList.append([labelTime, layout3[6]])


keyboard.on_press_key('q', keyq)
keyboard.on_press_key('w', keyw)
keyboard.on_press_key('e', keye)
keyboard.on_press_key('r', keyr)
keyboard.on_press_key('t', keyt)
keyboard.on_press_key('z', keyz)
keyboard.on_press_key('u', keyu)
keyboard.on_press_key('i', keyi)
keyboard.on_press_key('o', keyo)
keyboard.on_press_key('p', keyp)
keyboard.on_press_key('a', keya)
keyboard.on_press_key('s', keys)
keyboard.on_press_key('d', keyd)
keyboard.on_press_key('f', keyf)
keyboard.on_press_key('g', keyg)
keyboard.on_press_key('h', keyh)
keyboard.on_press_key('j', keyj)
keyboard.on_press_key('k', keyk)
keyboard.on_press_key('l', keyl)
keyboard.on_press_key('y', keyy)
keyboard.on_press_key('x', keyx)
keyboard.on_press_key('c', keyc)
keyboard.on_press_key('v', keyv)
keyboard.on_press_key('b', keyb)
keyboard.on_press_key('n', keyn)
keyboard.on_press_key('m', keym)

while not quitLoop:
    pass

time.sleep(1)

# Get data
req = [stat + '=full' for stat in PP_CHANNELS]
data = requests.get(f'http://{IP_ADDRESS}/get?{"&".join(req)}').json()
result_df = pd.DataFrame({key: data['buffer'][key]['buffer'] for key in PP_CHANNELS if 'acc' in key})
result2_df = pd.DataFrame({key: data['buffer'][key]['buffer'] for key in PP_CHANNELS if 'gyr' in key})
result3_df = pd.DataFrame({key: data['buffer'][key]['buffer'] for key in PP_CHANNELS if 'mag' in key})

print(f'Recording sample finished. Took {time.time() - start_time} seconds.')

stop_recording()
print('Recording stopped.')
time.sleep(1)

# Einfügen der Labels in den DataFrame
# leere Werte für die neue Spalte, die genauso Lang ist wie data

zeiger = 0
time = labelList[zeiger][0]
label = labelList[zeiger][1]

# die zeilen aus df aufrufen und zeiten abgleichen
counter = 0
result_df['label'] = ['PH'] * len(result_df)
for row in result_df.iterrows():
    # einfügen des labels in neuer spalte des dataframe
    try:
        result_df.loc[counter, 'label'] = label
    except:
        break

    counter += 1
    try:
        if result_df.loc[counter, 'acc_time'] > time:
            if zeiger < len(labelList) - 1:
                zeiger += 1
            time = labelList[zeiger][0]
            label = labelList[zeiger][1]
    except:
        break

# Label werden ausgegeben zum Testen/Kontrollieren
print(labelList)

result_df.to_csv('acc_data.csv')
result2_df.to_csv('gyr_data.csv')
result3_df.to_csv('mag_data.csv')
