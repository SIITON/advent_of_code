using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace day_01
{
    class Program
    {
        static void Main(string[] args)
        {

            var data =
                File.ReadAllLines("C:\\Users\\simon.tonnes\\source\\repos\\advent_of_code\\day01\\day_01\\input.txt").ToList();
            var testdata = new List<string>()
            {
                "199",
                "200",
                "208",
                "210",
                "200",
                "207",
                "240",
                "269",
                "260",
                "263"
            };
            var count = GetDepthIncreases(data);
            Console.WriteLine($"Part 1: {count} ");

            var slidingCount = GetDepthIncreasesSlidingWindow(data);
            Console.WriteLine($"Part 2: {slidingCount} ");
        }

        public static int GetDepthIncreasesSlidingWindow(List<string> data)
        {
            var count = 0;
            var measurements = data.Select(int.Parse).ToList();
            var lastDepth = measurements[0] + measurements[1] + measurements[2];
            for (int i = 0; i < data.Count - 2; i++)
            {
                var depthSum = measurements[i] + measurements[i + 1] + measurements[i + 2];
                if (depthSum > lastDepth)
                {
                    count++;
                }
                lastDepth = depthSum;
            }
            return count;
        }

        public static int GetDepthIncreases(List<string> data)
        {
            var count = 0;
            var lastDepth = int.Parse(data[0]);
            foreach (var depth in data.Select(int.Parse))
            {
                if (depth > lastDepth)
                {
                    count++;
                }
                lastDepth = depth;
            }

            return count;
        }
    }
}
