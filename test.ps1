poetry run black .
if(!$?) { throw }
poetry run isort .
if(!$?) { throw }
poetry run mypy .
if(!$?) { throw }
poetry run pytest .
if(!$?) { throw }
Write-Host "Done" -ForegroundColor Green

# refer: https://stackoverflow.com/questions/47032005/why-does-a-powershell-script-not-end-when-there-is-a-non-zero-exit-code-using-th
