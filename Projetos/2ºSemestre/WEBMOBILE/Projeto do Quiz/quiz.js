function validar(){
    var confirmado;
    var q1 = form1.questao1.value;
    var q2 = form1.questao2.value;
    var q3 = form1.questao3.value;
    var q4 = form1.questao4.value;
    var q5 = form1.questao5.value;
    var q6 = form1.questao6.value;
    var q7 = form1.questao7.value;
    if (q1 == false){
        alert("Preencha a pergunta 1");
        form1.questao1.focus;
        var confirmado = false;
        return false;
    }
    if (q2 == false){
        alert("Preencha a pergunta 2");
        form1.questao2.focus;
        var confirmado = false;
        return false;
    }
    if (q3 == false){
        alert("Preencha a pergunta 3");
        form1.questao3.focus;
        var confirmado = false;
        return false;
    }
    if (q4 == false){
        alert("Preencha a pergunta 4");
        form1.questao4.focus;
        var confirmado = false;
        return false;
    }
    if (q5 == false){
        alert("Preencha a pergunta 5");
        form1.questao5.focus;
        var confirmado = false;
        return false;
    }
    if (q6 == false){
        alert("Preencha a pergunta 6");
        form1.questao6.focus;
        var confirmado = false;
        return false;
        }
    if (q7 == false){
        alert("Preencha a pergunta 7");
        form1.questao7.focus;
        var confirmado = false;
        return false;
        }
    else{
        var confirmado = true;
    }
    while(confirmado=true){
        var i ;
        var cont = 0;
        var q1 = document.getElementById("r1");
        var q2 = document.getElementById("r2");
        var q3 = document.getElementById("r3");
        var q4 = document.getElementById("r4");
        var q5 = document.getElementById("r5");
        var q6 = document.getElementById("r6");
        var q7 = document.getElementById("r7");
        var gabarito = [q1,q2,q3,q4,q5,q6,q7,]
        for (var i =0; i<7;i++){
            if( gabarito[i].checked == true){
                cont ++
            }
        }
        alert("Você acertou: "+cont+" perguntas(s)");
    }
}