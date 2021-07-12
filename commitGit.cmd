rem "Daily git commit" 
git pull
git add --all
git commit -am "Changed file Commit."
git push -u origin main
git pull
set /p DUMMY=Hit ENTER to continue...
exit