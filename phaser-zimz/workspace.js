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
        
        this.basicNeeds = [this.bathroomNeed, 
            this.hungerNeed, this.idling];
    }
};

class BasicNeed {
    constructor(label, currentLvl, incrementer, threshold) {
    this.label = label;
    this.currentLvl = currentLvl;
    this.incrementer = incrementer;
    this.threshold = threshold;
    }
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
    "Bathroom": [goingPee,],
    "Hunger": [haveSnack,],
    "Idle": [readingNews,washingDishes,]
};
// I can't figure out how to iterate through the subarrays, and therefore 
// to check the Q for things that are in the Q already 

////// ZIMZ ///////
let peter = new Zim("Peter", "Zim");
let polina = new Zim("Polina", "Zim");

const allZimz = [peter, polina]

/** Creates testing conditions where the two zimz have slightly varied needs */
function testSetUp() {
    // sets up different need levels for peter and polina
    peter.bathroomNeed.currentLvl = 4
    peter.hungerNeed.currentLvl = 2
    polina.hungerNeed.currentLvl = 5 
    polina.bathroomNeed.threshold = 8
};

/////// HELPER FUNCTIONS ///////
function randomChoice(choices) {
    let index = Math.floor(Math.random() * choices.length);
    return choices[index];
}

//** Console Logs the current needs and taskQ */
function statusUpdate(zim) {
    console.log()
    console.log(`${zim.firstName}'s needs:`) // Needs
    console.log(zim.basicNeeds)
    console.log(`${zim.firstName}'s tasks: ${zim.myTaskQ.elements}`) // Task Q
    console.log()
}

/** Updates the currentLvl by adding the incrementer */
function updateZimNeeds(zim) {
    for (const need of zim.basicNeeds) {
        need.currentLvl += need.incrementer
    }
}

// function isInQ(zim, activity) {
// // activity is 
// }

function checkThresholdsAddTasks(zim) {
    for (const need of zim.basicNeeds) {
        if (need.currentLvl >= need.threshold) {
            if (need.label == "Idle" && zim.myTaskQ.elements.length > 0) {
                continue
            }
            let newActivity = randomChoice(activitiesByNeed[need]) 
            // this is having issues because this gets an object not an array 
            // Only seems to work with .label
            
            // check before adding the label to Q
            zim.myTaskQ.elements.push(newActivity.label)
            // if newTask.... i'd have to look through the existing task Q 
            // to see if it's already represented 
        }
    }
    // need to not add the task if it's already represented in the task q
}



////////////////// MAIN LOOP ////////////////////////
function mainLoop() {
    
    testSetUp()
    
    let time = 0

    while (time < 5) {

        console.log(`~~The time is ${time}~~`)

        for (const zim of allZimz) {
            statusUpdate(zim)
            updateZimNeeds(zim)
            checkThresholdsAddTasks(zim)
        }

        time++
    }
    
};

// mainLoop()

