# NO TIENE NOMBREW - Modpack

Modpack gestionado a trav�s de [Packwiz](https://packwiz.infra.link/) y alojado globalmente mediante Cloudflare Pages y Github Actions para asegurar descargas limpias, autom�ticas y ultra-r�pidas en todo el mundo.

## ?? Instalaci�n Autom�tica (Jugadores v�a Prism Launcher)

No necesitas bajarte el modpack entero a mano, usa este instalador que te mantendr� los archivos sincronizados autom�ticamente:

1. Crea una **Nueva Instancia** en Prism Launcher.
   - Versi�n de Minecraft: **1.21.1**
   - Modloader: **NeoForge 21.1.228**
2. Haz clic derecho en tu instancia nueva y elige "Abrir carpeta" para entrar en el directorio base (suerte llamarse `.minecraft` o `minecraft`).
3. Descarga el archivo **[packwiz-installer-bootstrap.jar](https://github.com/packwiz/packwiz-installer-bootstrap/releases/latest/download/packwiz-installer-bootstrap.jar)** y m�telo justo ah�, dentro de esa carpeta.
4. En Prism Launcher, entra a **Editar Instancia** -> Pesta�a **Configuraci�n** -> Apartado **Comandos personalizados**.
5. Marca la casilla de "Activar comandos" y en la barra de texto de **Pre-launch command**, copia y pega *exactamente* esto:

`"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://no-tiene-nombrew-packwiz.pages.dev/pack.toml`

6. **�Arranca el juego!** 
Ver�s que el instalador procesa, baja e instala m�gicamente todo: texturas custom, configs de men�, todos los mods necesarios y parches. Cada vez que inicias el juego se encargar� de revisarlo de manera inteligente y si hay actualizaciones, se bajar�n solas antes de la pantalla de Mojang.

## ?? Desarrollo y Repositorio (Developers)
Cualquier subida o modificaci�n del modpack hecha a la rama `main` en GitHub, invocar� autom�ticamente a una *GitHub Action* que sincroniza todo con Cloudflare en milisegundos.
