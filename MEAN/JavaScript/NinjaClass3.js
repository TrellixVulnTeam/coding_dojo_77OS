class Ninja {
    constructor(name){
    this.name = name;
    this.health = 100;
    this.speed = 3;
    this.strenght = 3; 
    }
    sayName(){
        console.log(`My ninja name is ${this.name}!`);
        
    }
    showStats(){
        console.log(`Name: ${this.name}, Health: ${this.health}, Speed: ${this.speed}, Strength: ${this.strenght}`);
    }
    drinkShake(){
       this.health += 10
       
    }
  
}
const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.drinkShake()
ninja1.showStats();
