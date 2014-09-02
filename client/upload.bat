@echo off
curl -i -F "fileselect=@%1" http://mail4.isurveylink.com:65523/upload/

echo \ndownload url:
echo http://mail4.isurveylink.com:65523/uploads/%1