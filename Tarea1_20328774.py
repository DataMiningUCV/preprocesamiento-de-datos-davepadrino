# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:42:59 2016

@author: dave
"""
import pandas as pd
import re
import datetime
import io
io.open('/dev/null', 'wt', encoding='utf-8').write(u'ä')

csv_file1 = pd.read_csv('data.csv', header=0, index_col=0)
csv_file1 = csv_file1.reset_index(drop=True)
csv_file1 = csv_file1.rename(columns={'Indique.el.Período.Académico.a.renovar':'Indique_el_Periodo_Academico_a_renovar',
                                      'Cédula.de.Identidad': 'Cedula_de_Identidad',
                                      'Fecha.de.Nacimiento..colocar.sólo.datos.numéricos.': 'Fecha_de_Nacimiento',
                                      'Estado.Civil': 'Estado_Civil',
                                      'Sexo': 'Sexo_1_hombre__0_mujer',
                                      'Año.de.Ingreso.a.la.UCV': 'Ano_de_Ingreso_a_la_UCV',
                                      'Modalidad.de.Ingreso.a.la.UCV': 'Modalidad_de_Ingreso_a_la_UCV',
                                      'Semestre.que.cursa': 'Semestre_que_cursa',  
                                      'Ha.cambiado.usted.de.dirección.':'Ha_cambiado_usted_de_direccion',  
                                      'De.ser.afirmativo..indique.el.motivo': 'De_ser_afirmativo_indique_el_motivo',  
                                      'Número.de.materias.inscritas.en.el.semestre.o.año.anterior': 'Numero_de_materias_inscritas_en_el_semestre_o_ano_anterior',  
                                      'Número.de.materias.aprobadas.en.el.semestre.o.año.anterior': 'Numero_de_materias_aprobadas_en_el_semestre_o_ano_anterior', 
                                      'Número.de.materias.retiradas.en.el.semestre.o.año.anterior': 'Numero_de_materias_retiradas_en_el_semestre_o_ano_anterior',  
                                      'Número.de.materias.reprobadas.en.el.semestre.o.año.anterior': 'Numero_de_materias_reprobadas_en_el_semestre_o_ano_anterior',
                                      'Promedio.ponderado.aprobado': 'Promedio_ponderado_aprobado',
                                      'Si.reprobó.una.o.más.materias.indique.el.motivo': 'Si_reprobo_una_o_mas_materias_indique_el_motivo',
                                      'Número.de.materias.inscritas.en.el.semestre.en.curso': 'Numero_de_materias_inscritas_en_el_semestre_en_curso',
                                      'X.Estás.realizado.tesis...trabajo.de.grado.o.pasantías.de.grado.': 'Esta_realizado_tesis_trabajo_de_grado_o_pasantias_de_grado',
                                      'Tesis...trabajo.de.grado.o.pasantías.de.grado': 'Tesis_trabajo_de_grado_o_pasantias_de_grado_1_si__0_no',
                                      'Lugar.donde.reside.mientras.estudia.en.el.Universidad': 'Lugar_donde_reside_mientras_estudia_en_el_Universidad',
                                      'Personas.con.las.cuales.usted.vive..mientras.estudia.en.la.universidad.': 'Personas_con_las_cuales_usted_vive_mientras_estudia_en_la_universidad',
                                      'Tipo.de.vivienda.donde.reside.mientras.estudia.en.la.universidad': 'Tipo_de_vivienda_donde_reside_mientras_estudia_en_la_universidad',
                                      'En.caso.de.vivir.en.habitación.alquilada.o.residencia.estudiantil..indique.el.monto.mensual.': 'En_caso_de_vivir_en_habitacion_alquilada_o_residencia_estudiantil_indique_el_monto_mensual',
                                      'Dirección.donde.se.encuentra.ubicada.la.residencia.o.habitación.alquilada': 'Direccion_donde_se_encuentra_ubicada_la_residencia_o_habitación_alquilada',
                                      'X.Contrajo.Matrimonio.': 'Contrajo_Matrimonio',
                                      'X.Ha.solicitado.algún.otro.beneficio.a.la.Universidad.u.otra.Institución.': 'Ha_solicitado_algun_otro_beneficio_a_la_Universidad_u_otra_Institucion_1_si__0_no',
                                      'En.caso.afirmativo.señale..año.de.la.solicitud..institución.y.motivo': 'En_caso_afirmativo_senale_ano_de_la_solicitud_institucion_y_motivo',
                                      'X.Se.encuentra.usted..realizando.alguna.actividad.que.le.genere.ingresos.': 'Se_encuentra_usted_realizando_alguna_actividad_que_le_genere_ingresos_1_si__0_no',
                                      'En.caso.de.ser.afirmativo..indique.tipo.de.actividad.y.su.frecuencia': 'En_caso_de_ser_afirmativo_indique_tipo_de_actividad_y_su_frecuencia',
                                      'Monto.mensual.de.la.beca': 'Monto_mensual_de_la_beca',
                                      'Aporte.mensual.que.le.brinda.su.responsable.económico': 'Aporte_mensual_que_le_brinda_su_responsable_economico',
                                      'Aporte.mensual.que.recibe.de.familiares.o.amigos': 'Aporte_mensual_que_recibe_de_familiares_o_amigos',
                                      'Ingreso.mensual.que.recibe.por.actividades.a.destajo.o.por.horas': 'Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas',
                                      'Ingreso.mensual.total': 'Ingreso_mensual_total',
                                      'Gastos.médicos': 'Gastos_medicos',
                                      'Gastos.odontológicos': 'Gastos_odontologicos',
                                      'Gastos.personales': 'Gastos_personales',
                                      'Alimentación': 'Alimentacion',
                                      'Transporte.público': 'Transporte',
                                      'Residencia.o.habitación.alquilada': 'Residencia_o_habitacion_alquilada',
                                      'Materiales.de.estudio': 'Materiales_de_estudio',
                                      'Recreación': 'Recreacion',
                                      'Otros.gastos': 'Otros_gastos',
                                      'Total.egresos': 'Total_egresos',
                                      'Indique.quién.es.su.responsable.económico': 'Indique_quien_es_su_responsable_economico',
                                      'Carga.familiar': 'Carga_familiar',
                                      'Ingreso.mensual.de.su.responsable.económico': 'Ingreso_mensual_de_su_responsable_economico',
                                      'Otros.ingresos': 'Otros_ingresos',
                                      'Total.de.ingresos': 'Total_de_ingresos',
                                      'Alimentación.1': 'Alimentacion_Responsable',
                                      'Transporte': 'Transporte_resp',
                                      'Gastos.médicos.1': 'Gastos_medicos_responsable',
                                      'Gastos.odontológicos.': 'Gastos_odontologicos_responsable',
                                      'Gastos.educativos': 'Gastos_educativos',
                                      'Servicios.públicos.de.agua..luz..teléfono.y.gas': 'Servicios_publicos_de_agua_luz_telefono_y_gas',
                                      'Otros.gastos.1': 'Otro_gastos_resp',
                                      'Total.de.egresos': 'Total_de_egresos_resp',
                                      'Deseamos.conocer.la.opinión.de.nuestros.usuarios..para.mejorar.la.calidad.de.los.servicios.ofrecidos.por.el.Dpto..de.Trabajo.Social.OBE': 'Deseamos_conocer_la_opinion_de_nuestros_usuarios_para_mejorar_la_calidad_de_los_servicios_ofrecidos_por_el_Dpto_de_Trabajo_Social_OBE',
                                      'Sugerencias.y.recomendaciones.para.mejorar.nuestra.atención': 'Sugerencias_y_recomendaciones_para_mejorar_nuestra_atencion',
                                      })
                                      
                                      

# It works only for str types...                                      
def hasNumbers(h):
    return any(char.isdigit() for char in h) 
                                    
# ...and This is why i pass as a str()                                      
def _get_number(cad):
    if not hasNumbers(str(cad)) or not cad:
        return 0.0
    if str(cad).isdigit() == False: 
        x = re.findall("\d+[\.]?\d*", cad)
        return str(x[0])
    else:
        return str(cad)    
# This, extracts strings in a unique format for variable types of dates in this .csv
def _format_date(dat):
    if re.match("(\d{2})[/](\d{2})[/](\d{2})$", dat): #for  format "10/13/91" 
        return datetime.datetime.strptime(dat, '%d/%m/%y').strftime('%d/%m/%Y') 
    elif re.match("(\d{2})[-](\d{2})[-](\d{4})$", dat):  #for format "25-01-2013" 
        return datetime.datetime.strptime(dat, '%d-%m-%Y').strftime('%d/%m/%Y')
    elif re.match("(\d{2})[-](\d{2})[-](\d{2})$", dat):  #for format "25-01-13" 
        return datetime.datetime.strptime(dat, '%d-%m-%y').strftime('%d/%m/%Y')
    elif re.match("(\d{2})[ ](\d{2})[ ](\d{2})$", dat):  #for format "25 01 13" 
        return datetime.datetime.strptime(dat, '%d %m %y').strftime('%d/%m/%Y') 
    elif re.match("(\d{2})[ ](\d{2})[ ](\d{4})$", dat):  #for format "25 01 2013" 
        return datetime.datetime.strptime(dat, '%d %m %Y').strftime('%d/%m/%Y')        
    elif re.match("(\d{2})[/](\d{2})[/](\d{4})$", dat):  #for format "25/01/2013" 
        return dat    
    else:
        return "mal" 
        
        
'''
just to personal entries
    
'''                            
for i in range(len(csv_file1.Ingreso_mensual_total)):
  #f = csv_file1.Monto_mensual_de_la_beca.fillna(0)[i]+csv_file1.Aporte_mensual_que_le_brinda_su_responsable_economico.fillna(0)[i]+csv_file1.Aporte_mensual_que_recibe_de_familiares_o_amigos.fillna(0)[i] + csv_file1.Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas.fillna(0)[i]
  csv_file1.Monto_mensual_de_la_beca[i] = float(csv_file1.Monto_mensual_de_la_beca.fillna(0)[i]) 
  csv_file1.Aporte_mensual_que_le_brinda_su_responsable_economico[i] = float(csv_file1.Aporte_mensual_que_le_brinda_su_responsable_economico.fillna(0)[i])
  csv_file1.Aporte_mensual_que_recibe_de_familiares_o_amigos[i] = float(csv_file1.Aporte_mensual_que_recibe_de_familiares_o_amigos.fillna(0)[i]) 
  csv_file1.Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas[i] = float(csv_file1.Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas.fillna(0)[i])

csv_file1 = csv_file1.drop('Ingreso_mensual_total',1)      
      
      
'''
just to personal exit 
'''                            
for i in range(len(csv_file1.Total_egresos)):
    #f = int(csv_file1.Alimentacion.fillna(0)[i])+int(csv_file1.Transporte.fillna(0)[i]) + int(csv_file1.Gastos_medicos.fillna(0)[i]) + int(csv_file1.Gastos_odontologicos.fillna(0)[i])+ int(csv_file1.Gastos_personales.fillna(0)[i])+ int(csv_file1.Residencia_o_habitacion_alquilada.fillna(0)[i]) + int(csv_file1.Recreacion.fillna(0)[i]) +int(csv_file1.Materiales_de_estudio.fillna(0)[i])+ int(csv_file1.Otros_gastos.fillna(0)[i])
    csv_file1.Alimentacion[i] = float(csv_file1.Alimentacion.fillna(0)[i])
    csv_file1.Transporte[i] = float(csv_file1.Transporte.fillna(0)[i])
    csv_file1.Gastos_medicos[i] = float(csv_file1.Gastos_medicos.fillna(0)[i])
    csv_file1.Gastos_odontologicos[i]= float(csv_file1.Gastos_odontologicos.fillna(0)[i])
    csv_file1.Gastos_personales[i]= float(csv_file1.Gastos_personales.fillna(0)[i])
    csv_file1.Residencia_o_habitacion_alquilada[i]= float(csv_file1.Residencia_o_habitacion_alquilada.fillna(0)[i])
    csv_file1.Materiales_de_estudio[i]= float(csv_file1.Materiales_de_estudio.fillna(0)[i])

mean_avg_Other_spend = int(csv_file1['Otros_gastos'].mean())
csv_file1.Otros_gastos = csv_file1.Otros_gastos.fillna(mean_avg_Other_spend)
mean_avg_Recreation = int(csv_file1['Recreacion'].mean())
csv_file1.Recreacion = csv_file1.Recreacion.fillna(mean_avg_Recreation)
    

csv_file1 = csv_file1.drop('Total_egresos',1)      
 
 
'''
just to responsible's entries

'''                            
for i in range(len(csv_file1.Total_de_ingresos)):
    #f = float(_get_number(csv_file1.Ingreso_mensual_de_su_responsable_economico.fillna(0)[i].replace(" ", "").replace(",", "."))) + float(_get_number(csv_file1.Otros_ingresos.fillna(0)[i]))
    csv_file1.Ingreso_mensual_de_su_responsable_economico[i] = float(_get_number(csv_file1.Ingreso_mensual_de_su_responsable_economico.fillna(0)[i].replace(" ", "").replace(",", "."))) 
    csv_file1.Otros_ingresos[i] = float(_get_number(csv_file1.Otros_ingresos.fillna(0)[i]))

csv_file1 = csv_file1.drop('Total_de_ingresos',1)


                         
'''
Average of spent money in living place
'''
mean_avg_home=0
for j in range(len(csv_file1.Vivienda)):
    if str(csv_file1.Vivienda[j]).isdigit():
        mean_avg_home += int(csv_file1.Vivienda[j])      
mean_avg_home /=  len(csv_file1.Vivienda)   
  
      
'''
just to responsible's exit
'''   
for i in range(len(csv_file1.Total_de_egresos_resp)):
    #f = float(_get_number(csv_file1.Vivienda.fillna(0)[i])) +float(_get_number(csv_file1.Alimentacion_Responsable.fillna(0)[i]))+float(_get_number(csv_file1.Transporte_resp.fillna(0)[i])) + float(_get_number(csv_file1.Gastos_medicos_responsable.fillna(0)[i])) + float(_get_number(csv_file1.Gastos_odontologicos_responsable.fillna(0)[i])) + float(csv_file1.Gastos_educativos.fillna(0)[i]) + float(_get_number(csv_file1.Servicios_publicos_de_agua_luz_telefono_y_gas.fillna(0)[i])) + float(_get_number(csv_file1.Condominio.fillna(0)[i])) + float(csv_file1.Otro_gastos_resp.fillna(0)[i])       
    csv_file1.Vivienda[i] = int(_get_number(csv_file1.Vivienda.fillna(mean_avg_home)[i]))
    csv_file1.Alimentacion_Responsable[i] = _get_number(csv_file1.Alimentacion_Responsable.fillna(0)[i])
    csv_file1.Transporte_resp[i] = _get_number(csv_file1.Transporte_resp.fillna(0)[i])
    csv_file1.Gastos_medicos_responsable[i] = _get_number(csv_file1.Gastos_medicos_responsable.fillna(0)[i]) 
    csv_file1.Gastos_odontologicos_responsable[i] = _get_number(csv_file1.Gastos_odontologicos_responsable.fillna(0)[i]) 
    csv_file1.Gastos_educativos[i] = csv_file1.Gastos_educativos.fillna(0)[i]
    csv_file1.Servicios_publicos_de_agua_luz_telefono_y_gas[i] = _get_number(csv_file1.Servicios_publicos_de_agua_luz_telefono_y_gas.fillna(0)[i])
    csv_file1.Condominio[i] = _get_number(csv_file1.Condominio.fillna(0)[i])
    #csv_file1.Otro_gastos_resp[i] = csv_file1.Otro_gastos_resp.fillna(0)[i]
csv_file1= csv_file1[csv_file1.Vivienda != 0]
mean_avg_Other_spend = int(csv_file1['Otros_gastos'].mean())  
csv_file1.Otro_gastos_resp = csv_file1.Otro_gastos_resp.fillna(mean_avg_Other_spend)  
csv_file1 = csv_file1.drop('Total_de_egresos_resp',1)
csv_file1 = csv_file1.reset_index(drop=True)               
 
 
'''
Drop Age, changing address and reasons  
'''
csv_file1 = csv_file1.drop('Edad',1)
csv_file1 = csv_file1.drop('Ha_cambiado_usted_de_direccion',1)
csv_file1 = csv_file1.drop('De_ser_afirmativo_indique_el_motivo',1)
csv_file1 = csv_file1.drop('Esta_realizado_tesis_trabajo_de_grado_o_pasantias_de_grado',1)





# Management of efficient and average      
'''
Average 
'''
for i in range(len(csv_file1.Promedio_ponderado_aprobado)):
    if (csv_file1.Promedio_ponderado_aprobado[i] < 1):
        csv_file1.Promedio_ponderado_aprobado[i] = -1
    if (csv_file1.Promedio_ponderado_aprobado[i] > 20 and csv_file1.Promedio_ponderado_aprobado[i] < 99999):
        aux = round(csv_file1.Promedio_ponderado_aprobado[i]/1000,4)
        csv_file1.Promedio_ponderado_aprobado[i] = str(aux).encode('ascii', 'ignore')
    elif (csv_file1.Promedio_ponderado_aprobado[i] > 100000):
        aux = round(csv_file1.Promedio_ponderado_aprobado[i]/10000,4)
        csv_file1.Promedio_ponderado_aprobado[i] = str(aux).encode('ascii', 'ignore')
    elif (csv_file1.Promedio_ponderado_aprobado[i] > 0 and csv_file1.Promedio_ponderado_aprobado[i] <= 20):
        aux = round(csv_file1.Promedio_ponderado_aprobado[i],4) 
        csv_file1.Promedio_ponderado_aprobado[i] = str(aux).encode('ascii', 'ignore') 
        
csv_file1= csv_file1[csv_file1.Promedio_ponderado_aprobado != -1]   
csv_file1 = csv_file1.reset_index(drop=True)
     
     
'''
Efficiency
'''
for i in range(len(csv_file1.Eficiencia)):
    if (csv_file1.Eficiencia[i] > 1):
        if(csv_file1.Eficiencia[i] > 99 and csv_file1.Eficiencia[i] <= 1000):
            csv_file1.Eficiencia[i] = round(csv_file1.Eficiencia[i]/1000, 4)
        elif (csv_file1.Eficiencia[i] > 1000 and csv_file1.Eficiencia[i] <= 10000):
            csv_file1.Eficiencia[i] = round(csv_file1.Eficiencia[i]/10000, 4)    
        elif (csv_file1.Eficiencia[i] > 10000 and csv_file1.Eficiencia[i] < 99999):
            csv_file1.Eficiencia[i] = round(csv_file1.Eficiencia[i]/100000, 4)  
    else:
        csv_file1.Eficiencia[i] = round(csv_file1.Eficiencia[i],4)       
csv_file1 = csv_file1.reset_index(drop=True)               
        
# see the number of matters included vs matters retired, approved or reprobated       
'''
Matters included vs matters approved, retired and repobed
'''        
for i in range(len(csv_file1.Numero_de_materias_inscritas_en_el_semestre_o_ano_anterior)):        
    total_inscritas = int(_get_number(csv_file1.Numero_de_materias_aprobadas_en_el_semestre_o_ano_anterior[i])) + int(csv_file1.Numero_de_materias_retiradas_en_el_semestre_o_ano_anterior[i]) + int(csv_file1.Numero_de_materias_reprobadas_en_el_semestre_o_ano_anterior[i])    
    if total_inscritas != int(csv_file1.Numero_de_materias_inscritas_en_el_semestre_o_ano_anterior[i]):        
        csv_file1.Numero_de_materias_inscritas_en_el_semestre_o_ano_anterior[i] = -1        
        #print i
    else:
        csv_file1.Numero_de_materias_inscritas_en_el_semestre_o_ano_anterior[i] = total_inscritas
        
csv_file1= csv_file1[csv_file1.Numero_de_materias_inscritas_en_el_semestre_o_ano_anterior != -1]                                              
csv_file1 = csv_file1.reset_index(drop=True)

# Standard template for date and semester formats
'''
Template for standard values in "date" fields
'''                                              
for i in range(len(csv_file1.Fecha_de_Nacimiento)): 
    aux = str(_format_date(str(csv_file1.Fecha_de_Nacimiento[i])))   
    csv_file1.Fecha_de_Nacimiento[i] = aux.encode('utf8')    
csv_file1= csv_file1[csv_file1.Fecha_de_Nacimiento != "mal"]
csv_file1 = csv_file1.reset_index(drop=True)

csv_file1 = csv_file1.drop('Contrajo_Matrimonio',1)


'''
Template for standard values in "period" field 
'''
for i in range(len(csv_file1.Indique_el_Periodo_Academico_a_renovar)):
    #print "### ",i
    # For pri-15 or similar
    if re.match("([pri[mer[o]*]*|[01]]+)[ /[sem[estre]*]*]*[-]?[ ]*(\d{4}|\d{2})$", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE):
        if len(_get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]))==2:
            dat = datetime.datetime.strptime(_get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]), '%y').strftime('%Y')           
            aux = "I - "+str(dat).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux
        elif len(_get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]))==4:  
            dat = _get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i])           
            aux = "I - "+str(dat).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux    
   # for seg - 15 or similar       
    elif re.match('([se[c]*[g]*[undo]*|[02]]+)[ [sem[estre]*]*]*[-]*[ ]*(\d{4}|\d{2})$', csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE) or re.match("([2]+[ ]*([do]*))[ ]*[-]*[ ]*(\d{4}|\d{2})$", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE):
        if len(_get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]))==2:
            dat = datetime.datetime.strptime(_get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]), '%y').strftime('%Y')           
            aux = "II - "+str(dat).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux
        elif  len(_get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]))==4:  
            dat = _get_number(csv_file1.Indique_el_Periodo_Academico_a_renovar[i])            
            aux = "II - "+str(dat).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux   
   # for 2do 15 and similars       
    elif re.match ("([1|2]+[ ]*([ero]*|[do]*)[ /[sem[estre]*]*]*[-]*[ ]*(\d{4}|\d{2})$)", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE) or re.match ("([1|2][- ]+([ero]*|[do]*)[ -periodo]*[ -]*(\d{4}|\d{2})$)", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE):        
        if re.match ("([1|2]+[ ]*([ero]*|[do]*)[ /[sem[estre]*]*]*[-]*[ ]*(\d{4}|\d{2})$)", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE):        
            finder = re.findall ("([\d{1}][ ]*([ero]*|[do]*)[ /[sem[estre]*]*]*[-]*[ ]*(\d{4}|\d{2})$)", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE)
            if int(finder[0][0][0]) == 1:
                if len(finder[0][2])==2:
                    dat = datetime.datetime.strptime(finder[0][2], '%y').strftime('%Y')                
                    aux = "I - "+str(dat).encode('ascii', 'ignore')
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore') 
                elif  len(finder[0][2])==4:                 
                    aux = "I -"+str(finder[0][2]).encode('ascii', 'ignore')
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
            elif int(finder[0][0][0]) ==2:
                if len(finder[0][2])==2:               
                    dat = datetime.datetime.strptime(finder[0][2], '%y').strftime('%Y').strftime('%Y')           
                    aux = "II - "+str(dat).encode('ascii', 'ignore')
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
                elif len(finder[0][2])==4: 
                    aux = "II - "+str(finder[0][2]).encode('ascii', 'ignore')
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
                else:
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] = 0
        else:
            finder = re.findall ("([1|2][- ]+([ero]*|[do]*)[ -periodo]*[ -]*(\d{4}|\d{2})$)", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE)
            if int(finder[0][0][0]) == 1:
                if len(finder[0][2])==2:
                    dat = datetime.datetime.strptime(finder[0][2], '%y').strftime('%Y')                
                    aux = "I - "+str(dat).encode('ascii', 'ignore')
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore') 
                elif  len(finder[0][2])==4:                 
                    aux = "I -"+str(finder[0][2]).encode('ascii', 'ignore')
                    csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
                elif int(finder[0][0][0]) ==2:
                    if len(finder[0][2])==2:               
                        dat = datetime.datetime.strptime(finder[0][2], '%y').strftime('%Y').strftime('%Y')           
                        aux = "II - "+str(dat).encode('ascii', 'ignore')
                        csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
                    elif len(finder[0][2])==4: 
                        aux = "II - "+str(finder[0][2]).encode('ascii', 'ignore')
                        csv_file1.Indique_el_Periodo_Academico_a_renovar[i] = aux.encode('ascii', 'ignore') 
                    else:
                        csv_file1.Indique_el_Periodo_Academico_a_renovar[i] = 0                                    
    elif re.match("(\d{4}|\d{2})+[ ]*[-]+[ ]*([01]+)([a-z -]*)$", str(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]), re.IGNORECASE):       
        finder = re.findall("(\d{4}|\d{2})+[ ]*[-]+[ ]*([01]+)([a-z -]*)$", str(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]), re.IGNORECASE)
        if len(finder[0][0])==2:
            dat = datetime.datetime.strptime(finder[0][0], '%y').strftime('%Y')             
            aux = "I - "+str(dat).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
        elif  len(finder[0][0])==4:              
            aux =  "I - "+str(finder[0][0]).encode('ascii', 'ignore')           
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] = aux.encode('ascii', 'ignore') 
    elif re.match("(\d{4}|\d{2})+[ ]*[-]+[ ]*([02]+)([a-z -]*)$", str(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]), re.IGNORECASE):       
        finder = re.findall("(\d{4}|\d{2})+[ ]*[-]+[ ]*([02]+)([a-z -]*)$", str(csv_file1.Indique_el_Periodo_Academico_a_renovar[i]), re.IGNORECASE)
        if len(finder[0][0])==2:           
            dat = datetime.datetime.strptime(finder[0][0], '%y').strftime('%Y')           
            aux = "II - "+str(dat).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
        elif  len(finder[0][0])==4:            
            aux = "II - "+str(finder[0][0]).encode('ascii', 'ignore') 
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
    #match for II-2014 or similar
    elif re.match("([I]*)[ ]*[-]?[ ]*(\d{4})+[ ]*[-]?[ ]*([I]*)$", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE):
        finder = re.findall("([I]*)[ ]*[-]?[ ]*(\d{4})+[ ]*[-]?[ ]*([I]*)$", csv_file1.Indique_el_Periodo_Academico_a_renovar[i], re.IGNORECASE)        
        if not finder[0][0]:             
            aux = str(finder[0][2])+' - '+str(finder[0][1]).encode('ascii', 'ignore')
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] = aux.encode('ascii', 'ignore')
        elif not finder[0][2]:            
            aux = str(finder[0][0])+' - '+str(finder[0][1]).encode('ascii', 'ignore')           
            csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  aux.encode('ascii', 'ignore')
    else:
        csv_file1.Indique_el_Periodo_Academico_a_renovar[i] =  0
csv_file1= csv_file1[csv_file1.Indique_el_Periodo_Academico_a_renovar != 0]
csv_file1 = csv_file1.reset_index(drop=True)



'''
Only numbers on semester's values
'''
for i in range(len(csv_file1.Semestre_que_cursa)):
    csv_file1.Semestre_que_cursa[i] = _get_number(csv_file1.Semestre_que_cursa[i])
    

'''
Binarize Sex (Men -> 1; Women-> 0)
'''
for i in range(len(csv_file1.Sexo_1_hombre__0_mujer)):
    #print "####", i
    if csv_file1.Sexo_1_hombre__0_mujer[i] == 'Masculino':
        csv_file1.Sexo_1_hombre__0_mujer[i] =  1
    else:
        csv_file1.Sexo_1_hombre__0_mujer[i] = 0

'''
Binarize Tesis_trabajo_de_grado_o_pasantias (si -> 1; no-> 0)
'''
for i in range(len(csv_file1.Sexo_1_hombre__0_mujer)):
    #print "####", i
    if not pd.isnull(csv_file1.Tesis_trabajo_de_grado_o_pasantias_de_grado_1_si__0_no[i]):
        csv_file1.Tesis_trabajo_de_grado_o_pasantias_de_grado_1_si__0_no[i] =  1
    else:
        csv_file1.Tesis_trabajo_de_grado_o_pasantias_de_grado_1_si__0_no[i] = 0

'''
Binarize other benefits (Men -> 1; Women-> 0)
'''
for i in range(len(csv_file1.Ha_solicitado_algun_otro_beneficio_a_la_Universidad_u_otra_Institucion_1_si__0_no)):
    #print "####", i
    if re.match("([si])*$", csv_file1.Ha_solicitado_algun_otro_beneficio_a_la_Universidad_u_otra_Institucion_1_si__0_no[i], re.IGNORECASE):
        csv_file1.Ha_solicitado_algun_otro_beneficio_a_la_Universidad_u_otra_Institucion_1_si__0_no[i] =  1
    else:
        csv_file1.Ha_solicitado_algun_otro_beneficio_a_la_Universidad_u_otra_Institucion_1_si__0_no[i] = 0


'''
Binarize other benefits (Men -> 1; Women-> 0)
'''
for i in range(len(csv_file1.Se_encuentra_usted_realizando_alguna_actividad_que_le_genere_ingresos_1_si__0_no)):
    #print "####", i
    if re.match("([si])*$", csv_file1.Se_encuentra_usted_realizando_alguna_actividad_que_le_genere_ingresos_1_si__0_no[i], re.IGNORECASE):
        csv_file1.Se_encuentra_usted_realizando_alguna_actividad_que_le_genere_ingresos_1_si__0_no[i] =  1
    else:
        csv_file1.Se_encuentra_usted_realizando_alguna_actividad_que_le_genere_ingresos_1_si__0_no[i] = 0


csv_file1.to_csv('minable.csv')     
       

        
        