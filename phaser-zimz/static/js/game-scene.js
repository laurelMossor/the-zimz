"use strict";


export default class GameScene extends Phaser.Scene {
    constructor() {
        super('game-scene')

    }

    preload() {
        this.load.image('toilet', 'static/assets/toilet.png');
        this.load.image('peter', 'static/assets/Peter.png');
        this.load.image('amy', 'static/assets/Amy.png')


    }
    create() {


    }

};