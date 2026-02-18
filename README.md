# Focus Toggle for Alfred

Quickly toggle any macOS Focus mode directly from Alfred using Apple Shortcuts.

![Focus Toggle Icon](icon.png)

## Features

- Toggle any Focus mode with a single keyword
- Supports all built-in and custom Focus modes
- Lightweight — no dependencies beyond macOS Shortcuts
- Fuzzy-filtered list so you can type to narrow down Focus modes
- Includes pre-built Shortcuts for Sleep, Do Not Disturb, Gaming, Work, and Reduce Interruptions

## Requirements

- macOS 12 (Monterey) or later
- [Alfred 5](https://www.alfredapp.com/) with Powerpack
- Apple Shortcuts app (included with macOS)

## Installation

### 1. Install the Shortcuts

Pre-built Shortcuts are included in the `shortcuts/` folder. Double-click each one to import into Shortcuts.app:

- `Sleep.shortcut`
- `Do_Not_Disturb.shortcut`
- `Gaming.shortcut`
- `Work.shortcut`
- `Reduce_Interuptions.shortcut`

You can verify they work from the terminal:

```bash
shortcuts list           # See all shortcut names
shortcuts run "Sleep"    # Test a specific shortcut
```

### 2. Install the Workflow

- Download the `.alfredworkflow` file from [Releases](../../releases)
- Double-click to import into Alfred

### 3. Configure Your Focus Modes

Open the workflow in Alfred Preferences and edit the **List Filter**:

1. Double-click the List Filter node
2. Click **+** to add each Focus mode:
   - **Title**: Display name (e.g., `Sleep`)
   - **Arg**: Exact Shortcut name — must match what `shortcuts list` returns (case-sensitive)
3. Optionally add icons for each item — pre-made icons are included in the `icons/` folder, designed to work on both light and dark Alfred themes

## Usage

1. Open Alfred (`⌘ Space` or your hotkey)
2. Type `ft` followed by a space
3. Select a Focus mode from the list or type to filter
4. Press `Enter` to toggle

## How It Works

The workflow passes your selection to a simple bash script:

```bash
/usr/bin/shortcuts run "$1"
```

Alfred's List Filter sends the selected item's `Arg` value, which maps directly to the Shortcut name. The Shortcut then toggles the corresponding Focus mode on or off.

## Adding More Focus Modes

1. Create a new Shortcut in Shortcuts.app with the **Set Focus** action set to **Toggle**
2. Name it to match the Focus mode
3. Add a new entry to the List Filter in Alfred with the **Arg** matching the Shortcut name exactly

## Known Limitations

- **Menu bar notification**: macOS briefly shows a Shortcuts indicator in the menu bar each time a Focus mode is toggled. This is an Apple system behavior and cannot be suppressed.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Couldn't find shortcut" | Run `shortcuts list` and verify the Arg matches the Shortcut name exactly (case-sensitive) |
| Nothing happens on selection | Ensure the List Filter is connected to the Run Script node on the canvas |
| Script doesn't run | Check that Run Script language is `/bin/bash` and uses `$1` (with input as argv) or `{query}` |
| First run prompts for permissions | Grant access when prompted — this only happens once |

## Repository Structure

```
alfred-focus-toggle/
├── README.md
├── icon.png                          # Workflow icon
├── icons/                            # List item icons (light + dark theme compatible)
│   ├── sleep.png
│   ├── dnd.png
│   ├── gaming.png
│   ├── work.png
│   └── reduce-interruptions.png
└── shortcuts/                        # Pre-built Apple Shortcuts
    ├── Sleep.shortcut
    ├── Do_Not_Disturb.shortcut
    ├── Gaming.shortcut
    ├── Work.shortcut
    └── Reduce_Interuptions.shortcut
```

## License

MIT
