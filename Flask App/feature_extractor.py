import numpy as np
import librosa

def audio_feature_extractor(filepath):
    y, sr = librosa.load(filepath)
    chroma_stft = librosa.feature.chroma_stft(y = y, sr = sr)
    rms = librosa.feature.rms(y = y)
    spec_centroid = librosa.feature.spectral_centroid(y, sr = sr)[0]
    spec_bw = librosa.feature.spectral_bandwidth(y = y, sr = sr)
    spec_rolloff = librosa.feature.spectral_rolloff(y, sr = sr)[0]
    zero_crossing = librosa.feature.zero_crossing_rate(y)
    harmony = librosa.effects.harmonic(y)
    per = librosa.effects.percussive(y)
    tempo, _ = librosa.beat.beat_track(y, sr = sr)  
    mfcc = librosa.feature.mfcc(y = y, sr = sr)

    data = {
        'length': y.shape[0],
        'chroma_stft_mean': np.mean(chroma_stft),
        'chroma_stft_var': np.var(chroma_stft),
        'rms_mean': np.mean(rms),
        'rms_var': np.var(rms),
        'spectral_centroid_mean': np.mean(spec_centroid),
        'spectral_centroid_var': np.var(spec_centroid),
        'spectral_bandwidth_mean': np.mean(spec_bw),
        'spectral_bandwidth_var': np.var(spec_bw),
        'rolloff_mean': np.mean(spec_rolloff),
        'rolloff_var': np.var(spec_rolloff),
        'zero_crossing_rate_mean': np.mean(zero_crossing),
        'zero_crossing_rate_var': np.var(zero_crossing),
        'harmony_mean': np.mean(harmony),
        'harmony_var': np.var(harmony),
        'perceptr_mean': np.mean(per),
        'perceptr_var': np.var(per),
        'tempo': tempo,
    }

    for i in range(1, 21):
        data.update({'mfcc' + str(i) + '_mean': np.mean(mfcc[i - 1])})
        data.update({'mfcc' + str(i) + '_var': np.var(mfcc[i - 1])})

    return data