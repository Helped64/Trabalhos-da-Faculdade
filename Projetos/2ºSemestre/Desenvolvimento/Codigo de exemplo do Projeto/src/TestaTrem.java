/*Giullia--TIA:31887759
Matheus--TIA:31926142
Tamiris--TIA:31901174*/
import java.util.Scanner;


public class TestaTrem {
    public static void main(String[] args) {
        vagaoTrem[] vag = new vagaoTrem[10];
        Passageiro[] pass = new Passageiro[10];
        Scanner input = new Scanner (System.in);
        Passageiro pass1 = new Passageiro(); 
        Funcionario func1 = new Funcionario();
        int op =0;
        int cont = 0;
        func1.registraLugar(vag, cont);
        while( op!=6){
            System.out.println("Para consultar, é necessário realizar um cadastro antecipadamente");
            System.out.println("");
            System.out.println("Digite 1 para cadastrar um Passageiro/Usuario: "
                    + "\nDigite 2 para mostrar Passageiros cadastrados: "
                    + "\nDigite 3 para mostrar Lugares Disponiveis: "
                    + "\nDigite 4 para realizar Reserva: "
                    + "\nDigite 5 para finalizar Reserva: "
                    + "\nDigite 6 para sair do sistema: ");
            op = input.nextInt();
            if (op ==1){
               pass1.registraPassageiro(pass,cont);
            }
            
            if (op==2){
                func1.consultaPassageiro(pass, cont);
            }
            
            if (op==3){
               pass1.consulta(vag, cont);
            }
            
            if (op ==4){
                pass1.reservar(pass, vag);
            }
            
            if (op ==5){
                pass1.sair(vag);
            }
        }
    }
}
