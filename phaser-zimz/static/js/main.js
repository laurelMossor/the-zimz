"use strict";

const config = {
    type: Phaser.AUTO,
    width: 900,
    height: 650,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 200 }
        }
    },
    scene: {
        preload: preload,
        create: create
    }
};

const game = new Phaser.Game(config);

function preload () {
        this.load.image('toilet', 'static/assets/toilet.png');
        this.load.image('peter', 'static/assets/Peter.png');
        this.load.image('amy', 'static/assets/Amy.png')


    }
function create () {
    this.add.image(700,500, "toilet").setDisplaySize(50,75)
    this.add.image(200,200, "peter").setDisplaySize(50,120)
    this.add.image(400,250, "amy").setDisplaySize(50,120)

    }


