'''
Created on 15/11/2017

@author: lovehinata

XXX: http://codeforces.com/contest/492/problem/C
'''
import logging
import sys

nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def vania_puta_core(examenes, tope_calificacion, promedio):
    examenes_tam = len(examenes)
    total_de_promedio = examenes_tam * promedio
    chosto_total = 0
    
    total_inicial = 0
    
    for _, calif in examenes:
        total_inicial += calif
    
    faltante_para_total_de_promedio = total_de_promedio - min(total_de_promedio, total_inicial)
    
    for chosto, calif in examenes:
        if(calif < tope_calificacion and faltante_para_total_de_promedio):
            faltante_calif_para_torpe = tope_calificacion - calif
            putos_a_tomar = min(faltante_para_total_de_promedio, faltante_calif_para_torpe)
            faltante_para_total_de_promedio -= putos_a_tomar
            chosto_total += chosto * putos_a_tomar
            if(not faltante_para_total_de_promedio):
                break
    
    return chosto_total

def vania_puta_main():
    lineas = list(sys.stdin)
    
    _, tope_calificacion, promedio = [int(x) for x in lineas[0].strip().split(" ")]
    
    examenes = []
    
    for linea in lineas[1:]:
        calif, chosto = [int(x) for x in linea.strip().split(" ")]
        examenes.append((chosto, calif))
    
    examenes.sort()
    logger_cagada.debug("examenes {}".format(examenes))
    
    chosto_total = vania_puta_core(examenes, tope_calificacion, promedio)
    print("{}".format(chosto_total))

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)
        vania_puta_main()
