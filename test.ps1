$ErrorActionPreference = 'Stop'

poetry run black .
if(!$?) { throw }
poetry run isort .
if(!$?) { throw }
poetry run mypy .
if(!$?) { throw }
poetry run pytest .
if(!$?) { throw }
Write-Host "Done" -ForegroundColor Green
