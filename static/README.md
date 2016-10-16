# Static Files Directory

Use this directory to store global static files that aren't app specific.
Additionally, any third party library dependencies should be added in the
`packages.json` file rather than downloaded and git added. They'll automatically
be downloaded upon running the app and located in the `node_modules` folder. 
THOU SHALT NOT COMMIT A THIRD PARTY LIBRARY.
