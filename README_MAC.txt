BUDDY FOR MAC — BUILD INSTRUCTIONS

This folder is a build kit, not the finished Mac app. GitHub Actions builds Buddy.app for macOS.

ONE-TIME BUILD
1. Sign in to https://github.com/ and create a new repository (for example, buddy-mac). Public or private is fine.
2. Upload all files and folders from this kit to the repository. IMPORTANT: include the hidden .github folder and its workflows/build-mac.yml file.
3. Open the repository's Actions tab. Choose “Build Buddy for macOS” and click “Run workflow” (if it hasn't started automatically after upload).
4. When it finishes, open the workflow run and download the “Buddy-macOS” artifact. Unzip Buddy-macOS.zip to get Buddy.app.

INSTALL ON YOUR MAC
1. Move Buddy.app into your Applications folder.
2. Double-click Buddy.app. Because this is an unsigned app built by GitHub Actions, macOS may block it the first time. If so, Control-click Buddy.app, choose Open, then choose Open again. Only do this for a build you trust.
3. To start it automatically when you sign in: open System Settings > General > Login Items, click + under “Open at Login”, and choose Buddy.app from Applications.
4. Keep Buddy running in the background. Closing a reminder popup does not quit Buddy; use Quit from its Dock menu if you want to stop it.

REMINDERS
Buddy shows a reminder immediately, then cycles through the reminders every 30 minutes while the Mac is awake and Buddy is running. It cannot show local popups while the Mac is shut down or asleep. The first launch may trigger macOS security prompts.

If you need to change or stop automatic launch, remove Buddy from System Settings > General > Login Items.
