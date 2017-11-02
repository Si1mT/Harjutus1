using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class dog : Mammal
    {
        public string Name { get; set; }
        public int Age { get; set; }
        public string Color { get; set; }
        public void woof()
        {
            Console.WriteLine("woof");
        }
    }
}
