var unique = function (orig) {
    "use strict";
    var a = [];
    orig.forEach(function (item) {
        if (-1 === a.indexOf(item)) {
            a.push(item);
        }
    });
    return a;
};
