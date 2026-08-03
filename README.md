# HyprWall-ilham

A simple GTK4 animated wallpaper picker for Hyprland using **mpvpaper**.

> Personal project by Ilham. Created as a lightweight replacement for Waytrogen with support for animated wallpapers.

---

## ✨ Features

- 🎥 Animated wallpapers (.mp4, .webm, .mkv)
- 🖼️ Automatic thumbnail generation
- 🖱️ One-click wallpaper apply
- 🔁 Infinite video looping
- 🚀 Fast GTK4 interface
- 📁 Automatically detects new wallpapers

---

## 📦 Dependencies

Arch / CachyOS

```bash
sudo pacman -S python python-gobject gtk4 libadwaita ffmpeg mpvpaper
```

---

## 📁 Project Structure

```
HyprWall/
├── main.py
├── thumbnail.py
├── apply.sh
├── requirements.txt
├── .gitignore
├── README.md
└── thumbnails/
```

---

## 📂 Wallpaper Directory

Put all animated wallpapers here:

```
~/Pictures/Wallpapers/animated
```

Supported formats:

- mp4
- webm
- mkv

Simply copy new videos into the folder.

No code changes are required.

---

## ▶️ Run

```bash
cd ~/Projects/HyprWall
python main.py
```

Or, if the desktop launcher has been installed:

```bash
hyprwall
```

---

## 🖼️ Thumbnail Cache

Thumbnails are automatically generated inside:

```
~/Projects/HyprWall/thumbnails
```

This folder is ignored by Git.

---

## 🚀 Backup & Restore

Clone the repository:

```bash
git clone git@github.com:KendrickMathers/hyprwall-ilham.git
```

Install dependencies:

```bash
sudo pacman -S python python-gobject gtk4 libadwaita ffmpeg mpvpaper
```

Run:

```bash
cd hyprwall-ilham
python main.py
```

Finally, restore your animated wallpapers into:

```
~/Pictures/Wallpapers/animated
```

---

## 📌 Notes

- Wallpapers are **not included** in this repository.
- Keep your wallpaper collection backed up separately (Google Drive, OneDrive, external SSD, etc.).
- The application will automatically detect newly added wallpapers.

---

## 📄 License

Personal project for learning and backup purposes.
