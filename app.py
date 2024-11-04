from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'  # Para manejar mensajes flash

# Diccionario para almacenar los datos temporalmente
items = {}
current_id = 1  # ID inicial para los elementos

# Ruta principal que muestra la lista de items
@app.route('/')
def index():
    return render_template('index.html', items=items)

# Ruta para crear un nuevo item (aseguramos que acepta POST)
@app.route('/create', methods=['POST'])
def create():
    global current_id
    name = request.form['name']
    description = request.form['description']
    items[current_id] = {'name': name, 'description': description}
    current_id += 1
    flash('Item creado exitosamente!')
    return redirect(url_for('index'))

# Ruta para eliminar un item por su ID
@app.route('/delete/<int:item_id>')
def delete(item_id):
    if item_id in items:
        del items[item_id]
        flash('Item eliminado exitosamente!')
    else:
        flash('Item no encontrado.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
