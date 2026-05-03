# Instrucciones para Inteligencia Artificial y Agentes (AGENTS.md)

Este repositorio utiliza **Packwiz** para gestionar un modpack de Minecraft y realiza despliegue continuo (CI/CD) automático a Cloudflare Pages mediante GitHub Actions.

## Herramientas Básicas
- **Añadir un mod oficial:** `packwiz modrinth add <slug>` o `packwiz curseforge add <slug>`
- **Actualizar todos los mods:** `packwiz update --all`
- **Eliminar un mod:** Borra su fichero `.pw.toml` en `mods/` y ejecuta `packwiz refresh`
- **Refrescar Índice:** `packwiz refresh` (¡Obligatorio cada vez que añadas, borres o modifiques algún fichero manualmente en el repositorio!).

## Estructura del Repositorio
- `mods/`: Ficheros `.pw.toml` apuntando a las bases de datos remotas. También admite archivos `.jar` en bruto si no existen en modrinth/curseforge.
- `config/`: Todas las configuraciones personalizadas del servidor y cliente.
- `resourcepacks/`: Texturas (en formato `.zip` y `.pw.toml`).
- `shaderpacks/`: Metadatos del shader.

## ?? CRÍTICO: Saltos de Línea y HASHES (LF vs CRLF) ??
Los archivos generados por packwiz generan sus algoritmos de validación Hash (SHA-256/SHA-1) en base a su contenido en BYTES exactos. 
1. Packwiz e instaladores son incompatibles con conversiones sorpresas de formato por parte de GitHub.
2. NUNCA cambies el `.gitattributes`. Está configurado para declarar `*.toml`, `*.json` y `*.cfg` como ficheros en crudo (`-text`) para prohibir a Git corromperlos al subirlos.
3. Si creas o editas scripts (como en PowerShell), ASEGÚRATE de no introducir terminaciones de Windows (`\r\n`). Todos los archivos de este repo han de mantener la codificación pura en Linux (`\n`) o LF.

## CI/CD Pipeline (Flujo Automatizado)
El proyecto está conectado a **Cloudflare Pages**.
- No tienes que desplegar localmente nunca más usando `wrangler deploy`.
- Basta con confirmar y subir los cambios: `git add .`, `git commit -m "Descripción"` y `git push`.
- GitHub Actions tomará el último `push` y publicará la carpeta raíz `.` completa al CDN en segundos.

## Archivos Personales o Configs Sueltos
Si el humano te pide añadir una textura local en `.zip` o cambiar un JSON de configuración de un mod:
1. Mete el archivo o haz las ediciones pertinentes.
2. Ejecuta *SIEMPRE* `packwiz refresh` antes de añadir a Git. Si olvidas esto, el `index.toml` se quedará obsoleto y el instalador final dará un "Hash Mismatch" crasheando la instalación de los jugadores.
