

from pyAudioAnalysis import audioTrainTest as aT
aT.extract_features_and_train(["C:/Users/asus/Desktop/GTZAN/pop/","C:/Users/asus/Desktop/GTZAN/country/","C:/Users/asus/Desktop/GTZAN/blues/","C:/Users/asus/Desktop/GTZAN/disco/","C:/Users/asus/Desktop/GTZAN/jazz/","C:/Users/asus/Desktop/GTZAN/classical/","C:/Users/asus/Desktop/GTZAN/hiphop/","C:/Users/asus/Desktop/GTZAN/metal/","C:/Users/asus/Desktop/GTZAN/reggae/","C:/Users/asus/Desktop/GTZAN/rock/"], 1.0, 0.5, aT.shortTermWindow, aT.shortTermStep, "svm", "svmMusicGenre3", True)
