let table = [1, 5, 34, 98, -4, 0, 3, 9, 9, 92, 54, 2, -45]

for (let x in table) {
    console.log(table[x])
}

let max = table[0];
let min = table[0];
for (let i in table) {
    if (max < table[i]) {
        max = table[i];
    } else if ( min > table[i]) {
        min = table[i];
    }
}
console.log('Maksimum to ' + max, '\nMinimum to ' + min)

let table2 = table

let first = table2[0];
table2[0] = table2[table2.length - 1];
table2[-1] = first

console.log('Teraz pierwsza liczba to ' + table2[0], '\nA ostatnia to ' + table2[-1])