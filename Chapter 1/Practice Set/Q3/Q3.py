
#Solution of Practice Set Q3
# from playsoound import playsound

# playsound.playsound(r"D:\Sound.wav")

#For Some reason This code doesn't work anymore so i am using inbuilt winsound Module

'''
For some reason Module couldn't get resolved in VSCode.
For fixing this add this line in Setting.json of vscode. 

"python.analysis.extraPaths":["./core"]

Setting.json can be opened by Command pallatte in VScode

'''
#winsound can only play wav file
import winsound

filename = 'D:\\Fuuka.wav' #Remeber to put the song Path name here with \\ instead of \
winsound.PlaySound(filename, winsound.SND_FILENAME)