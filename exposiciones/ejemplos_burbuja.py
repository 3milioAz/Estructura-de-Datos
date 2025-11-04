

def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
print("Lista ordenada:", burbuja(numeros))



public class Burbuja {
    public static void main(String[] args) {
        int[] numeros = {5, 2, 9, 1, 5, 6};
        bubbleSort(numeros);

        System.out.print("Lista ordenada: ");
        for (int num : numeros) {
            System.out.print(num + " ");
        }
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Intercambiar los elementos
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}


