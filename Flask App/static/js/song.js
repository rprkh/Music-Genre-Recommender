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

console.log(songNamesContainer);
console.log(cosSimContainer);

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

wavesurfer2.load('static/songs/Bohemian Rhapsody (Remastered 2011).m4a');

playBtnSong2.onclick = function() {
    wavesurfer2.playPause();
    if(playBtnSong2.src.includes('static/images/play.png')) {
        playBtnSong2.src = "static/images/pause.png";
    }
    else {
        playBtnSong2.src = 'static/images/play.png';
    }
};

wavesurfer2.on('finish', function() {
    playBtnSong2.src = 'static/images/play.png';
    wavesurfer2.stop()
});

wavesurfer3.load('static/songs/Ride of the Valkyries.m4a');

playBtnSong3.onclick = function() {
    wavesurfer3.playPause();
    if(playBtnSong3.src.includes('static/images/play.png')) {
        playBtnSong3.src = 'static/images/pause.png';
    }
    else {
        playBtnSong3.src = 'static/images/play.png';
    }
};

wavesurfer3.on('finish', function() {
    playBtnSong3.src = 'static/images/play.png';
    wavesurfer3.stop()
});