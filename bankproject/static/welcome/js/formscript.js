function populate(district,branch){

    var s1 = document.getElementById(district);
    var s2 = document.getElementById(branch);

    s2.innerHTML="";

    if(s1.value == "kottayam"){
        var oprionArray = ['pala|Pala', 'kanjirappally|Kanjirappally', 'pampady|Pampady', 'manarkad|Manarkad', 'mundakkayam|Mundakkayam'];
    }
   else if(s1.value == "idukki"){
        var oprionArray = ['kattappana|Kattappana', 'kuttikkanam|Kuttikkanam', 'peerumedu|Peerumedu', 'thodupuzha|Thodupuzha', 'kumily|Kumily'];
    }
    else if(s1.value == "ernakulam"){
        var oprionArray = ['kaloor|Kaloor', 'edappally|Edappally', 'aluva|Aluva', 'kothamangalam|Kothamangalam', 'palarivattom|Palarivattom'];
    }
    else if(s1.value == "thrissur"){
        var oprionArray = ['alur|Alur', 'chalakkudy|Chalakkudy', 'chemmannur|Chemmannur', 'edassery|Edassery', 'mambra|Mambra'];
    }
    else if(s1.value == "kozhikode"){
        var oprionArray = ['beypore|Beypore', 'calicutcity|Calicut City', 'cherukad|Cherukad', 'kabanigiri|Kabanigiri', 'mavoor|Mavoor'];
    }

    for(var option in oprionArray){
        var pair = oprionArray[option].split("|");
        var newoption = document.createElement("option");

        newoption.value = pair[0];
        newoption.innerHTML = pair[1];
        s2.options.add(newoption);
    }

}