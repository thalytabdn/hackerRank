function diagonalDifference(arr) {
    let primary = 0
    let secondary = 0
    let aux = arr[0].lenght

    for (let index = 0; index < aux; index++) {
        primary += arr[index][index]
        primary += arr[index][aux - i - 1]
    }

    return secondary - primary
}

const a = [[11,2,4],[4,5,6],[10,8,-12]]
console.log(diagonalDifference(a))