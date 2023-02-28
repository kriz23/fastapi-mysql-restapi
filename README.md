Proyecto creado con `Python 3.10.9` (Última disponible a la fecha)

# Instalar y activar ambiente virtual

## Instalación de Anaconda

Disponible a través de [este enlace](https://www.anaconda.com/products/distribution#Downloads)

Antes de proceder es necesario comprobar la instalación y usabilidad de `conda`

## Creación y activación virtualenv

### _Creación_:

`conda create --name fastapi-mysql-restapi python=3`

### _activación_ :

`conda activate fastapi-mysql-restapi`

# Instalación de dependencias

`pip install -r requirements.txt`

Nota: Cuando se instale una nueva dependencia se tiene que dar el siguiente comando: `pip freeze > requirements.txt`
para agregarla al archivo de requerimientos.

Nota 2: Es importante aislar el entorno virtual de los paquetes del espacio del usuario global del sistema, para no
estar inyectándole dependencias innecesarias al proyecto.