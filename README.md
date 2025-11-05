# 🎨 Qtile Configuration - Personal Setup

Una configuración moderna y optimizada de [Qtile](https://github.com/qtile/qtile), un window manager dinámico para Linux escrito en Python. Esta configuración está diseñada para ser eficiente, visualmente atractiva y altamente funcional.

![Qtile](https://img.shields.io/badge/Qtile-0.20+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Características

### 🚀 Performance Optimizado
- **Intervalos de widgets optimizados** - Reducción del 40-50% en carga de CPU
- **Cache de interfaz de red** - Evita llamadas repetidas a `psutil`
- **Autostart no bloqueante** - Inicio más rápido usando `subprocess`
- **Widgets inteligentes** - Actualización basada en importancia y frecuencia

### 🎨 Diseño Moderno
- **8 temas predefinidos** - Gruvbox, Dracula, Nord, Solarized, One Dark, Ayu Dark, Catppuccin, Tokyo Night
- **Sistema de colores consistente** - Organizado por categorías (red, sistema, media, estado)
- **Iconos Nerd Font** - Iconografía moderna y legible
- **Layouts personalizables** - MonadTall, MonadWide, BSP, Matrix, RatioTile, Max

### 📦 Widgets Complejos
- **Email (IMAP)** - Monitoreo de correo con notificaciones
- **Sistema** - CPU, Memoria, Disco, Batería
- **Red** - WiFi/Ethernet con detección automática
- **Multimedia** - Volumen, Brillo, Bluetooth
- **Estado** - Actualizaciones de sistema, Layout actual, Teclado

### 🛠️ Funcionalidades Avanzadas
- **Scratchpads** - Terminal, Calculadora y Notas flotantes
- **Multi-monitor** - Soporte automático con barras personalizadas
- **Gestión de sesión** - Menú rofi para shutdown, reboot, lock, logout
- **Atajos de teclado extensos** - Navegación eficiente y lanzamiento rápido de apps

## 📋 Requisitos

### Dependencias Principales
- **Qtile** - Window manager base
- **Python 3.8+** - Para ejecutar la configuración
- **Picom** - Compositor para efectos visuales
- **Rofi** - Lanzador de aplicaciones
- **Feh** - Gestor de fondos de pantalla

### Dependencias de Python
```bash
pip install psutil keyring
```

### Dependencias del Sistema (Arch Linux)
```bash
sudo pacman -S qtile picom rofi feh brightnessctl \
    kitty brave thunar vim scrot \
    light-locker-command zenity evolution \
    blueman-manager galculator mousepad
```

### Fuentes
- **Hack Nerd Font** - Fuente principal con iconos

```bash
# Instalar desde AUR
yay -S nerd-fonts-hack
```

## 🚀 Instalación

### Método 1: Clonar el Repositorio

```bash
# Hacer backup de tu configuración actual (si existe)
mv ~/.config/qtile ~/.config/qtile.backup

# Clonar este repositorio
git clone https://github.com/tu-usuario/qtile-config.git ~/.config/qtile

# Instalar dependencias de Python
pip install --user psutil keyring
```

### Método 2: Instalación Manual

1. Copia todos los archivos a `~/.config/qtile/`
2. Asegúrate de que los permisos de ejecución están correctos:
   ```bash
   chmod +x ~/.config/qtile/config.py
   chmod +x ~/.config/qtile/scripts/session_menu.sh
   ```
3. Instala las dependencias necesarias

### Configurar Variables de Entorno (.env)

Esta configuración usa un archivo `.env` para datos sensibles y personalizaciones. **Es importante configurarlo antes de usar Qtile**.

1. **Copia el archivo de ejemplo:**
   ```bash
   cp ~/.config/qtile/env.example ~/.config/qtile/.env
   ```

2. **Edita el archivo `.env` con tus datos:**
   ```bash
   nano ~/.config/qtile/.env
   ```

3. **Configuración mínima requerida:**
   - `QTILE_CONFIG_PATH`: Ruta de tu configuración (ajusta a tu usuario)
   - `EMAIL_USER`, `EMAIL_SERVER`: Si quieres usar el widget de email
   - `BACKLIGHT_NAME`, `DISK_DEVICE`: Ajusta según tu hardware

4. **Configurar Email (Opcional):**
   
   Primero configura las variables en `.env`:
   ```
   EMAIL_USER=tu-email@ejemplo.com
   EMAIL_SERVER=mail.ejemplo.com
   EMAIL_KEYRING_SERVICE=mail.ejemplo.com
   ```
   
   Luego guarda la contraseña en keyring:
   ```bash
   python -c "import keyring; keyring.set_password('mail.ejemplo.com', 'tu-email@ejemplo.com', 'tu-contraseña')"
   ```

**Nota**: El archivo `.env` está en `.gitignore` y NO se subirá a git. Es seguro para guardar datos sensibles.

## ⌨️ Atajos de Teclado

### Navegación
| Atajo | Acción |
|-------|--------|
| `Super + h/j/k/l` | Navegar entre ventanas |
| `Super + Shift + h/j/k/l` | Mover ventana |
| `Super + Ctrl + h/j/k/l` | Redimensionar ventana |
| `Super + Space` | Cambiar foco entre ventanas |
| `Super + Tab` | Cambiar layout |
| `Super + w` | Cerrar ventana |

### Aplicaciones
| Atajo | Acción |
|-------|--------|
| `Super + Return` | Terminal (kitty) |
| `Super + b` | Navegador (brave) |
| `Super + e` | Explorador de archivos (thunar) |
| `Super + m` | Menú de aplicaciones (rofi) |
| `Super + Ctrl + m` | Menú de ventanas (rofi) |
| `Super + v` | Editor de texto (vim) |
| `Super + s` | Captura de pantalla |

### Scratchpads
| Atajo | Acción |
|-------|--------|
| `Super + y` | Terminal flotante |
| `Super + u` | Calculadora |
| `Super + i` | Notas (mousepad) |

### Grupos de Trabajo
| Atajo | Acción |
|-------|--------|
| `Super + 1-9` | Cambiar a grupo |
| `Super + Shift + 1-9` | Mover ventana a grupo |

### Sistema
| Atajo | Acción |
|-------|--------|
| `Super + x` | Menú de sesión |
| `Super + Ctrl + r` | Recargar configuración |
| `Super + Ctrl + q` | Cerrar Qtile |
| `Super + r` | Ejecutar comando |
| `Super + f` | Pantalla completa |
| `Super + t` | Ventana flotante |

### Hardware
| Atajo | Acción |
|-------|--------|
| `XF86AudioMute` | Silenciar/Activar audio |
| `XF86AudioLowerVolume` | Bajar volumen |
| `XF86AudioRaiseVolume` | Subir volumen |
| `XF86MonBrightnessUp` | Aumentar brillo |
| `XF86MonBrightnessDown` | Disminuir brillo |

## 🎨 Temas Disponibles

La configuración incluye 8 temas predefinidos:

1. **Catppuccin** (default) - Moderno y suave
2. **Gruvbox** - Tono cálido y acogedor
3. **Dracula** - Oscuro y vibrante
4. **Nord** - Frío y minimalista
5. **Solarized Dark** - Clásico y legible
6. **One Dark** - Inspirado en Atom
7. **Ayu Dark** - Profesional y elegante
8. **Tokyo Night** - Nocturno y moderno

### Cambiar Tema

Edita `~/.config/qtile/.theme` y escribe el nombre del tema:

```bash
echo "dracula" > ~/.config/qtile/.theme
```

Luego recarga la configuración: `Super + Ctrl + r`

### Activar Tema Aleatorio

En `src/config.py`, cambia:
```python
_use_random_theme = True
```

## 📁 Estructura del Proyecto

```
qtile/
├── config.py              # Archivo principal de configuración
├── env.example            # Plantilla de variables de entorno
├── .env                   # Variables de entorno (NO se sube a git)
├── .gitignore             # Archivos ignorados por git
├── actions.md             # Lista de ideas y mejoras
├── MEJORAS.md            # Documentación de mejoras implementadas
├── README.md             # Este archivo
├── scripts/
│   └── session_menu.sh   # Script de menú de sesión
└── src/
    ├── app_rules.py      # Reglas para asignar apps a grupos
    ├── autostart.py      # Aplicaciones al inicio
    ├── colors.py         # Paletas de colores
    ├── config.py         # Configuración base (mod, terminal, etc.)
    ├── functions.py      # Funciones auxiliares
    ├── groups.py         # Grupos de trabajo y scratchpads
    ├── keys.py           # Atajos de teclado
    ├── layouts.py        # Layouts de ventanas
    ├── screens.py        # Configuración de pantallas
    ├── status_bar.py     # (Reservado para futuras mejoras)
    └── widgets.py        # Widgets de la barra de estado
```

### Variables de Entorno (.env)

El archivo `.env` contiene todas las configuraciones sensibles y personalizables:

- **Email**: Credenciales para el widget IMAP
- **Paths**: Rutas de configuración, screenshots, wallpapers
- **Aplicaciones**: Terminal, navegador, editor, etc.
- **Hardware**: Backlight, disco, interfaz de red
- **Tema**: Tema por defecto y configuración aleatoria
- **Display**: Configuración de monitores (xrandr)
- **Sesión**: Comando de bloqueo de pantalla

Ver `env.example` para todas las opciones disponibles.

## 🔧 Personalización

### Cambiar Aplicaciones por Defecto

**Método recomendado**: Edita el archivo `.env`:

```bash
TERMINAL=alacritty
BROWSER=firefox
FILE_MANAGER=nautilus
EDITOR=code
EMAIL_CLIENT=thunderbird
```

**Alternativa**: También puedes editar `src/config.py` directamente, pero usar `.env` es más limpio y seguro.

### Reglas de Aplicaciones (Asignar a Grupos)

Las aplicaciones se pueden asignar automáticamente a grupos específicos cuando se abren. Esto se configura en `src/app_rules.py`.

**Cómo funciona:**
- Cuando abres una aplicación, Qtile busca su `wm_class`
- Si hay una regla definida, la aplicación se mueve automáticamente al grupo correspondiente
- También cambia automáticamente a ese grupo

**Para encontrar el wm_class de una aplicación:**
```bash
xprop WM_CLASS
# Haz click en la ventana de la aplicación
```

**Para configurar reglas:**
Edita `src/app_rules.py` y agrega tu aplicación al diccionario `app_rules`:

```python
app_rules = {
    'brave': '2',           # Brave en grupo 2
    'Sublime_text': '3',   # Sublime Text en grupo 3
    'code': '3',            # VS Code en grupo 3
    # ... más aplicaciones
}
```

**Grupos disponibles:** 1-9 (corresponden a `Super+1` a `Super+9`)

**Ejemplos preconfigurados:**
- Navegadores → Grupo 2
- Editores de código → Grupo 3
- Terminales → Grupo 1
- Gestores de archivos → Grupo 4
- Multimedia → Grupo 5
- Office → Grupo 6
- Email → Grupo 7
- Chat → Grupo 8

### Modificar Widgets

Edita `src/widgets.py` para personalizar widgets:
- Agregar/quitar widgets
- Cambiar colores y estilos
- Ajustar intervalos de actualización

### Personalizar Layouts

Edita `src/layouts.py` para:
- Cambiar gaps entre ventanas
- Modificar colores de bordes
- Agregar/quitar layouts

## 🐛 Solución de Problemas

### La barra no aparece
- Verifica que Qtile esté ejecutándose: `qtile check`
- Recarga la configuración: `Super + Ctrl + r`
- Verifica que el archivo `.env` existe y está bien configurado

### Widgets no funcionan
- Verifica dependencias: `pip list | grep psutil`
- Revisa logs: `tail -f ~/.local/share/qtile/qtile.log`
- Verifica que las variables en `.env` estén correctas

### Widget de email no aparece
- Verifica que `EMAIL_USER` y `EMAIL_SERVER` estén configurados en `.env`
- Asegúrate de haber configurado la contraseña en keyring
- Si no quieres usar email, el widget se ocultará automáticamente

### Tema no cambia
- Verifica que el archivo `.theme` existe
- O configura `DEFAULT_THEME` en `.env`
- Asegúrate de recargar la configuración después de cambiar

### Error cargando .env
- Verifica que el archivo `.env` tenga formato correcto (clave=valor)
- No debe haber espacios alrededor del `=`
- Comentarios deben empezar con `#`

### Interfaz de red incorrecta
- Limpia el cache: Importa `clear_network_cache()` desde `src.functions`
- O reinicia Qtile

## 📊 Performance

Esta configuración está optimizada para:
- **40-50% menos carga de CPU** en widgets
- **Inicio más rápido** con autostart no bloqueante
- **Menor uso de memoria** con cache inteligente
- **Actualizaciones eficientes** según importancia

Ver [MEJORAS.md](MEJORAS.md) para detalles técnicos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Siéntete libre de:
- Reportar bugs
- Sugerir mejoras
- Enviar pull requests

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usar, modificar y distribuir.

## 🙏 Créditos

- [Qtile](https://github.com/qtile/qtile) - El window manager base
- [Nerd Fonts](https://www.nerdfonts.com/) - Iconografía
- Comunidad de r/qtile - Inspiración y ayuda

## 📸 Screenshots

> **Nota**: Agrega screenshots de tu configuración aquí para mostrar cómo se ve.

## 🔗 Enlaces Útiles

- [Documentación de Qtile](https://docs.qtile.org/)
- [Configuraciones de la Comunidad](https://github.com/qtile/qtile/wiki/Configs)
- [Wiki de Qtile](https://github.com/qtile/qtile/wiki)

---

⭐ Si te gusta esta configuración, considera darle una estrella en GitHub!

