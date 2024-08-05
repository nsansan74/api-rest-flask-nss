from flask import Flask, jsonify, request

app = Flask(__name__)

def metros_a_centimetros(metros):
    calculo = metros * 100
    return calculo

def centimetros_a_metros(centimetros):
    calculo = centimetros /100
    return calculo
   
def metros_a_pulgadas(metros):
    calculo = metros * 39.3700787
    return calculo

def pulgadas_a_metros(pulgadas):
    calculo = pulgadas / 39.37009424
    return calculo
 
@app.route('/convertir', methods = ['POST'])
def convertir_longitud():
    data = request.get_json()
    input_medida=data.get('medida')
    
    if data['type_de'] == 'metros' and  data['type_a'] == 'centimetros':
        result = metros_a_centimetros(input_medida)
        output_unit = 'centimetros'
    
    if data['type_de'] == 'centimetros' and data['type_a'] == 'metros':
        result = centimetros_a_metros(input_medida)
        output_unit = 'metros'
       
    if data['type_de'] == 'metros' and  data['type_a'] == 'pulgadas':
        result = metros_a_pulgadas(input_medida)
        output_unit = 'pulgadas'
    
    if data['type_de'] == 'pulgadas' and data['type_a'] == 'metros':
        result = pulgadas_a_metros(input_medida)
        output_unit = 'metros'   
    return jsonify({"longitud": result, "unidad": output_unit})

if __name__ == '__main__':
    app.run(debug=False)
    

#Esto esta en productivo