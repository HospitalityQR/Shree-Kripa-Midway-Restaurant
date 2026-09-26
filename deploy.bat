@echo off
echo ========================================================
echo  SHREE KRIPA MIDWAY - AUTO SAVE ^& DEPLOY TO GITHUB
echo ========================================================
echo.
echo 1. Saving all menu and config changes...
git add -A
git commit -m "Update menu and restaurant details"
echo.
echo 2. Pushing to main branch...
git push -u origin main
echo.
echo 3. Publishing live to gh-pages branch...
git push origin main:gh-pages -f
echo.
echo ========================================================
echo  Deployment complete! Your changes are now LIVE at:
echo  https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/
echo ========================================================
pause
