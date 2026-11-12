# Kivy starter

A one-button app built with [Kivy](https://kivy.org), ready to run. Everything
it needs, Python and Kivy included, lives in a container, so nothing goes on
your computer but three programs.

## Before you start

Install these once:

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Docker Desktop](https://www.docker.com/products/docker-desktop/), and open
   it so it is running
3. [Git](https://git-scm.com/downloads)

In VS Code, install the **Dev Containers** extension (from the Extensions
view on the left).

## Open it

1. Copy this repository to your own GitHub account, then clone your copy and
   open its folder in VS Code.
2. VS Code asks to **Reopen in Container**. Press it. The first time takes a
   few minutes while it sets up Python and Kivy; after that it opens in
   seconds.

## Run it

1. Press **F5**, or open **Run and Debug** and press **Run my app**.
2. Your app appears in the **Your app's window** tab. If no tab opens, open the
   **Ports** panel, find port 6080, and press the globe icon.
3. Press the button. The words change.

To see a change you made, stop the app (the red square) and run it again.

## Make it yours

`main.py` is the whole app. `Screen` lays out what you see: a `Label` above a
`Button`. `pressed` runs each time the button is pressed. Start there: change
the words, add a second button, or count down instead of up. Kivy's
[documentation](https://kivy.org/doc/stable/) lists every widget you can add.

## License

MIT licensed. See `LICENSE`.
