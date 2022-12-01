using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace day_15
{
    public class PathFinder
    {
        public List<int[]> data;
        private Dictionary<int[], int> pathRisk;
        public List<string> Input { get; set; }

        public int GetPathWithLowestRisk()
        {
            pathRisk = new Dictionary<int[], int>(new IntArrayEqualityComparer()); // Path -> risk

            return RiskOfPoint(new []{0, 0}) - data[0][0];
        }


        /*  start
         *      +-----> y
         *      |
         *      |
         *      V     * 
         *      x       goal
         */
        // Part 1
        public int RiskOfPoint(int[] pos) // [x, y]
        {
            if (pathRisk.ContainsKey(pos))
            {
                return pathRisk[pos];
            }
            if (pos.IsOutOfBoundsGiven(data))
            {
                return int.MaxValue;
            }

            if (pos.IsAtGoalGiven(data))
            {
                return data[pos[0]][pos[1]];
            }
            // move down, or move right. Choose minimal risk.
            var risk = data[pos[0]][pos[1]] + Math.Min(
                RiskOfPoint(new[] { pos[0] + 1, pos[1] }), 
                RiskOfPoint(new[] { pos[0], pos[1] + 1 }));

            pathRisk.Add(pos, risk);
            return risk;
        }

        // Part 2
        public void DijkstrasAlgorithm()
        {
            var unvisited = new Dictionary<int[], bool>(new IntArrayEqualityComparer());
            for (int x = 0; x < data.Count; x++)
            {
                for (int y = 0; y < data[0].Length; y++)
                {
                    unvisited.Add(new int[] { x, y }, true);
                }
            }
        }

        public void ExpandInputSpace()
        {
            var expandedData = new List<int[]>();

            // Expand to the right
            foreach (var line in data)
            {
                int[] newLine = new int[5 * data.Count];
                for (int i = 0; i < 5 * data[0].Length; i += data[0].Length) // 0, 100, 200, 300, 400
                {
                    for (int j = 0; j < data.Count; j++) // 0 - 99
                    {
                        var val = line[j] + i % (data[0].Length - 1);
                        if (val > 9)
                        {
                            val -= 9;
                        }
                        newLine[i + j] = val;
                    }
                }
                expandedData.Add(newLine);
            }
            // Expand down
            var copyOfList = new List<int[]>(expandedData);
            for (int i = 0; i < 4; i++)
            {
                foreach (var line in copyOfList)
                {
                    var newRow = new int[5 * data.Count];
                    for (int j = 0; j < line.Length; j++)
                    {
                        var val = line[j] + i % 9 + 1;
                        if (val > 9)
                        {
                            val -= 9;
                        }

                        newRow[j] = val;
                    }
                    expandedData.Add(newRow);
                }
            }

            data = expandedData;
        }

        public void ParseInput()
        {
            data = Input.Select(line => line.AsEnumerable().Select(p => int.Parse(p.ToString())).ToArray()).ToList();
        }
    }

    public static class Extensions
    {
        public static bool IsOutOfBoundsGiven(this int[] pos, List<int[]> input)
        {
            return pos[0] < 0 || pos[0] >= input.Count || pos[1] < 0 || pos[1] >= input[0].Length;
        }

        public static bool IsAtGoalGiven(this int[] pos, List<int[]> input)
        {
            return pos[0] == input.Count - 1 && pos[1] == input[0].Length - 1;
        }
    }
}
