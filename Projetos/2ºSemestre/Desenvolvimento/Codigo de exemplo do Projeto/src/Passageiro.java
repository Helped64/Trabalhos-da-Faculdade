/*Giullia--TIA:31887759
Matheus--TIA:31926142
Tamiris--TIA:31901174*/
import java.util.Scanner;
public class Passageiro{
    String nome;
    String sobrenome;
    String cpf;
    String moradia;
    int num;
    Passageiro[] pass = new Passageiro[10];
    Passageiro(String nome,String sobrenome, String cpf,String moradia){
        this.nome = nome;
        this.cpf = cpf;
        this.moradia = moradia;
        this.sobrenome=sobrenome;
    }
    Passageiro(){
    
    }
    int  registraPassageiro(Passageiro pass[],int i){
        int cont = i + 1;
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o primeiro nome do usuário: ");
        String nome = input.next();
        System.out.println("Digite o sobrenome do usuario: ");
        String sobrenome = input.next();
        System.out.println("Digite o CPF do usuario: ");
        String cpf = input.next();
        System.out.println("Digite onde você mora: ");
        String moradia = input.next();
        pass[i] = new Passageiro();
        pass[i].setNome(nome);
        pass[i].setSobrenome(sobrenome);
        pass[i].setMoradia(moradia);
        pass[i].setCpf(cpf);
        pass[i].num = i;
        return cont;
    }
    void reservar(Passageiro pass[],vagaoTrem vag[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o número da cadeira que sera reservada: ");
        String matricula = input.next();
        System.out.println("Digite o numero de matricula do usuario: ");
        int num = input.nextInt();
        vag[num].setDisponivel(false);
    }
    void sair(vagaoTrem vag[]){
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o numero da cadeira que ficara disponivel: ");
        int num = input.nextInt();
        
        vag[num].setDisponivel(true);
    }
    void mostraDados(){
        System.out.println("");
        System.out.println("Nome: "+this.getNome());
        System.out.println("CPF: "+this.getCpf());
        System.out.println("Local onde mora: "+this.getMoradia());
        System.out.println("");
    }
    void consulta(vagaoTrem vag[],int i){
        for(int k =0;k==i;k++){
            System.out.println("");
            System.out.println("Disponivel: "+vag[i].getDisponivel());
            System.out.println("Numero da cadeira do Vagão: "+vag[i].getNum());
            System.out.println(""); 
        }   
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getSobrenome() {
        return sobrenome;
    }
    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }
    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    public String getMoradia() {
        return moradia;
    }
    public void setMoradia(String moradia) {
        this.moradia = moradia;
    }
    public int getNum() {
        return num;
    }
    public void setNum(int num) {
        this.num = num;
    }
}