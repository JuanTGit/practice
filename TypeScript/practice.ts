/* 
Type Annotations

JS = const itemName: "plank";
TS = const itemName: string = "plank";
*/
console.log("===============Type Annotations===============")
const itemName: string = "Dragon bones";
// const itemID: number = 4151;
const isMembers: boolean = true;

console.log(itemName);
// console.log(itemID);
console.log(isMembers);

/* 
Interfaces
*/
console.log("===============Interfaces===============")
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

/* 
Typed Functions
*/
console.log("===============Typed Functions===============")
// Function that returns a value
function formatItemName(name: string): string {
	return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
}
// Void = do something not give something back. (side effect)
function logPrice(price: number): void {
	console.log(`Price: ${price.toLocaleString()} gp`);
}

console.log(formatItemName("dragon bones"));
logPrice(4200);

/* 
Async Functions
*/
console.log("===============Async Functions with Types===============")

interface PriceData {
	high: number;
	hightTime?: number; // optional — might use it later
	low: number;
	lowTime?: number; // optional — might use it later
}

async function getItemPrice(itemId: number): Promise<PriceData> {
	const response = await fetch(
		`https://prices.runescape.wiki/api/v1/osrs/latest?id=${itemId}`
	);

	if (!response.ok) {
		throw new Error(`Failed to fetch price for item ${itemId}`);
	}

	const data = await response.json();
	return data.data[itemId]
}

getItemPrice(4151).then(price => {
	// console.log(price);
	console.log(`${price.high.toLocaleString()} gp`);
})


/* 
Arrays and Optional Properties
*/
console.log("===============Arrays and Optional Properties===============")

const itemIds: number[] = [4151, 383, 11802];
const itemNames: string[] = ['Abyssal whip', 'Raw shark', 'Armadyl godsword'];


const lastHistory: PriceData[] = [];

lastHistory.push({ high: 4500, low: 4000 });
lastHistory.push({ high: 4200, low: 3800 });


interface PriceHistory {
	itemId: number;
	high: number;
	low: number;
	timestamp?: Date;
}

const history: PriceHistory[] = [];

history.push({ itemId: 4151, high: 4500, low: 4000 });
history.push({ itemId: 4151, high: 4700, low: 4300, timestamp: new Date() });

console.log(history);
