using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class Mammal
    {
        public Mammal()
        {
            numberOfEyes = 2;
            isCarnivore = true;
            Breathe();
        }
        public int numberOfEyes { get; set; }
        public bool isCarnivore { get; set; }
        public void Breathe()
        {
            Console.WriteLine("breathe");
        }
    }
}
