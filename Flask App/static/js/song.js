var playBtn = document.getElementById('playBtn');
var playBtnSong2 = document.getElementById('playBtnSong2');
var playBtnSong3 = document.getElementById('playBtnSong3');

var songNames = document.getElementsByClassName('names');
var cosSim = document.getElementsByClassName('cossim');

var songNamesContainer = [];
var cosSimContainer = [];

for(var i = 0; i < songNames.length; i++) {
    songNamesContainer.push(songNames[i].innerText);
}

for(var j = 0; j < cosSim.length; j++) {
    var cosSimScore = cosSim[j].innerText;
    cosSimScore = cosSimScore.split(': ')[1]
    cosSimContainer.push(cosSimScore);
}

var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor: '#ddd',
    progressColor: '#16a085',
    barWidth: 4,
    responsive: true,
    height: 70,
    barRadius: 4
});

var wavesurfer2 = WaveSurfer.create({
    container: '#waveform2',
    waveColor: '#ddd',
    progressColor: '#16a085',
    barWidth: 4,
    responsive: true,
    height: 70,
    barRadius: 4
});

var wavesurfer3 = WaveSurfer.create({
    container: '#waveform3',
    waveColor: '#ddd',
    progressColor: '#16a085',
    barWidth: 4,
    responsive: true,
    height: 70,
    barRadius: 4
});

wavesurfer.load('static/songs/' + songNamesContainer[0] + '.m4a');

playBtn.onclick = function() {
    wavesurfer.playPause();
    if(playBtn.src.includes('static/images/play_button.jpg')) {
        playBtn.src = "static/images/pause_button.jpg";
    }
    else {
        playBtn.src = 'static/images/play_button.jpg';
    }
};

wavesurfer.on('finish', function() {
    playBtn.src = 'static/images/play_button.jpg';
    wavesurfer.stop()
});

wavesurfer2.load('static/songs/' + songNamesContainer[1] + '.m4a');

playBtnSong2.onclick = function() {
    wavesurfer2.playPause();
    if(playBtnSong2.src.includes('static/images/play_button.jpg')) {
        playBtnSong2.src = "static/images/pause_button.jpg";
    }
    else {
        playBtnSong2.src = 'static/images/play_button.jpg';
    }
};

wavesurfer2.on('finish', function() {
    playBtnSong2.src = 'static/images/play_button.jpg';
    wavesurfer2.stop()
});

wavesurfer3.load('static/songs/' + songNamesContainer[2] + '.m4a');

playBtnSong3.onclick = function() {
    wavesurfer3.playPause();
    if(playBtnSong3.src.includes('static/images/play_button.jpg')) {
        playBtnSong3.src = 'static/images/pause_button.jpg';
    }
    else {
        playBtnSong3.src = 'static/images/play_button.jpg';
    }
};

wavesurfer3.on('finish', function() {
    playBtnSong3.src = 'static/images/play_button.jpg';
    wavesurfer3.stop()
});