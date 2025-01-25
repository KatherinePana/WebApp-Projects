from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hola_mundo(): 
    contenidoHtml = """ 
   <!DOCTYPE html>
   <html lang="en">
   <head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Página con Flask</title>
</head>
<body>  
    <h1>Hola Mundo desde Flask 😎</h1>
</body>
</html>
"""

return render_template_string(contenidoHtml)

if__name__== '__main__'  
 app.run(debug=Tue)
 