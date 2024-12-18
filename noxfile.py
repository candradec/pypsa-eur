import nox

@nox.session(tags=["style", "fix"])
def black(session):
    session.run("black", "pypsa_eur")

@nox.session(tags=["style", "fix"])
def isort(session):
    session.run("isort", "pypsa_eur")

@nox.session(tags=["style", "fix"])
def flake8(session):
    session.run("flake8", "pypsa_eur")

# @nox.session(tags=["style", "fix"])
# def mypy(session):
#     session.run("mypy", "pypsa_eur", "--check-untyped-defs")

@nox.session(tags=["style", "fix"])
def autopep8(session):
    session.run("autopep8", "pypsa_eur", "--in-place", "-r")

