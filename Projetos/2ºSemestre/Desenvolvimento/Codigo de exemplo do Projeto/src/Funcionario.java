/*Giullia--TIA:31887759
Matheus--TIA:31926142
Tamiris--TIA:31901174*/
public class Funcionario{
    String nome;
    String sobrenome;
    String cpf;
    int num;
    String matricula;
    
    Funcionario(String nome,String sobrenome, String cpf,String matricula){
        this.matricula = matricula;
        this.nome = nome;
        this.cpf = cpf;
        this.sobrenome=sobrenome;
    }
    Funcionario(){
    
    }
     void consultaPassageiro(Passageiro pass[],int i){
        for(int k =0;k==i;k++){
            System.out.println("");
            System.out.println("Nome: "+pass[i].getNome());
            System.out.println("Sobrenome: "+pass[i].getSobrenome());
            System.out.println("CPF: "+pass[i].getCpf());
            System.out.println("Local onde Mora: "+pass[i].getMoradia());
            System.out.println("Matricula do usuario: "+pass[i].getNum());
            System.out.println(""); 
        }
    } 
    
    int registraLugar(vagaoTrem vag[],int i){
        int cont = i+25;
        vag[i] = new vagaoTrem();
        vag[i].setDisponivel(true);
        vag[i].setNum(i);
        return cont;
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
    public String getMatricula() {
        return matricula;
    }
    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }
    public int getNum() {
        return num;
    }
    public void setNum(int num) {
        this.num = num;
    }
}