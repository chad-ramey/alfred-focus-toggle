# Focus Toggle

## Setup

This workflow uses a single Apple Shortcut named **Toggle Focus**.

1. Install the Alfred workflow.
2. Type `focus` in Alfred.
3. If the Shortcut isn’t installed yet, you’ll get a dialog prompt with an **Install Shortcut** button (one-time setup).

That’s it.

## Usage

Toggle macOS Focus modes via the `focus` keyword.

![Selecting a Focus mode](images/focus_toggle.png)

* <kbd>↩︎</kbd> Toggle the selected Focus mode on or off.

Includes pre-built modes for Sleep, Do Not Disturb, Gaming, Work, Reduce Interruptions, and Driving. Add more by editing the List Filter in the workflow and adding an entry with the exact Focus mode name as it appears in System Settings.

Configure the keyword in the Workflow's Configuration.

## Spanish Language Support

A separate **Focus Toggle (Español)** workflow is available for users with macOS set to Spanish. Install `Focus Toggle (Spanish).alfredworkflow` instead of the standard workflow.

Includes pre-built modes using the Spanish names macOS assigns to each built-in Focus mode: Sueño, No molestar, Juegos, Menos interrupciones, Trabajo, and Al volante. Apple's `Set Focus` Shortcut action requires the exact localized name as it appears in System Settings, so the arg and title are identical. Custom Focus modes use whatever name you gave them — add those to the List Filter using that exact name.

## Known Limitations

macOS briefly shows a Shortcuts indicator in the menu bar each time a Focus mode is toggled. This is an Apple system behavior and cannot be suppressed.
