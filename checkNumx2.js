let arr = [2, 4, 5, 9, 8]

function checkNumX2(arr){
    const checked = {};

    for (let num = 0; num < arr.length; num++){
        if (checked[arr[num] * 2] !== undefined || checked[arr[num] / 2] !== undefined){
            return true;
        }
        checked[arr[num]] = num;
    }
    return false;
}

console.log(checkNumX2(arr))