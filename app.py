import streamlit as st

# =========================================================================
# ⚙️ CONFIGURACIÓN DE LA APP ESTILO DUOLINGO
# =========================================================================
st.set_page_config(
    page_title="LogiCode Academy",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Estilo visual limpio y moderno (Tarjetas y tipografía profesional)
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; font-weight: bold; }
    .css-1r6slb0 { background-color: #f0f2f6; border-radius: 15px; padding: 20px; }
    </style>
""", unsafe_allow_html=True)

# =========================================================================
# 🗂️ BASE DE DATOS DE CONTENIDO: ARQUITECTURA MULTIMÓDULO
# =========================================================================
CURRICULUM = {
    1: {
        "etapa": "📦 ETAPA 1: El Analista de Operaciones",
        "titulo": "Módulo 1: Racks y Variables (Tipos de Datos)",
        "teoria": """
        En logística, una **Variable** es el equivalente exacto a una posición física en un rack de almacenamiento. 
        Cada posición tiene una **etiqueta única** (el nombre de la variable) y resguarda un **contenido específico** (el valor del dato).
        
        En el mundo real, los productos tienen distintos atributos y Python los clasifica de forma inteligente:
        * 🔢 **Enteros (int):** Cantidades exactas sin decimales (ej: Unidades en stock: `50`).
        * 📐 **Decimales (float):** Mediciones físicas (ej: Peso del pallet: `420.5` kg).
        * 🔤 **Texto (str):** Identificadores alfanuméricos entre comillas (ej: Código SKU: `"PROD-402"`).
        * ⚖️ **Booleanos (bool):** Estados binarios de Sí o No (ej: ¿Está refrigerado?: `True` o `False`).
        """,
        "codigo_ejemplo": """
# Registro maestro de un pallet ingresando al centro de distribución
sku_producto = "SKU-9921"       # Texto (str)
cantidad_unidades = 144         # Entero (int)
peso_pallet_kg = 520.75         # Decimal (float)
requiere_frio = False           # Booleano (bool)

print(f"Pallet {sku_producto} ingresado con {cantidad_unidades} unidades.")
        """,
        "pregunta": "Estás desarrollando el módulo de recepción de carga. Si necesitas guardar el peso exacto de un contenedor con sus decimales, ¿qué tipo de datos debes utilizar en Python?",
        "opciones": ["Entero (int)", "Decimal / Punto Flotante (float)", "Texto (str)", "Booleano (bool)"],
        "correcta": "Decimal / Punto Flotante (float)",
        "feedback_ok": "🎯 ¡Perfecto! Los datos tipo 'float' permiten almacenar números con fracciones decimales, crucial para balanzas de precisión y cubicaje.",
        "feedback_error": "❌ ¡Casi! Recuerda que el peso suele llevar decimales (ej: 12.5 kg). El tipo 'int' solo guarda números enteros.",
        "puntos_premio": 100
    },
    2: {
        "etapa": "📦 ETAPA 1: El Analista de Operaciones",
        "titulo": "Módulo 2: Semáforos en Bodega (Condicionales `if/else`)",
        "teoria": """
        La toma de decisiones en logística se basa en reglas críticas: *Si pasa X, hacemos Y*. 
        En programación, esto se controla mediante las estructuras **Condicionales (`if`, `elif`, `else`)**.
        
        El sistema evalúa una condición usando operadores lógicos y toma caminos separados según el resultado:
        * El bloque `if` (Si...) comprueba la condición principal.
        * El bloque `elif` (Si no, si...) evalúa condiciones secundarias si la primera falló.
        * El bloque `else` (De lo contrario...) se ejecuta automáticamente si ninguna regla previa se cumplió.
        """,
        "codigo_ejemplo": """
stock_actual = 8
stock_seguridad = 15

if stock_actual <= 0:
    print("🚨 QUIEBRE DE STOCK IRRECUPERABLE. Detener despachos.")
elif stock_actual < stock_seguridad:
    print("⚠️ STOCK BAJO MÍNIMO. Disparar orden de compra automática.")
else:
    print("✅ Inventario óptimo. Operación en verde.")
        """,
        "pregunta": "Basándote en el código de ejemplo superior, si el 'stock_actual' fuera exactamente igual a 0, ¿cuál de las tres alertas se imprimiría en la consola?",
        "opciones": [
            "🚨 QUIEBRE DE STOCK IRRECUPERABLE. Detener despachos.",
            "⚠️ STOCK BAJO MÍNIMO. Disparar orden de compra automática.",
            "✅ Inventario óptimo. Operación en verde."
        ],
        "correcta": "🚨 QUIEBRE DE STOCK IRRECUPERABLE. Detener despachos.",
        "feedback_ok": "🚀 ¡Brillante! Al ser 0, la primera condición (`if stock_actual <= 0`) resulta verdadera, por lo que el sistema ejecuta esa acción de inmediato y no evalúa las siguientes.",
        "feedback_error": "❌ ¡Ojo con el orden de las prioridades! Aunque 0 es menor que el stock de seguridad, Python lee de arriba hacia abajo y se detiene en la primera condición que sea Verdadera.",
        "puntos_premio": 150
    },
    3: {
        "etapa": "🚛 ETAPA 2: El Supervisor de Distribución",
        "titulo": "Módulo 3: Listas de Picking y Bucles (Automatización Masiva)",
        "teoria": """
        Felicidades por llegar a la Etapa de Supervisión. Aquí dejamos de procesar un dato a la vez y empezamos a controlar flujos masivos de operaciones.
        
        Una **Lista** en Python es como un manifiesto de carga o una hoja de ruta de picking: un solo documento ordenado que contiene múltiples elementos.
        Para automatizar la revisión de esta lista sin repetir código, usamos el **Bucle `for`**. Este ciclo actúa como una cinta transportadora automatizada: toma cada elemento de la lista, ejecuta las acciones programadas, y avanza a la siguiente posición de forma autónoma.
        """,
        "codigo_ejemplo": """
# Manifiesto con los SKUs que el operario debe recolectar (Picking)
hoja_picking = ["SKU-A", "SKU-B", "SKU-C", "SKU-D"]

print("⚡ Iniciando Ruta de Picking Optimizada...")
for producto in hoja_picking:
    print(f"📦 Pistoleando y recolectando: {producto}")

print("🏁 Consolidación completada. Pallet listo para andén de despacho.")
        """,
        "pregunta": "Si añadimos un quinto elemento a la lista 'hoja_picking', ¿qué cambio tendríamos que hacer en las líneas de código del bucle 'for' para que procese el nuevo producto?",
        "opciones": [
            "Duplicar las líneas de código dentro del bucle.",
            "Ninguno, el bucle 'for' se adapta dinámicamente al tamaño de la lista.",
            "Cambiar el nombre de la variable 'producto'.",
            "Agregar un condicional 'if' al final."
        ],
        "correcta": "Ninguno, el bucle 'for' se adapta dinámicamente al tamaño de la lista.",
        "feedback_ok": "🏆 ¡Espectacular! Esa es la magia de la automatización industrial en código. No importa si tu manifiesto tiene 4 o 40,000 productos, el bucle se ajusta automáticamente.",
        "feedback_error": "❌ ¡Revisa el concepto de automatización! El propósito del bucle `for` es que no tengas que modificar el algoritmo cuando cambien los datos de entrada.",
        "puntos_premio": 200
    }
}

# =========================================================================
# 🧠 SISTEMA DE MEMORIA (SESSION STATE)
# =========================================================================
if "puntos" not in st.session_state:
    st.session_state.puntos = 0
if "modulo_actual" not in st.session_state:
    st.session_state.modulo_actual = 1
if "respuesta_enviada" not in st.session_state:
    st.session_state.respuesta_enviada = False
if "respuesta_correcta" not in st.session_state:
    st.session_state.respuesta_correcta = False

# =========================================================================
# 👤 BARRA LATERAL (SIDEBAR)
# =========================================================================
with st.sidebar:
    st.markdown("## 📊 Estado de la Carrera")
    st.metric(label="🏆 Puntuación Global", value=f"{st.session_state.puntos} PTS")
    
    total_modulos = len(CURRICULUM)
    progreso_porcentaje = (st.session_state.modulo_actual - 1) / total_modulos
    st.progress(progreso_porcentaje)
    st.caption(f"Has completado el {int(progreso_porcentaje * 100)}% de la malla corporativa.")
    st.markdown("---")
    
    st.markdown("### 🗺️ Tu Ruta de Aprendizaje")
    for mod_id, mod_info in CURRICULUM.items():
        if mod_id < st.session_state.modulo_actual:
            st.markdown(f"✅ **{mod_info['titulo']}**")
        elif mod_id == st.session_state.modulo_actual:
            st.markdown(f"🎯 **{mod_info['titulo']}** *(Nivel Actual)*")
        else:
            st.markdown(f"🔒 *{mod_info['titulo']} (Bloqueado)*")
            
    st.markdown("---")
    if st.sidebar.button("🔄 Reiniciar Academia"):
        st.session_state.puntos = 0
        st.session_state.modulo_actual = 1
        st.session_state.respuesta_enviada = False
        st.session_state.respuesta_correcta = False
        st.rerun()

# =========================================================================
# 🚀 PANTALLA PRINCIPAL
# =========================================================================
current_id = st.session_state.modulo_actual

if current_id > len(CURRICULUM):
    st.balloons()
    st.title("🏆 ¡Graduación de LogiCode Academy!")
    st.markdown(f"""
    ### ¡Felicidades, Líder de Procesos Avanzados!
    Has completado de manera exitosa el entrenamiento intensivo con un puntaje total de **{st.session_state.puntos} PTS**.
    """)
    st.success("💼 Certificación disponible: **Desarrollador de Soluciones Arquitectónicas para Supply Chain**.")
else:
    data = CURRICULUM[current_id]
    st.caption(data["etapa"])
    st.title(data["titulo"])
    
    st.markdown("### 📖 Conceptos y Reglas de Negocio")
    st.info(data["teoria"])
    
    st.markdown("### 🐍 El Código en Entornos de Producción")
    st.code(data["codigo_ejemplo"], language="python")
    st.markdown("---")
    
st.markdown("### 🎯 Laboratorio Práctico - Evaluación por Puntos")
st.markdown(f"**Desafío:** {data['pregunta']}")

opcion_seleccionada = st.radio(
    "Selecciona la respuesta estratégica óptima:",
    data["opciones"],
    index=None,
    disabled=st.session_state.respuesta_enviada
)

if opcion_seleccionada and not st.session_state.respuesta_enviada:
    if st.button("🚀 Enviar Respuesta para Auditoría"):
        st.session_state.respuesta_enviada = True
        if opcion_seleccionada == data["correcta"]:
            st.session_state.respuesta_correcta = True
            st.session_state.puntos += data["puntos_premio"]
        else:
            st.session_state.respuesta_correcta = False
        st.rerun()

if st.session_state.respuesta_enviada:
    if st.session_state.respuesta_correcta:
        st.success(data["feedback_ok"])
        st.markdown(f"➕ **¡Sumaste {data['puntos_premio']} puntos corporativos!**")
        
        if st.button("Evolucionar al Siguiente Módulo ➡️"):
            st.session_state.modulo_actual += 1
            st.session_state.respuesta_enviada = False
            st.session_state.respuesta_correcta = False
            st.rerun()
    else:
        st.error(data["feedback_error"])
        if st.button("🔄 Intentar el Desafío Nuevamente"):
            st.session_state.respuesta_enviada = False
            st.session_state.respuesta_correcta = False
            st.rerun()
