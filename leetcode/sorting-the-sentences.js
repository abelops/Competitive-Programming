/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let splited = s.split(" ")
    let final = ""
    for(let j=1; j<=splited.length; j++){
        for(let i=0; i < splited.length; i++){
            let num = splited[i].split("")
            let tex = splited[i].slice(0, splited[i].length-1)
            num = num[num.length-1]
            if(parseInt(num)==j){
                final +=tex
                if(j!=splited.length)
                    final+= " "
            }
        }
    }
    return final
};