package com.mx.curso.unidad1;

import java.util.Vector;

public class EjercicioVector {

    public static void main(String[] args)  {

        Vector<Double> vector = new Vector<>();
        vector.add(1.85);
        vector.add(68.0);
        vector.add(19.0);

        System.out.println(vector.get(0));

        System.out.println("Modificacion: "+ vector.set(0,1.90));

        double sum=0;

        for(Double d: vector){
            sum+=d;
        }

        double media = sum/vector.size();

        System.out.println("Media de mis caracteristicas: "+ media);

    }
}