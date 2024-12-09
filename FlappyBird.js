// FlappyBird.js
var config = {
    type: Phaser.AUTO,
    width: 320,
    height: 480,
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);

function preload ()
{
    this.load.image('sky', 'assets/sky.png');
    this.load.image('ground', 'assets/ground.png');
    this.load.image('pipe', 'assets/pipe.png');
    this.load.image('bird', 'assets/bird.png');
}

function create ()
{
    // ... game initialization
}

function update ()
{
    // ... game logic
}
