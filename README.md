# HyprWall

A modern GTK4 animated wallpaper picker for **Hyprland**, powered by **mpvpaper**.

HyprWall provides a lightweight graphical interface for browsing, previewing and applying animated wallpapers on Hyprland without manually using terminal commands.

> Personal open-source project by Ilham.

---

## ✨ Features

- 🎥 Animated wallpaper support (`.mp4`, `.webm`, `.mkv`)
- 🖼️ Automatic thumbnail generation
- 🖱️ One-click wallpaper switching
- 🔁 Infinite wallpaper looping
- 🚀 Lightweight GTK4 interface
- 📂 Automatic wallpaper detection
- 💻 Designed specifically for Hyprland + mpvpaper

---

## 📸 Preview

> *(Add screenshots here later)*

```
screenshots/main.png
```

---

## 📦 Requirements

Arch Linux / CachyOS

```bash
sudo pacman -S python python-gobject gtk4 libadwaita ffmpeg mpvpaper
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/KendrickMathers/hyprwall-ilham.git
```

Go to the project

```bash
cd hyprwall-ilham
```

Run

```bash
python main.py
```

---

## 📂 Wallpaper Folder

Store your animated wallpapers here

```
~/Pictures/Wallpapers/animated
```

Supported formats

- mp4
- webm
- mkv

Simply copy new wallpapers into the folder.

HyprWall will automatically detect them.

---

## 📁 Project Structure

```
HyprWall/
├── main.py
├── thumbnail.py
├── apply.sh
├── requirements.txt
├── README.md
├── .gitignore
└── thumbnails/
```

---

## 🖼️ Thumbnail Cache

Thumbnails are automatically generated inside

```
thumbnails/
```

This directory is ignored by Git.

---

## 🔄 Backup

Clone the repository

```bash
git clone https://github.com/KendrickMathers/hyprwall-ilham.git
```

Install dependencies

```bash
sudo pacman -S python python-gobject gtk4 libadwaita ffmpeg mpvpaper
```

Run

```bash
python main.py
```

Restore your wallpapers into

```
~/Pictures/Wallpapers/animated
```

---

## 🛣️ Roadmap

- [x] Animated wallpapers
- [x] Automatic thumbnails
- [x] One-click wallpaper switching
- [ ] Search wallpapers
- [ ] Favorites
- [ ] Multi-monitor support
- [ ] Wallpaper preview
- [ ] Settings page
- [ ] Drag & Drop wallpapers

---

## 🤝 Contributing

Contributions, feature requests and bug reports are welcome.

Feel free to open an Issue or Pull Request.

---

## 📄 License

MIT License

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.
