import nox

# vscode complains because nox has been installed with pip3
# the solution was to actually re-create the environment after
# putting nox in with python3 (pip3)

nox.options.sessions = "lint", "tests"


@nox.session(python=["3.8"])  # could list more than one python versions
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.8"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import")
    session.run("flake8", *args)


# This way (with flake8-black and the black session) I can get the warnings
# and if I want I can use black to modify the files
@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
