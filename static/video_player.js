
function play_video(){
    v = document.getElementById('query_video');
    b = document.getElementById('play_button');
    if(v.paused || v.ended){
        console.log("play video...")
        b.innerText = "Pause";
        v.play();
    }
    else if(v.play){
        console.log("pause video...")
        b.innerText = "Play";
        v.pause();
    }
}

// scroll bar

// elapsed time