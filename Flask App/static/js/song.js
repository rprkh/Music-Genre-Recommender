var playBtn = document.getElementById("playBtn");

var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor: '#ddd',
    progressColor: '#ff006c',
    barWidth: 4,
    responsive: true,
    height: 90,
    barRadius: 4
});

wavesurfer.load('static/songs/Autumn Leaves.m4a');

playBtn.onclick = function() {
    wavesurfer.playPause();
    if(playBtn.src.includes('static/images/play.png')) {
        playBtn.src = "static/images/pause.png";
    }
    else {
        playBtn.src = 'static/images/play.png';
    }
};

wavesurfer.on('finish', function() {
    playBtn.src = 'static/images/play.png';
    wavesurfer.stop()
});