#Cargamos el cliente en localhost:8070
import os
os.system('cmd /c "docker pull grobid/grobid:0.7.2 & docker run --rm --gpus all -p 8070:8070 grobid/grobid:0.7.2"')

