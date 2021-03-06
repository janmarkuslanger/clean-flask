# clean-flask
Kickstart your next flask project with clean-flask. Clean-Flask is a template which bundles a few vital components when it comes to modern web applications.

## What do you get

**Flask**
<br>Flask is a super lightweight framework for web servers.

**SQLAlchemy**
<br>SQLAlchemy is an Object-Relational-Mapper that supports SQLite, MySql, and much more.

**webpack**
<br>Webpack is a bundler for your stylesheets and javascript. It comes with babel and some other neat packages like an autoprefixer for your scss files.

**scss**
SCSS is a super cool preprocessor for your stylesheets.

**eslint**
<br>Lints your javascript files.

**login**
<br>This template comes with a simple, not safe login.

## Get started

Clone or download this repository. Start your terminal and move into the root of this repository.

**Backend**
1. Create a virtual env `python3 -m venv venv`
2. Install dependencies `pip3 install -r requirements.txt`
3. Create DB `python3 db_setup.py`
4. Create demo user `python3 demo_data.py`
5. Run server `python3 run.py`

**Frontend**
1. Install packages `npm i`
2. Start bundler `npm run watch`

## Commands

- `npm run lint-js` - Lints your javascript files via eslint
- `npm run watch` - Start webpack and watch files
- `npm run build` - Build your assets files once
- `flake8 app` - Lint your python files via flake8
