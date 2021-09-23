import java.lang.Math;
import java.util.Arrays;

public class Polynomial {
    private double[] p;
    private int n;

    public Polynomial(double[] p, int n){// the values above and here not the same
        this.p = p;
        this.n = n;
    }

    public double[] get_coeffs(){
        return this.p;
    }

    public int get_degree(){
        return this.n;
    }

    public double evaluate(double a){
        double value = 0;

        for(int i =0; i <= this.n; i++){
            if(this.p[i] != 0)
                value += this.p[i] * Math.pow(a, i);
        }
        return value;
    }

    public Polynomial add(Polynomial poly_q){
        double[] q = poly_q.get_coeffs();
        int m = poly_q.get_degree();
        int size = Math.max(this.n, m);
        double[] t = new double[size + 1];

        for(int i = 0; i <= Math.min(this.n, m); i++){
            t[i] = this.p[i] + q[i];
        }

        if(size == this.n){
            for(int i = Math.min(this.n, m) + 1; i <= this.n; i++)
                t[i] = this.p[i];
        }else{
            for(int i = Math.min(this.n, m) + 1; i <= m; i++)
                t[i] = q[i];
        }
        
        Polynomial z = new Polynomial(t, size);
        return z;
    }

    public void display_poly(){
        System.out.println(Arrays.toString(this.p));
    }

    public static void main(String[] args){
        double[] poly_1_coeffs = {0, 0, 1, 4};
        double[] poly_2_coeeffs = {3,14,-4,-2,3};
        Polynomial poly_1 = new Polynomial(poly_1_coeffs, 3);
        Polynomial poly_2 = new Polynomial(poly_2_coeeffs, 4);
        //System.out.println(poly_1.evaluate(1));
        Polynomial poly_3 = poly_1.add(poly_2);
        poly_3.display_poly();
    }
}