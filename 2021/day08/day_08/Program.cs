using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day_08
{
    class Program
    {
        static void Main(string[] args)
        {
            // Part 1
            var input = File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day08\\day_08\\input.txt")
                                      .ToList();

            var theTerminator = new SignalDeterminator();
            theTerminator.Input = input;
            var count = theTerminator.DecodeByLength(s => s is 2 or 3 or 4 or 7);

            Console.WriteLine(count);

        }
    }
}
