# CAI-3 CONSULTARIA DE ASEGURAMIENTO DE LA INFORMACION 3

# Confidencialidad en el Almacenamiento de Información para Entidad Hospitalaria  
**Equipo:** secTeam 12 - INSEGUS  
**Fecha:** 4 Marzo 2025  

## Descripción del Proyecto  

Descripción del Proyecto
Este proyecto tiene como objetivo evaluar y garantizar la confidencialidad en el almacenamiento de información sensible para una gran entidad hospitalaria. El cliente gestiona un centro de diagnóstico por imagen que incluye tecnologías como radiología digital, gammagrafía, tomografía por emisión de positrones (PET), tomografías computarizadas, pruebas de medicina nuclear, resonancia magnética y ecografías. Los resultados de estas pruebas se almacenan digitalmente y requieren un enfoque robusto para proteger la privacidad y seguridad de los datos de los pacientes.

## Infraestructura Actual  
- **Almacenamiento Principal:** Sistema NAS (Network Attached Storage) con capacidad de 4 TB, ubicado físicamente en diferentes edificios del complejo hospitalario.  
- **Transmisión de Datos:** Las imágenes se envían al NAS mediante el protocolo **TLS v1.3**, garantizando una comunicación segura.  
- **Eliminación en Origen:** Los dispositivos de diagnóstico no retienen información; las imágenes se destruyen de forma segura tras ser enviadas.  
- **Red:** Todos los equipos y el NAS están conectados a una **VLAN** dedicada.  
- **Copia de Seguridad:** Un segundo NAS en la misma VLAN almacena respaldos diarios de los datos generados cada jornada laboral.  

## Objetivos del secTeam 12  
1. **Evaluación de Seguridad:** Analizar la configuración actual del sistema para identificar posibles vulnerabilidades.  
2. **Confidencialidad:** Asegurar que los datos cumplen con estándares de privacidad y normativas aplicables (ej. GDPR, HIPAA).  
3. **Propuestas de Mejora:** Diseñar e implementar medidas para fortalecer la protección de la información en el NAS y las copias de seguridad.  
4. **Documentación:** Proveer un informe detallado con hallazgos y recomendaciones.  

## Tecnologías y Herramientas  
- **Protocolo TLS 1.3:** Transmisión segura de datos.  
- **NAS:** Almacenamiento en red como base de la infraestructura.  
- **VLAN:** Red dedicada para aislar el tráfico sensible.  
- **Análisis de Seguridad:** Herramientas de auditoría y monitoreo (por definir).  

 

