'use strict';

// Zim object
  // Characteristics: Needs
  // Methods: increment need, add to queue
// Game loop:
  // Time counter
  // Address queue

function choose(choices) {
    var index = Math.floor(Math.random() * choices.length);
    return choices[index];
};

class Zim {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.myTaskQ = new TaskQ();
        this.bathroomNeed = new BasicNeed("Bathroom",0,1,7);
        this.hungerNeed = new BasicNeed("Hunger",0,1.2,6);
        this.idling = new BasicNeed("Idle",1,0,1);
    }
    
    displayNeeds() {
        let allNeeds = [this.bathroomNeed, this.hungerNeed, this.idling]

        for (let i in allNeeds) {
            console.log(`- ${allNeeds[i].label} need: ${allNeeds[i].currentLvl}`)
            }
        }
        // it would be nice if they were listed in an array 
    
};

class BasicNeed {
    constructor(label, currentLvl, incrementer, threshold) {
    this.label = label;
    this.currentLvl = currentLvl;
    this.incrementer = incrementer;
    this.threshold = threshold;
    }
  // increment func 
};

class Activity {
    constructor(correspondingNeed, label, lvlSatisfied, timeReqd) {
    this.correspondingNeed = correspondingNeed;
    this.label = label;
    this.lvlSatisfied = lvlSatisfied;
    this.timeReqd = timeReqd;
    }
};

class TaskQ {
    constructor() {
        this.elements = [];
    }
  // enqueue: push()
  // dequeue: shift()
  // peek [0]
};

///// INITIALIZE BASIC NEEDS /////
let bathroom = new BasicNeed("Bathroom");
let hunger = new BasicNeed("Hunger");
let idle = new BasicNeed("Idle");

//// INITIALIZE ACTIVITIES /////
let goingPee = new Activity(bathroom,"going pee",6,1);
let haveSnack = new Activity(hunger,"having a snack",5,1)
let readingNews = new Activity(idle,"reading the newspaper",0,1);
let washingDishes = new Activity(idle,"washing the dishes",0,2)

//// ACTIVITIES BY BASIC NEEDS DATABASE OBJECT ////
let activitiesByNeed = {
    bathroom: [goingPee,],
    hunger: [haveSnack,],
    idle: [readingNews,washingDishes,],
};

////// ZIMZ ///////
let peter = new Zim("Peter", "Zim");
let polina = new Zim("Polina", "Zim");

const allZimz = [peter, polina]

/////// HELPER FUNCTIONS ///////
function statusUpdate(allZimz) {
    
    for (const i in allZimz) {
        console.log()
        console.log(`${allZimz[i].firstName}'s needs: ${allZimz[i].displayNeeds()}`) // Needs
        console.log(`${allZimz[i].firstName}'s tasks: ${allZimz[i].myTaskQ.elements}`) // Task Q
        console.log()
    }
};

////////////////// MAIN LOOP ////////////////////////
function mainLoop() {

    let time = 0

    while (time < 5) {

        console.log(`~~The time is ${time}~~`)
        statusUpdate(allZimz)

        time++
    }
    
};

mainLoop()
