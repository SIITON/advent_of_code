using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day_09
{
    class Program
    {
        private static List<List<char>> data;

        static void Main(string[] args)
        {
            data = File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day09\\day_09\\input.txt")
                .Select(line => line.AsEnumerable().ToList())
                .ToList();
            //data = File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day09\\day_09\\testinput.txt")
            //    .Select(line => line.AsEnumerable().ToList())
            //    .ToList();

            var riskLevel = 0;
            for (int i = 0; i < data.Count; i++)
            {
                for (int j = 0; j < data[0].Count; j++)
                {
                    var currentHeight = int.Parse(data[i][j].ToString());
                    var left = (j > 0) ? int.Parse(data[i][j - 1].ToString()) : 1337;
                    var right = (j < data[0].Count - 1) ? int.Parse(data[i][j + 1].ToString()) : 1337;
                    var top = (i > 0) ? int.Parse(data[i - 1][j].ToString()) : 1337;
                    var bottom = (i < data.Count - 1) ? int.Parse(data[i + 1][j].ToString()) : 1337;

                    if (currentHeight < left && currentHeight < right && currentHeight < top && currentHeight < bottom)
                    {
                        riskLevel += currentHeight + 1;
                    }
                }
            }

            Console.WriteLine(riskLevel);
        }
    }
}
