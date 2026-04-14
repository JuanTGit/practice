/* 
Type Annotations

JS = const itemName: "plank";
TS = const itemName: string = "plank";
*/

const itemName: string = "Dragon bones";
const itemID: number = 537;
const isMembers: boolean = true;

console.log(itemName);
console.log(itemID);
console.log(isMembers);

/* 
Interfaces
*/

interface Item {
	id: number;
	name: string;
	members: boolean;
}

const dragonBones: Item = {
	id: 537,
	name: "Dragon bones",
	members: true
}

console.log(dragonBones)