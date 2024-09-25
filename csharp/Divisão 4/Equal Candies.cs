using System;
class HelloWorld {
  static void Main() {
    int n = int.Parse(Console.ReadLine());
    int doces = 0;
    for(int i = 1; i <= n; i++)
    {
       int tam = int.Parse(Console.ReadLine());
       string[] s = Console.ReadLine().Split(' ');
       int menor = int.Parse(s[0]);
       for(int j = 1; j < tam; j++)
       {
           if(int.Parse(s[j]) < menor) 
           menor = int.Parse(s[j]);
       }
       for(int j = 0; j < tam; j++)
       {
           int x = int.Parse(s[j]);
           doces += x - menor;
           
       }
       Console.WriteLine(doces);
       doces = 0;
    }
    
  }
}