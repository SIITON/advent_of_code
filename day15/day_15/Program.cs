using System;
using System.IO;
using System.Linq;

namespace day_15
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllLines(
                "C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day15\\day_15\\input.txt").ToList();
            var finder = new PathFinder();
            finder.Input = input;

            var risk = finder.GetPathWithLowestRisk();
            Console.WriteLine($"Part 1, risk: {risk}");
        }
    }
}
