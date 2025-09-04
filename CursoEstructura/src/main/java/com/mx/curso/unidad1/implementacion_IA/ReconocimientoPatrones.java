package com.mx.curso.unidad1.implementacion_IA;

import java.util.Vector;

public class ReconocimientoPatrones {

    public static void main(String[] args) {

        Vector<Double> caracteristicas = new Vector<>();
        caracteristicas.add(3.5);
        caracteristicas.add(1.4);
        caracteristicas.add(0.2);

        System.out.println("Vector Original: " + caracteristicas);

        double sum = 0.0D;
        for (Double d : caracteristicas) {
            sum += d;
        }

        for (int i = 0; i < caracteristicas.size(); i++) {
            double valor = caracteristicas.get(i);
            double valorNormalizado = valor / sum;
            caracteristicas.set(i, valorNormalizado);
        }
        System.out.println("Vector Normalizado: " + caracteristicas);


    }
}