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

The Alfred list shows Spanish display names (`Modo de descanso`, `No molestar`, etc.), but passes the English internal name to the Shortcut — which is what Apple's `Set Focus` action requires regardless of system language. Custom Focus modes (modes you created yourself) use whatever name you gave them; add those to the List Filter using that exact name.

Built-in mode name mapping:

| Alfred (español) | Shortcut input (English) |
|---|---|
| Modo de descanso | Sleep |
| No molestar | Do Not Disturb |
| Modo de juego | Gaming |
| Reducir interrupciones | Reduce Interruptions |
| Modo de trabajo | Work |
| Modo de conducción | Driving |

## Known Limitations

macOS briefly shows a Shortcuts indicator in the menu bar each time a Focus mode is toggled. This is an Apple system behavior and cannot be suppressed.
