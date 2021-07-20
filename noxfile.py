# noxfile.py
import nox


@nox.session(python=["3.8"])# could list more than one python versions
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)