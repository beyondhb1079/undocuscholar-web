# Static Files Directory

## Purpose
This directory is meant to store any global static files as well as any third
party libraries that can't be installed via `npm`. Libraries that can be
installed via `npm` should be added in `package.json` as those will be
automatically downloaded for local development and in the production environment
as well in the node_modules/ directory. THOU SHALT NOT COMMIT A THIRD PARTY 
LIBRARY THAT NPM CAN INSTALL.
