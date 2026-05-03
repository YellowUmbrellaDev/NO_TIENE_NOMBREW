# NO TIENE NOMBREW - Modpack

Modpack gestionado a través de [Packwiz](https://packwiz.infra.link/) y alojado globalmente mediante Cloudflare Pages y Github Actions para asegurar descargas limpias, automáticas y ultra-rápidas en todo el mundo.

## ?? Instalación Automática (Jugadores vía Prism Launcher)

No necesitas bajarte el modpack entero a mano, usa este instalador que te mantendrá los archivos sincronizados automáticamente:

1. Crea una **Nueva Instancia** en Prism Launcher.
   - Versión de Minecraft: **1.21.1**
   - Modloader: **NeoForge 21.1.228**
2. Haz clic derecho en tu instancia nueva y elige "Abrir carpeta" para entrar en el directorio base (suerte llamarse `.minecraft` o `minecraft`).
3. Descarga el archivo **[packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar)** y mételo justo ahí, dentro de esa carpeta.
4. En Prism Launcher, entra a **Editar Instancia** -> Pestaña **Configuración** -> Apartado **Comandos personalizados**.
5. Marca la casilla de "Activar comandos" y en la barra de texto de **Pre-launch command**, copia y pega *exactamente* esto:

`"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://no-tiene-nombrew-packwiz.pages.dev/pack.toml`

6. **¡Arranca el juego!** 
Verás que el instalador procesa, baja e instala mágicamente todo: texturas custom, configs de menú, todos los mods necesarios y parches. Cada vez que inicias el juego se encargará de revisarlo de manera inteligente y si hay actualizaciones, se bajarán solas antes de la pantalla de Mojang.

## ?? Desarrollo y Repositorio (Developers)
Cualquier subida o modificación del modpack hecha a la rama `main` en GitHub, invocará automáticamente a una *GitHub Action* que sincroniza todo con Cloudflare en milisegundos.
