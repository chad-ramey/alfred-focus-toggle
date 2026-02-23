# Focus Toggle

## Setup

This workflow uses a single Apple Shortcut named **Toggle Focus**.

1. Install the Alfred workflow.
2. Run `focus install` in Alfred (one-time setup).
3. Shortcuts.app will open—click **Add Shortcut**.

Verify it’s installed by running:

```sh
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
