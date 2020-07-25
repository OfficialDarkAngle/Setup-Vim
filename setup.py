#-*- coding: utf-8 -*

import os,sys,time,random

'''

tool ini tersedia open source

jadi bisa kalian pelajari

tapi mohon jika merecode tempelkan sumbernya

jika tidak itu melanggar hak cipta

Date: 25-07-2020

'''

import os

def instal():

    # Install Package

    os.system('pkg install vim')

    os.system('pkg install git')

    os.system('git clone https://github.com/VundleVim/Vundle.vim')

    # Move Folder

    os.system('mkdir ~/.vim')

    os.system('mkdir ~/.vim/bundle')

    os.system('cp -r Vundle.vim ~/.vim/bundle')

    os.system('rm /data/data/com.termux/files/usr/share/vim/vimrc')

    os.system('cp vimrc /data/data/com.termux/files/usr/share/vim/vimrc')

    # Langkah selanjutnya

    print('\n')

    print('     '+'+'*33)

    print("     * Masuklah ke vim Anda lalu masukan perintah ':PluginInstall'")

    print('\n')

    print('     * Jika kurang mengerti silakan hubungi Saya')

    print('     * 6282125068665 (hanya wa)')

def mengetik(s):

    os.system("clear")

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(random.random() * 0.1)

mengetik('  ▼￣＞-―-＜￣▼       ~  ~  ~   ┌∩┐(◣_◢)┌∩┐   ~  ~  ~\n   Ｙ       Ｙ    ╔╦╗╔═╗╦═╗╔╦╗╦ ╦═╗ ╦\n/\ /   ●  ω ●）    ║ ╠╣ ╠╦╝║║║║ ║╔╩╦╝ <•>\n\ ｜　 つ　  ヽつ  ╩ ╚═╝╩╚═╩ ╩╚═╝╩ ╚═\n[ setup vim ]  [  tool install vim dan setting vim   ]\n╔══════════════════════════════════════════════════════════╗\n║  {•}  Author    :   Tegar ID                             ║\n║  {•}  Team      :   - PARANOID CYBER  ️                   ║\n║                     -【ᏒᎶ4】ʙʟᴀᴄᴋ  ◤coᴅᴇʀ◢ ツ            ║\n║                     - Black Coder Crush                  ║\n║  {•}  Github    :   https://github.com/OfficialDarkAngle ║\n╚══════════════════════════════════════════════════════════╝\n\n              SAVE GAZA PALESTINA\n')

print ("")

print ("(1) untuk installasi")

sel = input('\n     -> ')

if sel == '1':

    instal()

else:

    mengetik()

if __name__ == '__main__':

    main()
