# features/environment.py
from playwright.sync_api import sync_playwright
import os

def before_all(context):
    # Esto es como el setup del Suite
    # Creamos una carpeta para evidencias si no existe
    if not os.path.exists("evidence"):
        os.makedirs("evidence")

def before_scenario(context, scenario):
    # Setup del navegador (Antes de cada @Test)
    context.pw = sync_playwright().start()
    context.browser = context.pw.chromium.launch(headless=True)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Manejo de errores (Teardown)
    if scenario.status == "failed":
        # Si la prueba falló, guardamos evidencia automáticamente
        screenshot_path = f"evidence/{scenario.name.replace(' ', '_')}.png"
        context.page.screenshot(path=screenshot_path)
        print(f"Error detectado. Screenshot guardado en: {screenshot_path}")

    # Limpieza de procesos
    context.browser.close()
    context.pw.stop()