import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Guía de Alimentación Saludable",
    page_icon="🥗",
    layout="wide"
)

# Título principal
st.title("🍎 Guía de Alimentación Saludable Según la Edad")
st.markdown(
    "La alimentación es fundamental para mantener una buena salud, tener energía, "
    "fortalecer los huesos y músculos, y prevenir enfermedades. Aunque las necesidades "
    "nutricionales cambian con la edad, lo ideal es mantener una alimentación "
    "variada, equilibrada y adaptada a las necesidades de cada persona."
)

st.divider()

# Creación de pestañas para organizar el contenido
tab1, tab2, tab3, tab4 = st.tabs([
    "👶 Rango de Edad", 
    "💡 Recomendaciones", 
    "🍽️ Menú Diario", 
    "⚠️ Notas Importantes"
])

with tab1:
    st.header("1. Alimentos recomendados por rango de edad")
    st.markdown("Selecciona tu rango de edad para ver los objetivos y alimentos recomendados:")

    # Diccionario con la información por edad
    edades = {
        "De 10 a 20 años": {
            "objetivo": "Favorecer el crecimiento y el desarrollo.",
            "alimentos": {
                "Proteínas": "Huevos, pollo, pescado, habichuelas y lentejas.",
                "Calcio": "Leche, yogur y queso.",
                "Frutas": "Guineo, mango, naranja y lechosa.",
                "Vegetales": "Zanahoria, brócoli, espinaca y auyama.",
                "Energía": "Arroz, avena, batata, yuca y pan integral.",
                "Grasas saludables": "Aguacate, maní y nueces."
            }
        },
        "De 21 a 30 años": {
            "objetivo": "Mantener la energía y fortalecer músculos y huesos.",
            "alimentos": {
                "Proteínas": "Pescado, pollo, huevos y legumbres.",
                "Carbohidratos": "Avena, arroz, batata y cereales integrales.",
                "Frutas": "Manzana, naranja, piña y guineo.",
                "Vegetales": "Ensaladas verdes, tomate y brócoli.",
                "Grasas saludables": "Aceite de oliva, semillas y aguacate.",
                "Calcio y otros nutrientes": "Yogur natural, leche y alimentos ricos en hierro."
            }
        },
        "De 31 a 40 años": {
            "objetivo": "Conservar la masa muscular y cuidar la salud cardiovascular.",
            "alimentos": {
                "Proteínas": "Pescado, pollo, huevos y habichuelas.",
                "Fibra": "Avena, frutas enteras y vegetales.",
                "Cereales integrales": "Arroz integral y pan integral.",
                "Vegetales": "Espinaca, brócoli, tayota y zanahoria.",
                "Grasas saludables": "Aguacate, semillas y aceite de oliva.",
                "Calcio": "Yogur natural, leche y queso en cantidades moderadas."
            }
        },
        "De 41 a 50 años": {
            "objetivo": "Cuidar el corazón, la presión arterial y el azúcar en la sangre.",
            "alimentos": {
                "Proteínas": "Pescado, pollo sin piel, huevos y legumbres.",
                "Fibra": "Avena, habichuelas, frutas y vegetales.",
                "Grasas saludables": "Aguacate, nueces y aceite de oliva.",
                "Calcio": "Leche, yogur y otros alimentos fortificados.",
                "Alimentos ricos en potasio": "Guineo, aguacate y habichuelas.",
                "Pescado": "Sardinas, salmón y otros pescados ricos en omega-3."
            }
        },
        "De 51 años en adelante": {
            "objetivo": "Preservar los músculos, los huesos, la memoria y la autonomía.",
            "alimentos": {
                "Proteínas": "Pescado, huevos, pollo, yogur y habichuelas.",
                "Calcio y vitamina D": "Lácteos o bebidas fortificadas y otros alimentos adecuados.",
                "Frutas": "Lechosa, naranja, guineo y frutas de temporada.",
                "Vegetales": "Auyama, zanahoria, espinaca y brócoli.",
                "Fibra": "Avena, lentejas, habichuelas y cereales integrales.",
                "Grasas saludables": "Aguacate, semillas y pescado.",
                "Agua": "Beber regularmente, aunque no se sienta mucha sed."
            }
        }
    }

    selected_age = st.selectbox("Elige tu rango de edad:", list(edades.keys()))

    # Mostrar la información del rango seleccionado
    current_data = edades[selected_age]
    st.subheader(f"🎯 Objetivo: {current_data['objetivo']}")
    
    st.markdown("### Alimentos clave:")
    for categoria, items in current_data["alimentos"].items():
        st.markdown(f"- **{categoria}:** {items}")

with tab2:
    st.header("2. Recomendaciones generales para cuidar la salud")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1. Alimentación equilibrada")
        st.write("Incluir frutas, vegetales, proteínas, cereales integrales y legumbres en las comidas diarias.")
        
        st.markdown("#### 2. Beber suficiente agua")
        st.write("Tomar agua durante el día y aumentar su consumo cuando haga calor o se realice actividad física.")
        
        st.markdown("#### 3. Realizar actividad física")
        st.write("Caminar, bailar, montar bicicleta o practicar algún deporte según la edad y condiciones físicas.")
        
    with col2:
        st.markdown("#### 4. Dormir lo suficiente")
        st.write("Mantener horarios regulares de sueño. Los adolescentes necesitan más horas de descanso que la mayoría de los adultos.")
        
        st.markdown("#### 5. Reducir azúcar y sal")
        st.write("Limitar los refrescos, dulces, frituras, embutidos y alimentos ultraprocesados.")
        
        st.markdown("#### 6. Chequeos médicos")
        st.write("Revisar periódicamente la presión arterial, el colesterol, la glucosa y otros indicadores según la edad.")

with tab3:
    st.header("3. Ejemplo de un menú saludable para un día")
    
    st.info("💡 Este es un modelo base que puedes adaptar a tus gustos y necesidades.")

    menu = {
        "🌅 Desayuno": "Avena con leche o yogur, una fruta y agua.",
        "☀️ Almuerzo": "Arroz, habichuelas, pollo guisado o pescado y ensalada.",
        "🍎 Merienda": "Una fruta, yogur natural o un puñado de frutos secos, según las necesidades.",
        "🌙 Cena": "Pescado o huevos con vegetales y batata hervida."
    }

    for tiempo, desc in menu.items():
        with st.expander(tiempo):
            st.write(desc)

with tab4:
    st.header("4. Recomendaciones importantes y Conclusión")
    
    st.warning(
        "**Puntos clave a tener en cuenta:**\n"
        "- La edad por sí sola no determina la dieta ideal; también influyen la actividad física, el embarazo, las enfermedades y las necesidades individuales.\n"
        "- Las personas con diabetes, hipertensión o enfermedad renal deben adaptar su alimentación con orientación profesional.\n"
        "- No es necesario comprar alimentos costosos: el arroz, las habichuelas, los huevos, la avena, las frutas de temporada y los vegetales locales son excelentes opciones.\n"
        "- A partir de los 50 años conviene prestar especial atención a la conservación de la masa muscular, la salud ósea y la hidratación."
    )
    
    st.success(
        "**Conclusión:** Una buena alimentación, acompañada de ejercicio, descanso y chequeos médicos, "
        "ayuda a cuidar la salud en todas las etapas de la vida. La clave es elegir alimentos variados "
        "y adaptar las porciones y los nutrientes a las necesidades de cada persona."
    )
