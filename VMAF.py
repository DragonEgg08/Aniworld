import os
import subprocess
import sys
from pathlib import Path

Endgültige_Qualität = []
def VMAF_Score_Rechner(Output: Path):
    Output = open(Output).read().split("\n")
    Array = []
    Höchster_Score = 0.0
    Niedrigster_Score_Array = []
    Scores = [0,0,0,0]
    Rechnung = 0
    for i in Output:
        try:
            if i.split(" ")[8] == '"vmaf":':
                Array.append(i.split(" ")[-1])
        except:
            None
    for i in Array:
        Rechnung += float(i)

    #Berechnung Niedrigster und Höchster Scores
    for i in Array:
        i = float(i)
        if i > Höchster_Score:
            Höchster_Score = i
        if 95 <= i <= 100:
            Scores[0] += 1
    #Finden gleich schlechter Frames
    for i in Array:
        i = float(i)
        if 0 <= i <= 69:
            Niedrigster_Score_Array.append(i)
    Endgültige_Qualität.append(Rechnung / len(Array))
    print(f"\nQualität berechnet: {str(Endgültige_Qualität)}")
    print("Höchster Score: " + str(Höchster_Score))
    print(str(round(len(Niedrigster_Score_Array)/len(Array)*100, 3)) + f"% schlechte Frames (Score 0-69; {len(Niedrigster_Score_Array)} von {len(Array)} Frames)")


    for i in Niedrigster_Score_Array:
        if 49.5 < i <= 69:
            Scores[1] += 1
        elif 29.5 < i <= 49.5:
            Scores[2] += 1
        elif 0 < i <= 29.5:
            Scores[3] += 1
    try:
        print(f"\nScores für die Frames:\nScore 100-95: {Scores[0]}; {round(Scores[0] / len(Array) * 100, 2)}% Netflix' 'Unsichtbare Komprimierung'")
        print(f"Score 69-50: {Scores[1]}; {round(Scores[1]/len(Niedrigster_Score_Array)*100, 2)}% Durchschnittliche Qualität, sichtbare Artefakte und Verluste")
        print(f"Score 30-49: {Scores[2]}; {round(Scores[2]/len(Niedrigster_Score_Array)*100, 2)}% Unterdurchschnittliche Qualität, deutliche Artefakte und Verluste")
        print(f"Score 0-29: {Scores[3]}; {round(Scores[3]/len(Niedrigster_Score_Array)*100, 2)}% Schlechte Qualität, stark beeinträchtigt")
    except ZeroDivisionError:
        print("ZDE")

#90-100: Exzellente Qualität, kaum wahrnehmbare Unterschiede zum Original.
#70-89: Gute Qualität, geringe Artefakte oder Verluste.
#50-69: Durchschnittliche Qualität, sichtbare Artefakte und Verluste.
#30-49: Unterdurchschnittliche Qualität, deutliche Artefakte und Verluste.
#0-29: Schlechte Qualität, stark beeinträchtigt

def Qualität_berechnen(Video_Original: str, Video_Komprimiert: str):
    Befehl = (
        f'ffmpeg -i {Video_Original} -i {Video_Komprimiert} ' 
        '-lavfi "[0:v]scale[scaled_ref];[scaled_ref]format=yuv420p[ref];'
        '[1:v]scale[scaled_dist];[scaled_dist]format=yuv420p[dist];'
        '[ref][dist]libvmaf=log_path=vmaf_results.json:log_fmt=json:n_threads=16"'
        ' -f null -'
    )
    os.system(f'start cmd /k "{"X: &&" + Befehl}" && exit')

Was_tun = input("Möchtest du die Qualität berechen [QB] oder die Qualität Auswerten [QA]?: ").lower()

if Was_tun == "qb":
    Qualität_berechnen(input("Bitte Pfad Originalvideo: "), input("Bitte Pfad Komprimiertes Video: "))
elif Was_tun == "qa":
    VMAF_Score_Rechner("X:\\vmaf_results.json")