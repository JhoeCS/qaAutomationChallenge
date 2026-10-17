# QA Automation Challenge

Proyecto de automatización de pruebas para los requerimientos de Registro y Login.

## Arquitectura del Proyecto

El proyecto está diseñado bajo una arquitectura modular y escalable, manteniendo una separación estricta entre pruebas de servicios y pruebas de interfaz de usuario:

```text
qaAutomationChallenge/
├── api/
│   └── test_auth_api.py       # Pruebas automatizadas de API REST con Requests
├── web/
│   ├── pages/                 # Page Object Model
│   │   ├── register_page.py   # Selectores y acciones de Registro
│   │   └── login_page.py      # Selectores y acciones de Login
│   └── test_auth_web.py       # Pruebas de interfaz de usuario con Playwright
├── conftest.py                # Fixtures y configuración global de pytest
├── requirements.txt           # Dependencias necesarias
└── README.md                  # Documentación de instalación y ejecución
```

## Tecnologías Utilizadas

* **Python 3:** Lenguaje principal del proyecto.
* **pytest:** Ejecutor de pruebas, aserciones y configuración de fixtures.
* **Requests:** Cliente HTTP para validación directa de APIs REST.
* **Playwright con Python:** Automatización web para validaciones de interfaz y flujos de usuario.
* **Page Object Model:** Patrón de diseño para desacoplar la estructura de la página de la lógica de las pruebas.

## Requisitos Previos

1. Instalar las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```

2. Si es la primera vez que se utiliza Playwright en el entorno, descargar los navegadores:
   ```bash
   playwright install chromium
   ```

3. Tener en ejecución los servicios de la aplicación bajo prueba:
   * Backend en puerto 3000: `http://localhost:3000`
   * Frontend en puerto 4000: `http://localhost:4000`

## Ejecución de Pruebas

Para ejecutar las pruebas desde la carpeta raíz del proyecto qaAutomationChallenge, utilizar los siguientes comandos:

### 1. Ejecutar solo las pruebas de API
```bash
pytest api/ -v
```

### 2. Ejecutar solo las pruebas Web
```bash
pytest web/ -v
```

### 3. Ejecutar toda la suite de regresión
```bash
pytest -v
```

## Cobertura de Casos Automatizados

Se automatizaron los escenarios clave definidos en la matriz de pruebas del Reto 1:

* **TC-REG-01 y TC-LOG-01:** Flujo exitoso con datos válidos.
* **TC-REG-02 y TC-LOG-02:** Valor límite inferior de 5 caracteres en contraseña.
* **TC-REG-03 y TC-LOG-03:** Contraseña menor al límite con 4 caracteres.
* **TC-REG-04 y TC-LOG-04:** Formato de correo inválido sin arroba.
* **TC-REG-05 y TC-LOG-05:** Campos obligatorios vacíos.
