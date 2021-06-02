/*Giullia--TIA:31887759
Matheus--TIA:31926142
Tamiris--TIA:31901174*/
public class vagaoTrem {
    boolean disponivel;
    int num;
    vagaoTrem[] vag = new vagaoTrem[10];
   
    void mostrar(vagaoTrem vag[],int i){
        System.out.println("");
        System.out.println("Disponivel: "+vag[i].getDisponivel());
        System.out.println("Número do acento: "+vag[i].getNum());
        System.out.println("");
        System.out.println("");  
    }
    public boolean getDisponivel() {
        return disponivel;
    }
    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }
    public int getNum() {
        return num;
    }
    public void setNum(int num) {
        this.num = num;
    }
    
}
