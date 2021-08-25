// PROCESSOR.JS
// Gets each frame from the video element, and runs it through a canvas element. This will be used to draw over top of the video. 
//

var i = 0;
var video_objects = {};
let processor = {
    timerCallback: function () {
        console.log("TimerCallback");
        if (this.video.paused || this.video.ended) {
            return;
        }
        this.computeFrame();
        let self = this;
        setTimeout(function () {
            self.timerCallback();
        }, 0);
    },

    doLoad: function () {
        console.log("doLoad");
        this.video = document.getElementById("query_video");
        this.canvas = document.getElementById("canvas");
        canvas.style.position = "absolute";
        canvas.style.top = video.offsetTop+"px";
        canvas.style.height = (window.innerHeight * 0.5)+"px";
        
        this.ctx1 = this.canvas.getContext("2d");
        let self = this;
        
        this.video.addEventListener("play", function () {
            self.width = self.video.videoWidth;
            self.height = self.video.videoHeight;
            self.timerCallback();
        }, false);
    },

    
    computeFrame: function () {
        console.log("<"+i+">, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>");
        console.log("<"+i+">, <"+objects_in_frame[i++][1]+">, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>");
        // Print out the result of tracking each frame
        console.log(objects_in_frame[i++]);
        
        // Loop through detected objects

        // draw lines around objects based on coordinates provided by "backend"
        this.ctx1.drawImage(this.video, 0, 0, this.width, this.height);
        let frame = this.ctx1.getImageData(0, 0, this.width, this.height);
        
        // crop frame to object only, and append to list of unique objects

        // The result of the object tracking output, 
        
        
        return;
    }
};

document.addEventListener("DOMContentLoaded", () => {
    processor.doLoad();
});


// Identify objects which may be associated