using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day_14
{
    class Program
    {
        private static List<string> _recipes;

        static void Main(string[] args)
        {
            // Part 1
            var sub = new SubmarineEquipment();
            sub.FindPolymerByInsertion();
            
            // Part 2
            var counts = sub.FindPolymerCounts();

            foreach (var charPair in counts)
            {
                Console.WriteLine($"{charPair.Key} : {charPair.Value}");
            }

            var maxKey = counts.Values.Max();
            var minKey = counts.Values.Min();
            Console.WriteLine($"max: {maxKey} - min: {minKey} = {maxKey-minKey}");

        }

        
    }
}
