using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day_07
{
    class Program
    {
        static void Main(string[] args)
        {
            // Part 1
            var crabSubs = new CrabSubmarines();
            crabSubs.SetHorizontalPositions("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day07\\day_07\\input.txt");
            var fuelCost = crabSubs.GetLowestFuelCostWhenAligned();
            Console.WriteLine(fuelCost);

            // Part 2
            var actualFuelCost = crabSubs.GetTheActualLowestFuelCostWhenAligned();
            Console.WriteLine(actualFuelCost);
        }
    }

    
}
