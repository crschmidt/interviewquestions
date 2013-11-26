function anagrams(words) {
    var groups = {}
    for (var i = 0; i < words.length; i++) {
        var word = words[i];
        var chars = word.split("");
        chars.sort();
        var key = chars.join("");
        if (!groups[key]) {
            groups[key] = []
        }    
        groups[key].push(word)
    }
    var output = []
    for (var key in groups) {
        output.push(groups[key])
    }
    output.sort();
    return output;
}
console.log(anagrams(["art", "rat", "bats", "banana", "stab", "tar"]));
