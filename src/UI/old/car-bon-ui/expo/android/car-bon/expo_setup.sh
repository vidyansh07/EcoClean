# expo setup
# replace <user> with Windows user
# add andorid tp path
echo -e "\n# Android\nexport ANDROID_HOME=/mnt/c/Users/<user>/AppData/Local/Android/Sdk\nexport WSLENV=ANDROID_HOME/p" >> $HOME/.bashrc && source $HOME/.bashrc
# alternate path for adb
sudo cp /mnt/c/Users/<user>/AppData/Local/Android/sdk/platform-tools/adb.exe /mnt/c/Users/<user>/AppData/Local/Android/sdk/platform-tools/adb