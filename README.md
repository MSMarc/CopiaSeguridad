# 💾 Copia de Seguridad de Carpetas Personales

Script en Python para realizar una copia de seguridad automatizada en otro disco de múltiples carpetas personales, incluyendo documentos, imágenes y más. Ideal para ejecutarse de forma periódica mediante el **Programador de Tareas de Windows**.

---

## 🧩 Características

- 📁 Copia múltiples carpetas definidas por el usuario
- 🕒 Solo copia archivos nuevos o modificados
- 🗜️ Comprime el backup en un único archivo `.zip`
- 🧼 Elimina archivos temporales tras la compresión
- 🗓️ Mantiene un histórico de todos los backups.

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Sistema Windows (uso de `%USERPROFILE%`)

---

## 🛠 Instalación

1. Clona este repositorio o descarga el código:
   ```bash
   git clone https://github.com/MSMarc/CopiaSeguridad.git
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
3. Renombra el archivo `.env.example` como `.env` y cambia las rutas de carpetas que quieras respaldar y dónde guardar los backups.
4. Crear una tarea programada con el "Programador de tareas" de windows, que lance el script cuando te convenga. Mejor si usas un `.bat`. Recomiendo hacerla cada semana.