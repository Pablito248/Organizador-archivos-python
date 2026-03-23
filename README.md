# Python File Organizer / Organizador de Archivos en Python

*Read this document in English or Spanish below.*

---

## English Version

A lightweight Python utility that scans a working directory, dynamically creates sub-folders based on file types, and safely moves files to keep your workspace clean.

### Features
* Automatic Sorting: Detects file extensions automatically and creates corresponding folders (e.g., pdf, jpg, txt).
* Safe Execution: The script includes a failsafe to prevent it from moving or organizing itself.
* Global Command (Windows): Can be configured to run from any directory using a simple custom command in the terminal.

### Prerequisites
* Python 3.x installed on your system.
* Standard Python libraries used (os, shutil), so no external dependencies are required.

### How to Use

#### Option 1: Direct Execution
1. Open your terminal or command prompt.
2. Navigate to the messy folder you want to organize:
   cd path/to/your/messy/folder
3. Run the script by providing its absolute path:
   python "C:\Path\To\Your\Script\organizador.py"

#### Option 2: Global Command (Windows Setup)
If you want to organize any folder by simply typing the command 'organizar' in your terminal, follow these steps:
1. Create a file named 'organizar.bat' in the same directory as your Python script with the following code:
   @echo off
   python "C:\Path\To\Your\Script\organizador.py"
2. Open the Windows Start Menu and search for "Environment Variables".
3. Click on "Edit the system environment variables" and find the "Path" variable.
4. Add the absolute path to the folder containing your .bat and .py files.
5. Restart your terminal. Now you can navigate to any folder and simply type 'organizar' to clean it up!

---

## Versión en Español

Una utilidad ligera en Python que escanea un directorio de trabajo, crea subcarpetas dinámicamente basándose en los tipos de archivo y mueve los archivos de forma segura para mantener tu espacio de trabajo limpio.

### Características
* Clasificación automática: Detecta automáticamente las extensiones de los archivos y crea las carpetas correspondientes (ej. pdf, jpg, txt).
* Ejecución segura: El script incluye una medida de seguridad para evitar moverse u organizarse a sí mismo.
* Comando global (Windows): Puede configurarse para ejecutarse desde cualquier directorio usando un comando personalizado simple en la terminal.

### Requisitos
* Python 3.x instalado en tu sistema.
* Utiliza librerías estándar de Python (os, shutil), por lo que no requiere dependencias externas.

### Cómo usar

#### Opción 1: Ejecución directa
1. Abre tu terminal o símbolo del sistema.
2. Navega a la carpeta desordenada que quieres organizar:
   cd ruta/a/tu/carpeta/desordenada
3. Ejecuta el script proporcionando su ruta absoluta:
   python "C:\Ruta\A\Tu\Script\organizador.py"

#### Opción 2: Comando global (Configuración en Windows)
Si quieres organizar cualquier carpeta simplemente escribiendo el comando 'organizar' en tu terminal, sigue estos pasos:
1. Crea un archivo llamado 'organizar.bat' en el mismo directorio que tu script de Python con el siguiente código:
   @echo off
   python "C:\Ruta\A\Tu\Script\organizador.py"
2. Abre el menú de inicio de Windows y busca "Variables de entorno".
3. Haz clic en "Editar las variables de entorno del sistema" y busca la variable "Path".
4. Agrega la ruta absoluta a la carpeta que contiene tus archivos .bat y .py.
5. Reinicia tu terminal. ¡Ahora puedes navegar a cualquier carpeta y simplemente escribir 'organizar' para limpiarla!

---

**Author / Autor:** [Pablito248] - V1.0