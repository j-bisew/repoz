const table = [4, 6, 2];

for (let i in table) {
    if (table[i] < 0) {
        console.log('Błąd: pojawia się liczba ujemna');
        break
    } 
}

if (table[0] > 0 && table[1] > 0 && table[2] > 0) {
    let a = table[0];
    let b = table[1];
    let c = table[2];

    if ( a <= b + c && b <= a + c && c <= b + a) {
        console.log('Nie da się zrobić trójkąta')
    } else {
        console.log('Da się zrobić trójkąt')
    }
}
