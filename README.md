# Focus Toggle

## Setup

Install the included Apple Shortcuts from the `shortcuts/` folder by double-clicking each one. These create the toggle actions for each Focus mode.

Verify they are installed by running in the terminal:

```
shortcuts list
```

## Usage

Toggle macOS Focus modes via the `focus` keyword.

![Selecting a Focus mode](images/focus_toggle.png)

* <kbd>↩︎</kbd> Toggle the selected Focus mode on or off.

Includes pre-built shortcuts for Sleep, Do Not Disturb, Gaming, Work, and Reduce Interruptions. Add more by creating a new Shortcut with the **Set Focus** action set to **Toggle**, then adding an entry to the List Filter.

Configure the keyword in the Workflow's Configuration.

## Known Limitations

macOS briefly shows a Shortcuts indicator in the menu bar each time a Focus mode is toggled. This is an Apple system behavior and cannot be suppressed.
